-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/593ef0e98b90525e090000b9
-- # Notes  : tag-codewars, tag-kyu-6
-- #-----------------------------------------------------------

SELECT th.id, th.heads, bh.legs, th.arms, bh.tails, 
  CASE 
    WHEN th.heads > th.arms THEN 'BEAST'
    WHEN bh.tails > bh.legs THEN 'BEAST'
    ELSE 'WEIRDO'
  END AS species
FROM top_half th, bottom_half bh
WHERE th.id = bh.id
ORDER BY species
