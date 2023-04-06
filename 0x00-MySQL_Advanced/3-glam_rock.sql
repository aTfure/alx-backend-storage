-- Lists all the bands with Glam rock as their main style
-- Ranked by their longetivity
-- Columns name must be: band_name and lifespan(years)
-- Should use attributes formed and split from computing lifespan

SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
