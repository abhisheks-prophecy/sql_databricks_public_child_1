import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from dcomzbwlkncix34ykqcmsw_.tasks import (
    DBT_0_1,
    DBT_0_1_1,
    DBT_0_1_1_1,
    DBT_0_1_2,
    DBT_0_1_2_1,
    DBT_0_1_2_1_1,
    DBT_0_1_2_2,
    DBT_0_1_3,
    DBT_0_1_3_1,
    DBT_0_1_4,
    DBT_0_1_4_1,
    DBT_0_1_4_1_1,
    DBT_0_1_5
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "DcOmZBWlkNciX34YkqcMsw_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "hhFvJ5E5"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2033, 9, 23, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    DBT_0_1_4_op = DBT_0_1_4()
    DBT_0_1_3_op = DBT_0_1_3()
    DBT_0_1_3_1_op = DBT_0_1_3_1()
    DBT_0_1_op = DBT_0_1()
    DBT_0_1_1_op = DBT_0_1_1()
    DBT_0_1_5_op = DBT_0_1_5()
    DBT_0_1_1_1_op = DBT_0_1_1_1()
    DBT_0_1_2_op = DBT_0_1_2()
    DBT_0_1_4_1_op = DBT_0_1_4_1()
    DBT_0_1_2_1_op = DBT_0_1_2_1()
    DBT_0_1_2_2_op = DBT_0_1_2_2()
    DBT_0_1_4_1_1_op = DBT_0_1_4_1_1()
    DBT_0_1_2_1_1_op = DBT_0_1_2_1_1()
    DBT_0_1_4_1_1_op >> DBT_0_1_2_1_1_op
    DBT_0_1_2_2_op >> DBT_0_1_4_1_1_op
    DBT_0_1_3_op >> DBT_0_1_3_1_op
    DBT_0_1_4_1_op >> DBT_0_1_2_1_op
    DBT_0_1_4_op >> DBT_0_1_3_op
    DBT_0_1_3_1_op >> DBT_0_1_op
    DBT_0_1_op >> DBT_0_1_1_op
    DBT_0_1_2_op >> DBT_0_1_4_1_op
    DBT_0_1_1_1_op >> DBT_0_1_2_op
    DBT_0_1_5_op >> DBT_0_1_1_1_op
    DBT_0_1_2_1_op >> DBT_0_1_2_2_op
    DBT_0_1_1_op >> DBT_0_1_5_op
