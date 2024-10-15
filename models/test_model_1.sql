WITH very_complex_table AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.qa_database', 'very_complex_table') }}

),

distinct_asthma_medications AS (

  {#Identifies unique classes of asthma medications for better treatment options.#}
  SELECT DISTINCT `c_complex-array`.Asthma.medications.medicationsClasses.className_1.`associated-Drug`
  
  FROM very_complex_table AS in0

)

SELECT *

FROM distinct_asthma_medications
