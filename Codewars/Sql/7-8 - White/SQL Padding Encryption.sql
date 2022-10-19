-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/5943b797d8c9432eb7000066
-- # Notes  : tag-codewars, tag-kyu-7
-- #-----------------------------------------------------------

SELECT 
  CONCAT(md5, REPEAT('1', char_length(sha256) - char_length(md5))) AS md5, 
  CONCAT(REPEAT('0', char_length(sha256) - char_length(sha1)), sha1) AS sha1, 
  sha256
FROM encryption