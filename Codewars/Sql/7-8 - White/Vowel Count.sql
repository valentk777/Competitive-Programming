-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/54ff3102c1bad923760001f3
-- # Notes  : tag-codewars, tag-kyu-7
-- #-----------------------------------------------------------

SELECT str, LENGTH(REGEXP_REPLACE(str, '[^aeiou]', '', 'g')) AS res
FROM getcount;

-- another solution
SELECT str, LENGTH(str) - LENGTH(TRANSLATE(str,'aeiou','')) AS res
FROM getcount;