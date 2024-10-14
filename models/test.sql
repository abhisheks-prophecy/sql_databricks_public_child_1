

{% set c_test_string = 'test_string' %}
{% set c_test_int = 11 %}

WITH all_type_non_partitioned AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.qa_db_warehouse', 'all_type_non_partitioned') }}

)

SELECT *

FROM all_type_non_partitioned
