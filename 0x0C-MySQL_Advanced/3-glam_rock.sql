-- Lists all bands with Glam rock as their main style, ranked by their longevity
-- (OLD code)
-- SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
-- (New Code --> Compliant with the  2024 constraint)
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
