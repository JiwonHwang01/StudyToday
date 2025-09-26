SELECT 
    H.HISTORY_ID,
    FLOOR(
        C.DAILY_FEE * (DATEDIFF(H.END_DATE, H.START_DATE) + 1) *
        (100 - IFNULL(
            CASE
                WHEN days >= 90 THEN (
                    SELECT DISCOUNT_RATE 
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '90일 이상'
                )
                WHEN days >= 30 THEN (
                    SELECT DISCOUNT_RATE 
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '30일 이상'
                )
                WHEN days >= 7 THEN (
                    SELECT DISCOUNT_RATE 
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '7일 이상'
                )
                ELSE 0
            END, 0)
        ) / 100
    ) AS FEE
FROM (
    SELECT HISTORY_ID, CAR_ID, START_DATE, END_DATE, 
           DATEDIFF(END_DATE, START_DATE) + 1 AS days
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) H
JOIN CAR_RENTAL_COMPANY_CAR C
  ON H.CAR_ID = C.CAR_ID
WHERE C.CAR_TYPE = '트럭'
ORDER BY FEE DESC, H.HISTORY_ID DESC;
