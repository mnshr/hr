# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 16:52:21 2017

@author: mnshr
"""

--https://www.hackerrank.com/challenges/revising-the-select-query
SELECT * 
FROM CITY
WHERE COUNTRYCODE='USA'
AND POPULATION>100000;

--https://www.hackerrank.com/challenges/revising-the-select-query-2
SELECT NAME
FROM CITY
WHERE COUNTRYCODE='USA'
AND POPULATION>120000;

--https://www.hackerrank.com/challenges/select-all-sql
SELECT * 
FROM CITY;

--https://www.hackerrank.com/challenges/select-by-id
SELECT * FROM CITY
WHERE ID=1661;

--https://www.hackerrank.com/challenges/japanese-cities-attributes
SELECT * 
FROM CITY
WHERE COUNTRYCODE='JPN';

--https://www.hackerrank.com/challenges/japanese-cities-name
SELECT NAME 
FROM CITY
WHERE COUNTRYCODE='JPN';

--https://www.hackerrank.com/challenges/weather-observation-station-1
SELECT CITY, STATE
FROM STATION;

--https://www.hackerrank.com/challenges/weather-observation-station-3
SELECT DISTINCT(CITY)
FROM STATION
WHERE mod(ID, 2)=0;
         
--https://www.hackerrank.com/challenges/weather-observation-station-4
SELECT COUNT(CITY)-COUNT(DISTINCT(CITY))
FROM STATION;

--https://www.hackerrank.com/challenges/weather-observation-station-5

SELECT city, LENGTH(city)
FROM station
ORDER BY LENGTH(city), CITY
LIMIT 1;

SELECT city, LENGTH(city)
FROM station
ORDER BY LENGTH(city) DESC, CITY
LIMIT 1;

--https://www.hackerrank.com/challenges/weather-observation-station-6
SELECT CITY
FROM STATION
WHERE LEFT(LOWER(CITY),1) IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/weather-observation-station-7
SELECT CITY
FROM STATION
WHERE RIGHT(LOWER(CITY),1) IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/weather-observation-station-8
SELECT CITY
FROM STATION
WHERE LEFT(LOWER(CITY),1) IN ('a','e','i','o','u')
AND RIGHT(LOWER(CITY),1) IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/weather-observation-station-9
SELECT CITY
FROM STATION
WHERE LEFT(LOWER(CITY),1) NOT IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/weather-observation-station-10
SELECT CITY
FROM STATION
WHERE RIGHT(LOWER(CITY),1) NOT IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/weather-observation-station-11
SELECT CITY
FROM STATION
WHERE LEFT(LOWER(CITY),1) NOT IN ('a','e','i','o','u')
OR RIGHT(LOWER(CITY),1) NOT IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/weather-observation-station-12
SELECT CITY
FROM STATION
WHERE LEFT(LOWER(CITY),1) NOT IN ('a','e','i','o','u')
AND RIGHT(LOWER(CITY),1) NOT IN ('a','e','i','o','u')
GROUP BY 1;

--https://www.hackerrank.com/challenges/more-than-75-marks
SELECT NAME
FROM STUDENTS
WHERE MARKS>75
ORDER BY RIGHT(NAME,3), ID;
              
--https://www.hackerrank.com/challenges/name-of-employees
SELECT NAME
FROM EMPLOYEE
ORDER BY NAME;

--https://www.hackerrank.com/challenges/salary-of-employees
SELECT NAME
FROM EMPLOYEE
WHERE SALARY>2000
AND MONTHS < 10
ORDER BY EMPLOYEE_ID;
-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
--https://www.hackerrank.com/challenges/what-type-of-triangle
SELECT
CASE 
    WHEN (B+C)>A AND (A+B)>C AND (A+C)>B THEN
    CASE
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN A=B OR B=C OR A=C THEN 'Isosceles'
        ELSE 'Scalene'
    END
    ELSE 'Not A Triangle'
END AS ABC
FROM TRIANGLES;

--https://www.hackerrank.com/challenges/the-pads
SELECT CONCAT(NAME, '(',LEFT(OCCUPATION,1),')')
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT('There are total ', B, ' ', A, 's.')
FROM
(SELECT LOWER(OCCUPATION) A, COUNT(NAME) B
FROM OCCUPATIONS
GROUP BY 1) TBL
ORDER BY B,A;

--https://www.hackerrank.com/challenges/occupations
--ORACLE SOL
SELECT D_N, P_N, S_N, A_N FROM
(
  select row_number() over (partition by occupation order by name) rnm, name, occupation 
  from occupations
)
PIVOT
(
  max(name) N
  FOR occupation IN ('Doctor' D, 'Professor' P, 'Singer' S, 'Actor' as A)
)
ORDER BY rnm;

--MYSQL
SELECT
   MIN(o.Doctor),MIN(o.Professor),MIN(o.Singer),MIN(o.Actor)
FROM
    (SELECT
        CASE WHEN occupation='Doctor' THEN @d:=@d+1
             WHEN occupation='Professor' THEN @p:=@p+1
             WHEN occupation='Singer' THEN @s:=@s+1
             WHEN occupation='Actor' THEN @a:=@a+1 END AS row,
        CASE WHEN occupation='Doctor' THEN name END AS Doctor,
        CASE WHEN occupation='Professor' THEN name END AS Professor,
        CASE WHEN occupation='Singer' THEN name END AS Singer,
        CASE WHEN occupation='Actor' THEN name END AS Actor
     FROM occupations JOIN (SELECT @d:=0, @p:=0, @s:=0,@a:=0) AS r 
     ORDER BY name) o
GROUP BY row;

--https://www.hackerrank.com/challenges/binary-search-tree-1
SELECT b.N, CASE
            WHEN b.P IS NULL
                THEN 'Root'
            ELSE CASE
                    WHEN (SELECT COUNT(*) FROM BST WHERE P=b.N)>0
                        THEN 'Inner'
                    ELSE 'Leaf'
                    END
            END
FROM BST AS b
ORDER BY b.N;

--https://www.hackerrank.com/challenges/the-company
SELECT A.COMPANY_CODE, A.FOUNDER, B.CLM, C.CSM, D.CM, E.CE
FROM COMPANY A
JOIN (SELECT COMPANY_CODE, COUNT(DISTINCT LEAD_MANAGER_CODE) CLM
     FROM LEAD_MANAGER
     GROUP BY 1) B
ON A.COMPANY_CODE=B.COMPANY_CODE
JOIN (SELECT COMPANY_CODE, COUNT(DISTINCT SENIOR_MANAGER_CODE) CSM
     FROM SENIOR_MANAGER
     GROUP BY 1) C
ON A.COMPANY_CODE=C.COMPANY_CODE
JOIN (SELECT COMPANY_CODE, COUNT(DISTINCT MANAGER_CODE) CM
     FROM MANAGER
     GROUP BY 1) D
ON A.COMPANY_CODE=D.COMPANY_CODE
JOIN (SELECT COMPANY_CODE, COUNT(DISTINCT EMPLOYEE_CODE) CE
     FROM EMPLOYEE
     GROUP BY 1) E
ON A.COMPANY_CODE=E.COMPANY_CODE
ORDER BY COMPANY_CODE;
-----------------------------------------------------------------------
----------------------------JOINS--------------------------------------
-----------------------------------------------------------------------
--https://www.hackerrank.com/challenges/asian-population
SELECT SUM(A.POPULATION)
FROM CITY A
JOIN COUNTRY B
ON A.COUNTRYCODE=B.CODE
WHERE B.CONTINENT='ASIA';

--https://www.hackerrank.com/challenges/african-cities
SELECT A.NAME
FROM CITY A
JOIN COUNTRY B
ON A.COUNTRYCODE=B.CODE
WHERE B.CONTINENT='Africa';

--https://www.hackerrank.com/challenges/average-population-of-each-continent
SELECT B.CONTINENT, FLOOR(SUM(A.POPULATION)/COUNT(A.ID))
FROM CITY A
JOIN COUNTRY B
ON A.COUNTRYCODE=B.CODE
GROUP BY 1;

--https://www.hackerrank.com/challenges/the-report
SELECT
    CASE WHEN GRADE>7 THEN NAME
    ELSE NULL
    END AS NM, GRADE, MARKS 
FROM (
SELECT A.NAME, B.GRADE, A.MARKS
FROM STUDENTS A
JOIN GRADES B
ON A.MARKS BETWEEN B.MIN_MARK AND B.MAX_MARK) TBL
ORDER BY GRADE DESC, NM, MARKS

--https://www.hackerrank.com/challenges/full-score
SELECT S.HACKER_ID, H.NAME
FROM SUBMISSIONS S, CHALLENGES C, HACKERS H, DIFFICULTY D
WHERE S.CHALLENGE_ID=C.CHALLENGE_ID
AND S.HACKER_ID=H.HACKER_ID
AND C.DIFFICULTY_LEVEL=D.DIFFICULTY_LEVEL
AND D.SCORE=S.SCORE
GROUP BY 1, 2
HAVING COUNT(S.SCORE)>1
ORDER BY COUNT(S.SCORE) DESC, S.HACKER_ID
              
--https://www.hackerrank.com/challenges/harry-potter-and-wands
SELECT W.id, WP.age, W.coins_needed, W.power
FROM WANDS W, WANDS_PROPERTY WP
WHERE W.CODE = WP.CODE
AND IS_EVIL=0
and W.COINS_NEEDED = (SELECT MIN(COINS_NEEDED) from WANDS as W1
                      JOIN WANDS_PROPERTY AS WP1
                      on (W1.CODE = WP1.CODE) 
                      WHERE W.POWER = W1.POWER
                      and WP1.AGE = WP.AGE)
ORDER BY POWER DESC, AGE DESC;

--https://www.hackerrank.com/challenges/challenges
select b.hacker_id, a.name, b.tot_cha 
from hackers a 
join (select hacker_id, count(challenge_id) as tot_cha 
      from challenges 
      group by hacker_id) b 
      on a.hacker_id = b.hacker_id 
      where b.tot_cha not in 
(select c.tot_cha 
 from 
 (select hacker_id, count(challenge_id) as tot_cha 
  from challenges 
  group by hacker_id) c 
 where c.tot_cha != 
 (select count(challenge_id) as tot_cha 
  from challenges 
  group by hacker_id 
  order by tot_cha desc limit 1) 
 group by c.tot_cha 
 having count(c.tot_cha) > 1) 
order by b.tot_cha desc, b.hacker_id;

--https://www.hackerrank.com/challenges/contest-leaderboard
SELECT A.HACKER_ID, B.NAME, SUM(SCOR)
FROM (
SELECT HACKER_ID, CHALLENGE_ID, MAX(SCORE) AS SCOR
FROM SUBMISSIONS
GROUP BY 1, 2
ORDER BY 1, 2, 3 DESC) AS A
JOIN HACKERS B
ON A.HACKER_ID=B.HACKER_ID
GROUP BY 1, 2
HAVING SUM(SCOR) > 0
ORDER BY SUM(SCOR) DESC, HACKER_ID
;

