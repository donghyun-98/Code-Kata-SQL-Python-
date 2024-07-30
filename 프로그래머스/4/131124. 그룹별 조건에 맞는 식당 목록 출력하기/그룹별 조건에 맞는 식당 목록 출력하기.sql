SELECT
    mr.MEMBER_NAME,
    rr.REVIEW_TEXT,
    DATE_FORMAT(rr.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM MEMBER_PROFILE mr
    INNER JOIN REST_REVIEW rr
    ON mr.MEMBER_ID = rr.MEMBER_ID
WHERE rr.MEMBER_ID = ( SELECT MEMBER_ID
                       FROM REST_REVIEW
                       GROUP BY 1
                       ORDER BY COUNT(*) DESC
                       LIMIT 1)
ORDER BY 3 ASC, 2 ASC;

