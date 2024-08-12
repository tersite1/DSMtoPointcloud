# 3D Mesh Generation from DSM Images

This project showcases the process of converting Digital Surface Model (DSM) data into high-quality 3D mesh and point cloud outputs. The DSM image used for this process, along with the generated outputs, are displayed below.

#### Updates 

* 1.0 VersionInitial Release '24.08.09
* 1.1 Version Zero Division Error Fixed, Empty Information Area is now filled with lowest Z level. '24.08.10
* 1.2 Version Now You can convert greyscale image, or RGB image to DSM '24.08.12

## Target DSM Image

This is the target DSM image that was used to create the 3D data:

![Target DSM Image](https://github.com/user-attachments/assets/8b74c7d0-3510-4385-8529-79c422b7c841)

## Outputs

Below are the results of the 3D data creation process:

### Point Cloud Created
![Point Cloud Created](https://github.com/user-attachments/assets/a84d837d-5890-49dd-bb5c-49c462a3ca74)


### Mesh Created
![Mesh Created](https://github.com/user-attachments/assets/02c29db7-323e-4c1e-aaea-0f6326adcb39)



### Object Created (OBJ)
![Object Created](https://github.com/tersite1/DSMtoPointcloud/blob/main/MeshCreated1.png?raw=true)
![Object Created](https://github.com/tersite1/DSMtoPointcloud/blob/main/MeshCreated2.png?raw=true)



## Features

- **DSM Image Processing**: Converts DSM images into point clouds.
- **3D Mesh Generation**: Creates 3D meshes using Poisson surface reconstruction.
- **Multi-format Export**: Outputs results in both `.ply` and `.obj` formats.
- **Height Adjustment**: Adjusts building heights to better match reality.

You can adjust Created 3D Object's height for purpose(Verical images etc..)

![height](https://github.com/tersite1/DSMtoPLY/blob/main/HeightSample.png?raw=true/.png)


## Usage

### Prerequisites

Ensure you have Python 3.x installed and the following libraries:

```bash
pip install numpy pillow open3d tqdm
```

### Running the Script

1. **Set Input and Output Paths**: Edit the script to set the correct file paths for your DSM image input and desired output locations.

2. **Run the Script**:

(if you need)
```bash
   pip install requirements.txt
```
   ```bash
   python main.py
```
3. **View the Results**: The script will generate point cloud and 3D mesh files in both `.ply` and `.obj` formats, which you can open with 3D visualization software like MeshLab, Blender, or Open3D.

### Example Command

```bash
python main.py --input /path/to/your/DSM_image.tif --output_ply /path/to/save/output.ply --output_obj /path/to/save/output.obj
```


## Adjustable Parameters

The script includes several adjustable parameters that can be tuned according to your specific needs:

### 1. **Height Scaling Factor**


- **Variable**: `height_scaling_factor`
- **Description**: Adjusts the height (z-values) of the DSM data to better reflect the real-world heights of buildings.
- **Default**: `1.5`
- **Example**: `height_scaling_factor = 2.0` will double the height of buildings.

- 

### 2. **Poisson Reconstruction Depth**

- **Variable**: `depth`
- **Description**: Controls the depth of the Poisson surface reconstruction. Higher values increase the level of detail.
- **Default**: `12`
- **Example**: `depth=10` for less detail, `depth=15` for more detail.

### 3. **Normal Estimation Parameters**

- **Variables**: `radius`, `max_nn`
- **Description**: Defines the search radius and the maximum number of nearest neighbors for normal estimation.
- **Defaults**: `radius=1.0`, `max_nn=30`
- **Example**: `radius=2.0`, `max_nn=50` for wider and more comprehensive normal estimation.

### 4. **Vertex Density Threshold**

- **Variable**: `density_threshold`
- **Description**: Controls the threshold for removing low-density vertices from the mesh. 
- **Default**: `0.01` (1% quantile)
- **Example**: `density_threshold = 0.05` will remove more vertices, creating a cleaner but potentially less detailed mesh.


## Contact

If you have any questions, suggestions, or issues, please feel free to reach out.

- **Email**: [itcouldbe0@yonsei.ac.kr](mailto:itcouldbe0@yonsei.ac.kr)

This project was created and maintained by **Jaden Jang**, a 4th-year undergraduate student in **Civil & Environmental Engineering** at Yonsei University.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


