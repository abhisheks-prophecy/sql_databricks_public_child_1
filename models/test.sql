

{% set c_test_string = 'test_string' %}
{% set c_test_int = 11 %}

WITH all_type_non_partitioned AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.qa_db_warehouse', 'all_type_non_partitioned') }}

),

distinct_all_types AS (

  {#Extracts unique combinations of tiny integer values and concatenated integer-string pairs.#}
  SELECT 
    DISTINCT c_tinyint,
    concat(c_int, c_string) AS c_int_string
  
  FROM all_type_non_partitioned AS in0

),

unique_tinyint_records AS (

  {#Identifies unique records based on a specific small integer value.#}
  SELECT * 
  
  FROM distinct_all_types AS in0
  
  QUALIFY COUNT(*) OVER (PARTITION BY c_tinyint) = 1

),

distinct_rows_by_partition AS (

  {#Identifies unique entries based on city, state, and a boolean flag, prioritizing specific numeric values.#}
  SELECT * 
  
  FROM all_type_non_partitioned AS in0
  
  QUALIFY ROW_NUMBER() OVER (PARTITION BY concat(c_struct.city, c_struct.state), c_boolean ORDER BY c_int ASC, c_bigint DESC) = 1

),

distinct_rows_by_partition_1 AS (

  {#Identifies unique entries based on specific city and state attributes, ensuring data integrity.#}
  SELECT * 
  
  FROM all_type_non_partitioned AS in0
  
  QUALIFY ROW_NUMBER() OVER (PARTITION BY c_struct.city, c_boolean, c_struct.state, c_struct.pin ORDER BY c_int ASC, c_bigint DESC) = COUNT(*) OVER (PARTITION BY c_struct.city, c_boolean, c_struct.state, c_struct.pin)

),

joined_records AS (

  {#Combines various unique records to create a comprehensive dataset for analysis.#}
  SELECT 
    in0.c_tinyint AS c_tinyint,
    in0.c_int_string AS c_int_string,
    in1.c_bigint AS c_bigint,
    in1.c_array AS c_array,
    in2.c_struct AS c_struct,
    in2.c_string AS c_string,
    in2.c_double AS c_double
  
  FROM unique_tinyint_records AS in0
  INNER JOIN distinct_rows_by_partition AS in1
     ON in0.c_tinyint != in1.c_tinyint
  INNER JOIN distinct_rows_by_partition_1 AS in2
     ON in1.c_tinyint != in2.c_smallint

)

SELECT *

FROM Reformat_1
