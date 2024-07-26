SELECT 
    a.AUTHOR_ID,
    a.AUTHOR_NAME,
    b.CATEGORY,
    SUM(bs.SALES*b.PRICE) TOTAL_SALES
FROM 
    BOOK b
    INNER JOIN AUTHOR a
    ON b.AUTHOR_ID = a.AUTHOR_ID
    JOIN BOOK_SALES bs
    ON b.BOOK_ID = bs.BOOK_ID
    WHERE bs.SALES_DATE LIKE '2022-01%'
GROUP BY 1, 3 
ORDER BY 1 ASC, 3 DESC;