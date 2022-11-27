-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
-- # Notes  : tag-codewars, tag-kyu-8
-- #-----------------------------------------------------------

SELECT 
  CASE 
    WHEN number % 2 = 0 THEN 'Even'
    ELSE 'Odd'
  END AS is_even 
FROM numbers;