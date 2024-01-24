from urllib.request import Request
from airflow_python_api.api import ApiCore
from airflow_python_api.utils import request_body_validator, get_full_uri


class PostDAGRun(ApiCore):
    """
    Trigger a new DAG run
    https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html#operation/post_dag_run
    """

    def __init__(self, configuration, dag_id: str):
        super().__init__(configuration)
        self.dag_id = dag_id

    @request_body_validator
    def execute(self, data: dict):
        url = get_full_uri(
            self.configuration.host,
            ['dags', self.dag_id, 'dagRuns']
        )
        req = Request(
            url,
            headers=self.get_headers(
                {'Content-Type': 'application/json; charset=utf-8'}
            ),
            data=self.get_request_body(data),
            method='POST'
        )
        return self.make_request(req)


class GetDAGRun(ApiCore):
    """
    Get a DAG run
    https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html#operation/get_dag_run
    """

    def __init__(self, configuration, dag_id: str):
        super().__init__(configuration)
        self.dag_id = dag_id

    def execute(self, dag_run_id: str):
        url = get_full_uri(
            self.configuration.host,
            ['dags', self.dag_id, 'dagRuns', dag_run_id]
        )
        req = Request(url, headers=self.get_headers(), method='GET')
        return self.make_request(req)
