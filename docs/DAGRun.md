# airflow_python_api.DAGRun

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dag_run**](DAGRun.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
[**post_dag_run**](DAGRun.md#post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run


# **get_dag_run**

Get a DAG run (see https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html#operation/get_dag_run)

### Example

```python
import airflow_python_api
from airflow_python_api.api.dag_runs import GetDAGRun

# Defining the host and configure required parameters for HTTP basic authorization
configuration = airflow_python_api.Configuration(
    host='https://localhost/api/v1',
    username='your_username',
    password='your_password'
)

# Create an instance of the API class
get_dag_run = GetDAGRun(configuration=configuration, dag_id='example_dag')

# Get response with data about a specific DAGRun
response = get_dag_run.execute(dag_run_id='test_init_dagrun_123')
print(response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **dag_run_id** | **str**| The DAG run ID. |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **post_dag_run**

Trigger a new DAG run (see https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html#operation/post_dag_run)

### Example

```python
import airflow_python_api
from airflow_python_api.api.dag_runs import PostDAGRun

# Defining the host and configure required parameters for HTTP basic authorization
configuration = airflow_python_api.Configuration(
    host='https://localhost/api/v1',
    username='your_username',
    password='your_password'
)

# Create an instance of the API class
post_dag_run = PostDAGRun(configuration=configuration, dag_id='example_dag')

# Set the required payload for your request
data = {
    'dag_run_id': 'test_init_dagrun_123', # recommended to specified
    'logical_date': '2024-01-30T14:15:22Z',
    'note': 'Test init dagrun',
    'conf': {}
}

# Sending a request to initiate a new DAGRun
response = post_dag_run.execute(data=data)
print(response)
```

### Parameters

Name | Type     | Description  | Notes
------------- |----------| ------------- | -------------
 **dag_id** | **str**  | The DAG ID. |
 **data** | **dict** | Payload of request |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

