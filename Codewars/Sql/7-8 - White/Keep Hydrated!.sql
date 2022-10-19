-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/582cb0224e56e068d800003c
-- # Notes  : tag-codewars, tag-kyu-8
-- #-----------------------------------------------------------

SELECT *,
CASE
  WHEN hours > 0 THEN FLOOR(hours * 0.5) 
END AS liters
FROM cycling;