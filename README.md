# MSRS: Multi-Spectral Road Scenarios for Practical Infrared and Visible Image Fusion 

We construct a new multi-spectral dataset for infrared and visible image fusion based on the **[MFNet](https://www.mi.t.u-tokyo.ac.jp/static/projects/mil_multispectral/)** dataset. The MFNet dataset contains 1,569 image pairs (820 taken at the daytime and 749 taken at nighttime) with spatial resolution is 480 × 640. However, There are many misaligned image pairs in the MFNet dataset and most infrared images are low signal-to-noise and low contrast. To this end, we first collect 715 daytime image pairs and 729 nighttime image pairs via removing 125 misaligned image pairs. Moreover, an image enhancement algorithm based on dark channel prior is leveraged to optimize the contrast and signal-to-noise of infrared images. As a result, the released new Multi-Spectral Road Scenarios (**MSRS**) dataset contains 1,444 pairs of aligned infrared and visible images with high quality.

You could run (visualize.py)[https://github.com/Linfeng-Tang/MSRS/blob/main/visualize.py] to visualize segmentation labels 

Some typical examples are shown below(the left column are Vis images and the right column are IR images):
<img  src="./test/vi/00537D.png"  width="384"  height="288.0"/>  <img  src="./test/ir/00537D.png"  width="384"  height="288.0"/>

<img  src="./train/vi/00633D.png"  width="384"  height="288.0"/>  <img  src="./train/ir/00633D.png"  width="384"  height="288.0"/>

<img  src="./train/vi/00881N.png"  width="384"  height="288.0"/>  <img  src="./train/ir/00881N.png"  width="384"  height="288.0"/>

<img  src="./train/vi/01023N.png"  width="384"  height="288.0"/>  <img  src="./train/ir/01023N.png"  width="384"  height="288.0"/>

  

If this dataset is helpful to you, please cite it as:
```
@article{Tang2022PIAFusion,
  title={PIAFusion: A progressive infrared and visible image fusion network based on illumination aware},
  author={Tang, Linfeng and Yuan, Jiteng and Zhang, Hao and Jiang, Xingyu and Ma, Jiayi},
  journal={Information Fusion},
  year={2022},
  publisher={Elsevier}
}
```
