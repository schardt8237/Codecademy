/*SELECT * FROM stream LIMIT 20;
SELECT * FROM chat LIMIT 20;
SELECT DISTINCT game FROM stream;
SELECT DISTINCT channel FROM stream;
SELECT game, COUNT(*) FROM stream GROUP BY 1 ORDER BY 2 DESC;
SELECT country, COUNT(*) FROM stream WHERE game = 'League of Legends' GROUP BY 1 ORDER BY 2 DESC;
SELECT player, COUNT(*) FROM stream GROUP BY 1 ORDER BY 2 DESC;
SELECT game, CASE
WHEN game = 'League of Legends' THEN 'MOBA'
WHEN game = 'Dota 2' THEN 'MOBA'
WHEN game = 'Heroes of the Storm' THEN 'MOBA'
WHEN game = 'Counter-Strike: Global' THEN 'FPS'
WHEN game = 'DayZ' THEN 'Survival'
WHEN game = 'Survival Evolved' THEN 'Survival'
ELSE 'Other'
END AS 'Genre', COUNT(*) As 'Viewers'
FROM stream
GROUP BY 1
ORDER BY 3 DESC;
SELECT time
FROM stream
LIMIT 10;
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;
SELECT strftime('%H', time) AS 'Hour', COUNT(*) AS 'Viewers' FROM stream
GROUP BY 1;*/
SELECT * FROM stream s JOIN chat c ON s.device_id = c.device_id;