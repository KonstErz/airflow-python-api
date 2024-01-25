from typing import List
from airflow_python_api.exceptions import ApiValidationError


def get_full_uri(base_path: str, uri_parts: List[str], endslash=False) -> str:
    """
    Returns full uri path from base path and sequences of uri parts;
    Endslash allows to finish '/' at the end of the uri path
    """

    base_path = base_path if base_path.endswith('/') else f'{base_path}/'
    full_uri = base_path
    last_part = str(uri_parts.pop(-1))
    for part in uri_parts:
        part = str(part).replace('/', '')
        full_uri += f'{part}/'
    full_uri += f"{last_part.replace('/', '')}"
    full_uri += '/' if endslash else ''
    return full_uri


def request_body_validator(func):
    """
    Decorator for validation of data availability in parameters, dict only
    """

    def _wrapper(*args, **kwargs):
        body = kwargs.get('data')
        if not body:
            for arg in args:
                if isinstance(arg, dict):
                    body = arg
                    break
        if not body or not isinstance(body, dict):
            raise ApiValidationError('dict with data for request body is required')
        return func(*args, **kwargs)
    return _wrapper
