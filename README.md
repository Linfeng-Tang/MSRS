# MSRS: Multi-Spectral Road Scenarios for Practical Infrared and Visible Image Fusion 
## ✨ News  

- **[2025-09-18]** Our paper *[ControlFusion: A Controllable Image Fusion Framework with Language-Vision Degradation Prompts](https://arxiv.org/pdf/2503.23356?)* has been officially accepted by **Advances in Neural Information Processing Systems (NeurIPS 2025)**! [[Paper](https://arxiv.org/pdf/2503.23356?)] [[Code](https://github.com/Linfeng-Tang/ControlFusion)]  

- **[2025-09-10]** Our paper *[Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion](https://ieeexplore.ieee.org/document/11162636)* has been officially accepted by **IEEE Transactions on Pattern Analysis and Machine Intelligence (IEEE TPAMI)**! [[Paper](https://ieeexplore.ieee.org/document/11162636)] [[Code](https://github.com/Linfeng-Tang/Mask-DiFuser)]  

- **[2025-03-15]** Our paper *[C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning](https://github.com/Linfeng-Tang/C2RF)* has been officially accepted by the **International Journal of Computer Vision (IJCV)**! [[Paper](https://link.springer.com/article/10.1007/s11263-025-02427-1)] [[Code](https://github.com/Linfeng-Tang/C2RF)]  

- **[2025-02-11]** We released a large-scale dataset for infrared and visible video fusion: *[M2VD: Multi-modal Multi-scene Video Dataset](https://github.com/Linfeng-Tang/M2VD)*.  


We construct a new multi-spectral dataset for infrared and visible image fusion based on the **[MFNet](https://www.mi.t.u-tokyo.ac.jp/static/projects/mil_multispectral/)** dataset. The MFNet dataset contains 1,569 image pairs (820 taken at the daytime and 749 taken at nighttime) with spatial resolution is 480 × 640. However, There are many misaligned image pairs in the MFNet dataset and most infrared images are low signal-to-noise and low contrast. To this end, we first collect 715 daytime image pairs and 729 nighttime image pairs via removing 125 misaligned image pairs. Moreover, an image enhancement algorithm based on dark channel prior is leveraged to optimize the contrast and signal-to-noise of infrared images. As a result, the released new Multi-Spectral Road Scenarios (**MSRS**) dataset contains 1,444 pairs of aligned infrared and visible images with high quality.

You could run [visualize.py](https://github.com/Linfeng-Tang/MSRS/blob/main/visualize.py) to visualize segmentation labels 

Some typical examples are shown below(the left column are Vis images and the right column are IR images):
<img  src="./test/vi/00537D.png"  width="384"  height="288.0"/>  <img  src="./test/ir/00537D.png"  width="384"  height="288.0"/>

<img  src="./train/vi/00633D.png"  width="384"  height="288.0"/>  <img  src="./train/ir/00633D.png"  width="384"  height="288.0"/>

<img  src="./train/vi/00881N.png"  width="384"  height="288.0"/>  <img  src="./train/ir/00881N.png"  width="384"  height="288.0"/>

<img  src="./train/vi/01023N.png"  width="384"  height="288.0"/>  <img  src="./train/ir/01023N.png"  width="384"  height="288.0"/>

  

If this dataset is helpful to you, please cite it as:
```
@article{Tang2024Mask-DiFuser,
  author={Tang, Linfeng and Li, Chunyu and Ma, Jiayi},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title={Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion}, 
  year={2025},
  volume={},
  number={},
  pages={1-18},
 }
```

```
@article{Tang2024C2RF,
	title={C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning}, 
	author={Tang, Linfeng and Yan, Qinglong and Xiang, Xinyu and Fang, Leyuan and Ma, Jiayi},
	journal={International Journal of Computer Vision}, 
	pages={5262--5280},
	volume={133},
	year={2025},
}
```
```
@article{Tang2022PIAFusion,
  title={PIAFusion: A progressive infrared and visible image fusion network based on illumination aware},
  author={Tang, Linfeng and Yuan, Jiteng and Zhang, Hao and Jiang, Xingyu and Ma, Jiayi},
  journal={Information Fusion},
  year={2022},
  publisher={Elsevier}
}
```

```
@article{TangSeAFusion,
title = {Image fusion in the loop of high-level vision tasks: A semantic-aware real-time infrared and visible image fusion network},
author = {Linfeng Tang and Jiteng Yuan and Jiayi Ma},
journal = {Information Fusion},
volume = {82},
pages = {28-42},
year = {2022},
issn = {1566-2535},
publisher={Elsevier}
}
```

```
@article{Ma2022SwinFusion,
  title={SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer},
  author={Ma, Jiayi and Tang, Linfeng and Fan, Fan and Huang, Jun and Mei, Xiaoguang and Ma, Yong},
  journal={IEEE/CAA Journal of Automatica Sinica},
  volume={9},
  number={7},
  pages={1200--1217},
  year={2022},
  publisher={IEEE}
}
```

