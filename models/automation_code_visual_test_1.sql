WITH all_type_partitioned AS (

  SELECT * 
  
  FROM {{ source('spark_catalog.qa_database', 'all_type_partitioned') }}

)

SELECT *

FROM all_type_partitioned
