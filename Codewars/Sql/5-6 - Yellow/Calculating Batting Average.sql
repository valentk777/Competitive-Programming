-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/5994dafcbddc2f116d000024
-- # Notes  : tag-codewars, tag-kyu-6
-- #-----------------------------------------------------------

SELECT player_name, games, CAST(ROUND(hits*1.0 / at_bats, 3) AS varchar) AS batting_average 
FROM yankees
WHERE at_bats >= 100
ORDER BY batting_average DESC;