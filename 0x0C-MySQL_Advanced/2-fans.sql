-- Ranks country origins of bands, ordered by the number of (non-unique) fans.
SELECT SUM(fans) AS nb_fans, origin FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
