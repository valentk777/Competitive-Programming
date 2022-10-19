-- #-----------------------------------------------------------
-- # URL    : https://www.codewars.com/kata/594257d4db68b6e99200002c
-- # Notes  : tag-codewars, tag-kyu-6
-- #-----------------------------------------------------------

SELECT project, array_to_string(regexp_split_to_array(address, '\d'), '') 
    AS letters, array_to_string(regexp_split_to_array(address, '[^\d]'), '') 
    AS numbers 
FROM repositories;