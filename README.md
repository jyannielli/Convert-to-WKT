# Convert-to-WKT
Python module to convert latitude and longitude set to WKT format, suitable for the Coverage/Geometry field in Omeka/Neatline.

Requires the math and csv modules.

Used in conjunction with a geocoding API that generates a table in lat/long format. Outputs data in WKT.

For example, 	

41.307621, -72.9246216  -->  GEOMETRYCOLLECTION(POINT(-8117931.74167 5057822.12513))

I found these formulas online a while back, but I can't seem to locate the originals now. I am posting the full code here so others may benefit. If the original author(s) wish to assert a proprietary right to this code, please let me know!



