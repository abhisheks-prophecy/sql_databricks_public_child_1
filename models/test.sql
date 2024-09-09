WITH country_classification AS (

  SELECT * 
  
  FROM {{ ref('country_classification')}}

),

Reformat_1 AS (

  SELECT * 
  
  FROM country_classification AS in0

)

SELECT *

FROM Reformat_1
