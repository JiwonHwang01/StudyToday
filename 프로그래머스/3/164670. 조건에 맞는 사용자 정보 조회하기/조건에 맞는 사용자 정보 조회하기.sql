-- 코드를 입력하세요
WITH B AS (
    SELECT WRITER_ID, COUNT(*) AS CNT
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
)

SELECT USER_ID,NICKNAME,CONCAT(CITY, " ",STREET_ADDRESS1, " ", STREET_ADDRESS2) AS "전체주소",CONCAT(SUBSTR(TLNO,1,3),"-",SUBSTR(TLNO,4,4),"-",SUBSTR(TLNO,8,4)) AS "전화번호"
FROM B
INNER JOIN USED_GOODS_USER AS U
ON B.WRITER_ID = U.USER_ID
WHERE B.CNT >= 3
ORDER BY B.WRITER_ID DESC
