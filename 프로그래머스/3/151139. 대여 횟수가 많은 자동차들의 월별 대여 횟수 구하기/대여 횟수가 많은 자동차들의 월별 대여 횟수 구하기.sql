SELECT
    MONTH(START_DATE) MONTH,
    CAR_ID,
    COUNT(*) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    AND CAR_ID IN 
    ( SELECT CAR_ID
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
      GROUP BY CAR_ID
      HAVING COUNT(CAR_ID) >= 5
    )
GROUP BY 2, 1
HAVING RECORDS >= 1
ORDER BY 1 ASC, CAR_ID DESC;