-- a code  SQL script that ranks country origins of bands, ordered by the number
-- of (non-unique) fans
SELECT origin, SUM(fans) aS nb_fans FROM metal_bands
GROUP BY  origin
ORDER BY nb_fans DESC;
