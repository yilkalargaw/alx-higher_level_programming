--  list the number of records with the same score in  table second_table
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
