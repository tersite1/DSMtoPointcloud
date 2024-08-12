import numpy as np
from PIL import Image
import open3d as o3d
from tqdm import tqdm

# Output paths: Set the paths for saving the results
output_ply_path = 'Your_path/output.ply'  # Path for the point cloud PLY file
output_mesh_ply_path = 'Your_path/mesh_output.ply'  # Path for the high-quality mesh PLY file
output_mesh_obj_path = 'Your_path/mesh_output.obj'  # Path for the high-quality mesh OBJ file

 Scaling factor for building heights
height_scaling_factor = 1.5  # Adjust this value based on your specific needs

# Display progress bar for DSM Image Load
print("Loading DSM Image...")
with tqdm(total=100, desc="Progress", ncols=100) as pbar:
    dsm_image = Image.open('/yourimage.tif')
    dsm_array = np.array(dsm_image)
    pbar.update(20)  # 20% completed

# Check if the DSM array is empty or not
if dsm_array.size == 0:
    raise ValueError("DSM image data is empty. Please check the input file.")

# Apply scaling factor to z-values
print(f"Applying height scaling factor of {height_scaling_factor}...")
z = dsm_array.flatten() * height_scaling_factor  # Scale the height values

# Create Ply using vectorized numpy operations: Generate point cloud using vectorized operations
print("Creating Point Cloud...")
h, w = dsm_array.shape  # Get the height and width of the DSM image
x, y = np.meshgrid(np.arange(w), np.arange(h))  # Create a grid of x and y coordinates
points = np.vstack((x.flatten(), y.flatten(), z)).T  # Combine x, y, z coordinates into a single array to form points
pbar.update(20)  # 40% completed

# PointCloud Object Creation: Create a point cloud object using Open3D
print("Creating PointCloud Object...")
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)  # Set the coordinates in the point cloud
pbar.update(20)  # 60% completed

# **Normal Estimation**: Estimate normals for the point cloud
print("Estimating Normals...")
point_cloud.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=1.0, max_nn=30))
pbar.update(10)  # 70% completed

# **Remove Outliers**
print("Removing Outliers...")
cl, ind = point_cloud.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
point_cloud = point_cloud.select_by_index(ind)

# Option 1: Perform Poisson Surface Reconstruction with adjusted parameters
# print("Performing Poisson Surface Reconstruction...")
# mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(point_cloud, depth=6, scale=1.0)
# pbar.update(10)  # 80% completed

# Option 2: Perform Ball Pivoting Algorithm (BPA)
print("Performing Ball Pivoting Algorithm...")
radii = [0.5, 1.0, 2.0]  # Adjust these radii based on your data
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
    point_cloud, o3d.utility.DoubleVector(radii)
)
pbar.update(10)  # 80% completed

# Refine and Save the mesh
print("Saving Mesh and Point Cloud...")
o3d.io.write_triangle_mesh(output_mesh_ply_path, mesh)  # Save as PLY
o3d.io.write_triangle_mesh(output_mesh_obj_path, mesh)  # Save as OBJ
o3d.io.write_point_cloud(output_ply_path, point_cloud)  # Save the original point cloud to a PLY file
pbar.update(10)  # 100% completed

print("Process Completed.")
