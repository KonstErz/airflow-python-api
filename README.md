# airflow-python-api

## Overview

Python package for interacting with [Airflow API (Stable)](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html)

## Requirements.

Python >= 3.6

Your version of the `apache-airflow` must be at least `2.6.3`

## Installation & Usage
### pip install

installing from github repo:

```sh
pip install ...
```

Then import the package:
```python
import airflow_python_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import airflow_python_api
```

## Getting Started

Example code for getting DAGRun data:

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

### Response example

Client returns the response from the Airflow API in the following default **python dict** format:

```python
{
  'success': True, 
  'code': 200, # HTTP Response status code if request reaches the API server
  'message': 'OK', # HTTP Response reason or error description
    # HTTP Response payload
  'content': {
    'conf': {}, 
    'dag_id': 'example_dag', 
    'dag_run_id': 'test_init_dagrun_123', 
    'data_interval_end': '2024-01-20T10:13:05.300848+00:00', 
    'data_interval_start': '2024-01-20T10:13:05.300848+00:00', 
    'end_date': '2024-01-20T10:13:50.473629+00:00', 
    'execution_date': '2024-01-20T10:13:05.300848+00:00', 
    'external_trigger': True, 
    'last_scheduling_decision': '2024-01-20T10:13:50.470070+00:00', 
    'logical_date': '2024-01-20T10:13:05.300848+00:00', 
    'note': None, 
    'run_type': 'manual', 
    'start_date': '2024-01-20T10:13:05.865698+00:00', 
    'state': 'success'
  }, 
    # HTTP Response headers if request reaches the API server
  'headers': [
    ('Server', 'nginx'), 
    ('Date', 'Wed, 24 Jan 2024 12:37:51 GMT'), 
    ('Content-Type', 'application/json'), 
    ('Content-Length', '714'), 
    ('Connection', 'close'), 
    ('X-Robots-Tag', 'noindex, nofollow')
  ]
}
```

## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DAGRun* | [**get_dag_run**](docs/DAGRun.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
*DAGRun* | [**post_dag_run**](docs/DAGRun.md#post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author

konstantin.yerzin@gmail.com

