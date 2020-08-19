# 2D-Voxel-image

For voxel-image generation, we used `python==3.6`. You also need csv of pdb_ids for the same. For e.g. I have used here `pdb_ids.csv` file
To get voxel images, follow the following steps:

* First clone this repository
```bash
git clone https://github.com/p1halani/2D-Voxel-image.git
```

* Create conda environment
```bash
conda create --name ml pip
conda activate ml
```

* Install Enzynet library
```bash
git clone https://github.com/shervinea/enzynet.git
cd enzynet
pip3 install -r requirements.txt
pip3 install -e .
```

* Make output directory for voxel images
```bash
mkdir Voxel_output
mkdir Voxel_output/charge
mkdir Voxel_output/hydropathy
mkdir Voxel_output/isoelectric
mkdir Voxel_output/None
```

* Replacement of visualization file with our file.
```bash
cp ../2D-Voxel-image/visualization.py enzynet/
```

* Replace `{version}` with the actual version of python in `ml` environment and also replace path to `ml` conda environment. For me the command was : `cp ../2D-Voxel-image/axes3d.py /home/parth/anaconda3/envs/JBHI/lib/python3.6/site-packages/mpl_toolkits/mplot3d/`
```bash
cp ../2D-Voxel-image/axes3d.py /path/to/conda/environment/lib/python{version}/site-packages/mpl_toolkits/mplot3d/
```

* Run the code to get voxel images as output in `Voxel_output` folder
```python
python -m enzynet/visualization
```