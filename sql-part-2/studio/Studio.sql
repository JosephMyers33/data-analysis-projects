SELECT 
    ROUND(AVG(A.value), 2) AS AvgEarnings, 
    2016 AS Year,
    'Annual' AS Period
FROM 
    LaborStatisticsDB.dbo.annual_2016 AS A
JOIN 
    LaborStatisticsDB.dbo.series AS S ON A.series_id = S.series_id
WHERE 
    S.data_type_code = 30

UNION

SELECT 
    ROUND(AVG(J.value), 2) AS AvgEarnings, 
    2017 AS Year,
    'January' AS Period
FROM 
    LaborStatisticsDB.dbo.january_2017 AS J
JOIN 
    LaborStatisticsDB.dbo.series AS S ON J.series_id = S.series_id
WHERE 
    S.data_type_code = 30;