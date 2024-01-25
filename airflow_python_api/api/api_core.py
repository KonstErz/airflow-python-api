import base64
import json
import logging
import urllib.request
import urllib.error
from typing import Union


logger = logging.getLogger(__name__)


class ApiCore:
    """
    Base class for Airflow API endpoints
    """

    def __init__(self, configuration):
        self.configuration = configuration

    def _set_proxies(self, request_obj):
        for pr_type, pr_addr in self.configuration.proxies.items():
            request_obj.set_proxy(pr_addr, pr_type)
        return request_obj

    def _update_total_headers(self, current_headers: dict, total_headers: dict) -> dict:
        for k, v in current_headers.items():
            if k not in total_headers:
                total_headers.update({k: v})
        return total_headers

    def get_basic_auth_token(self) -> str:
        """
        Get token for basic HTTP authentication
        """

        username = self.configuration.username
        password = self.configuration.password

        return base64.b64encode(f'{username}:{password}'.encode('ascii')).decode()

    def get_headers(self, headers=None) -> dict:
        """
        Get default and additional HTTP headers
        """

        _headers = {
            'Accept': 'application/json',
            'Authorization': f'Basic {self.get_basic_auth_token()}'
        }

        if headers and isinstance(headers, dict):
            _headers = self._update_total_headers(headers, _headers)

        return _headers

    def response_from_api(self, response_obj=None, code=None, message='OK', content=None) -> dict:
        """
        Accepts the response from API and remake it to default representation
        """

        result = {
            'success': False,
            'code': code,
            'message': message,
            'content': content,
            'headers': None     # list of tuples if exists
        }

        if response_obj is not None:
            response_data = None

            result['code'] = response_obj.status
            result['headers'] = response_obj.headers.items()

            if 200 <= response_obj.status <= 299:
                result['success'] = True
                result['message'] = 'OK'

            if 300 <= response_obj.status <= 399:
                result['message'] = response_obj.reason
                return result

            try:
                response_data = json.loads(response_obj.read().decode('utf-8'))
            except json.decoder.JSONDecodeError as err:
                logger.debug(f'An error reading the response content occurred: {err}')

            result['content'] = response_data

        return result

    def get_request_body(self, body: dict) -> Union[bytes, dict]:
        """
        Get a valid payload for a request
        """

        try:
            payload = json.dumps(body).encode('utf-8')
        except ValueError as err:
            logger.debug(f'An error forming request json body occurred: {err}')
            return self.response_from_api(message=err.__str__())
        return payload

    def make_request(self, request_obj) -> dict:
        """
        Make a request to the API
        """

        if self.configuration.proxies:
            request_obj = self._set_proxies(request_obj)

        try:
            with urllib.request.urlopen(request_obj) as response:
                return self.response_from_api(response)
        except urllib.error.HTTPError as err:
            logger.debug(f'An HTTP error occurred: {err}')
            return self.response_from_api(err, message=err.reason)
        except urllib.error.URLError as err:
            logger.debug(f'An URL error occurred: {err}')
            return self.response_from_api(message=err.__str__())
        except ValueError as err:
            logger.debug(f'An error reading the response content occurred: {err}')
            return self.response_from_api(message=err.__str__())
        except Exception as err:
            logger.debug(f'An unknown error occurred: {err}')
            return self.response_from_api(message=err.__str__())
