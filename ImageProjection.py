import open3d as o3d
import numpy as np
from PIL import Image

# 1. Load the PLY file
ply_file_path = "input.ply"
pcd = o3d.io.read_point_cloud(ply_file_path)
points = np.asarray(pcd.points)

# 2. Load the aerial image
image_path = "aerial_image.jpg"
image = Image.open(image_path)

# 2-1. Rotate the image 90 degrees counterclockwise
image = image.rotate(90, expand=True)

# 3. Calculate the x, y range of the PLY file
x_min, y_min = points[:, 0].min(), points[:, 1].min()
x_max, y_max = points[:, 0].max(), points[:, 1].max()

# 4. Resize the image to fit the point cloud's x, y range
width, height = image.size
x_range = x_max - x_min
y_range = y_max - y_min
aspect_ratio = width / height

# Adjust the image size based on the aspect ratio
if x_range / y_range > aspect_ratio:
    new_width = int(x_range)
    new_height = int(new_width / aspect_ratio)
else:
    new_height = int(y_range)
    new_width = int(new_height * aspect_ratio)

resized_image = image.resize((new_width, new_height))
resized_image_np = np.array(resized_image)

# 5. Convert the point's x, y coordinates to the image's pixel coordinates
def point_to_pixel(x, y, x_min, y_min, x_range, y_range, image_width, image_height):
    px = int((x - x_min) / x_range * (image_width - 1))
    py = int((y - y_min) / y_range * (image_height - 1))
    # Flip the y-axis since image y-axis is inverted
    py = image_height - 1 - py
    return px, py

# 6. Extract color from the image for each point
colors = []
for point in points:
    px, py = point_to_pixel(point[0], point[1], x_min, y_min, x_range, y_range, new_width, new_height)
    color = resized_image_np[py, px] / 255.0  # Normalize color to [0, 1] range
    colors.append(color)

# 7. Assign colors to the point cloud
pcd.colors = o3d.utility.Vector3dVector(colors)

# 8. Save the colored PLY file
output_ply_path = "output_colored.ply"
o3d.io.write_point_cloud(output_ply_path, pcd)

print(f"Colored PLY file saved at {output_ply_path}.")
