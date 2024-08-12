
import cv2
import numpy as np
from osgeo import gdal

gdal.UseExceptions()


# Step 1: Load the DEM image (grayscale or RGB)
dem_image = cv2.imread('/Users/Caz/Desktop/tar2.jpg')

# Check if the image is grayscale or RGB
if len(dem_image.shape) == 2:  # Grayscale image
    is_grayscale = True
    dem_array = dem_image.astype(np.float32)
else:  # RGB image
    is_grayscale = False
    dem_image = cv2.cvtColor(dem_image, cv2.COLOR_BGR2RGB)  # Convert to RGB if it's not already

# Step 2: Initialize an empty array for the DSM values (if not grayscale)
if not is_grayscale:
    height, width, _ = dem_image.shape
    dsm_array = np.zeros((height, width), dtype=np.float32)

    # Define a function to map RGB to elevation
    def rgb_to_elevation(rgb):
        r, g, b = rgb
        # Convert RGB to grayscale equivalent (simple linear mapping example)
        elevation = (0.2989 * r + 0.5870 * g + 0.1140 * b)  # Modify based on your specific mapping
        return elevation

    # Map each pixel color to an elevation value
    for y in range(height):
        for x in range(width):
            pixel_color = tuple(dem_image[y, x])
            dsm_array[y, x] = rgb_to_elevation(pixel_color)
else:
    dsm_array = dem_array

# Step 3: Save the DSM as a GeoTIFF
height, width = dsm_array.shape
driver = gdal.GetDriverByName('GTiff')
out_tif = driver.Create('/Users/Caz/Desktop/output_dsm.tif', width, height, 1, gdal.GDT_Float32)
out_tif.GetRasterBand(1).WriteArray(dsm_array)

# Set GeoTransform and Projection (optional)
out_tif.FlushCache()  # Ensure all data is written to disk
out_tif = None  # Close the file
