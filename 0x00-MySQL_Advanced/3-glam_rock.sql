-- performing calculation of lifespan to rank bands with a particular style

SELECT band_name, (split - formed) AS lifespan FROM metal_bands WHERE style='Glam rock' ORDER BY lifespan DESC LIMIT 20;
