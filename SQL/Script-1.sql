SELECT * FROM SALARIES LIMIT 10;

SELECT yearID FROM SALARIES LIMIT 10;
SELECT yearID, PLAYERID , salary FROM SALARIES LIMIT 10;

SELECT * FROM SALARIES  ORDER BY SALARY DESC LIMIT 20;
-- 주석

SELECT * FROM SALARIES WHERE yearid = '2010' ORDER BY SALARY DESC LIMIT 20;