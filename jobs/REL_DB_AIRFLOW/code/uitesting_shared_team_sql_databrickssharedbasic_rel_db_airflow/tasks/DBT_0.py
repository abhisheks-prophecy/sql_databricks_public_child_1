from uitesting_shared_team_sql_databrickssharedbasic_rel_db_airflow.utils import *

def DBT_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "DBT_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": True,
          "run_seeds": True,
          "run_parents": True,
          "run_children": False,
          "run_tests": False,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "74",
          "git_entity": "tag",
          "git_entity_value": "__PROJECT_FULL_RELEASE_TAG_PLACEHOLDER__",
          "git_ssh_url": "https://github.com/abhisheks-prophecy/sql_databricks_public_child_1",
          "git_sub_path": "",
          "select": "",
          "exclude": "",
          "run_props": " --profile run_profile --threads 1",
          "envs": {
            "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
            "DBT_PROFILES_DIR": "/home/airflow/gcs/data", 
            "DBT_PRINT": "false", 
            "DBT_FULL_REFRESH": "true"
          }
        },
        retry_exponential_backoff = True, 
        retries = 0
    )
