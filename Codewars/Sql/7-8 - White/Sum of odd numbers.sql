-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
-- # Notes  : tag-codewars, tag-kyu-7
-- #-----------------------------------------------------------

SELECT 
  (
    SELECT sum(x)
    FROM generate_series((n-1)*n+1, n*(n+1)-1, 2) AS x
  ) AS res
FROM nums;

-- ANOTHER SOLUTION
SELECT n * n * n AS res 
FROM nums;