# A comparative analysis of deep learning models for lung segmentation on X-ray images

The aim of the project is to create a ranking of deep learning solutions for lung segmentation on X-ray images. 
The task is to create a benchmark of existing solutions and analyse the advantages and disadvantages of each one.

## Scope of work
- analyzing existing deep learning models for lung segmentation on X-ray images,
- evaluating them on diverse dataset, 
- assessing their performance under various image modifications. 

The ultimate goal is to identify the most accurate method for lung segmentation across different scenarios, contributing to advancements in medical imaging technology.

## Reproduced works

- [**Lung VAE**](./LungVAE) aims to be a lung segmentation model that is not dependent on training set distribution. For this purpose, a U-net-based segmentation network encoder and variational encoder are used. As the authors did not train the model on opacity cases, the variational encoder is used for data imputation and may be treated as data augmentation. The results of the U-net encoder and variational encoder are concatenated and passed to the decoder. [(Selvan et al., 2020)](https://arxiv.org/abs/2005.10052)

- [**TransResUNet**](./TransResUNet) is an improved version of the U-net model dedicated to the task of lung field segmentation. Three modifications were made. First, a pre-trained encoder was taken from the VGG-16 architecture trained on the ImageNet dataset. The first seven layers were used. As a second improvement, skip connections with a series of convolution blocks were added between the encoder and decoder layers. Finally, a dedicated post-processing step with hole filling, artifacts removal, and morphological opening was applied to the output images. [(Reza et al., 2020)](https://doi.org/10.1109/TENSYMP50017.2020.9230835)

- [**CE-Net**](./CE-Net) is a U-net-based approach of a context encoder network aimed at capturing more abstract and preserving spatial information for 2D medical image segmentation. It consists of three components: a feature encoder module, a context extractor, and a feature decoder module. For feature extraction, a pretrained ResNet-34 is used. Dense atrous convolution blocks and residual multi-kernel pooling are used for context extraction. Transposed convolution is applied in the feature decoder module. [(Gu et al., 2019)](https://doi.org/10.1109/TMI.2019.2903562)


## Useful literature

- [Tilborghs et al. "Comparative study of deep learning methods for automatic segmentation of lung, lesion, and lesion type in CT scans of COVID-19 patients"](https://arxiv.org/abs/2007.15546)
- [Segment Me If You Can - A Benchmark for Anomaly Segmentation](https://segmentmeifyoucan.com/)
- [COVID-19 Imaging-based AI Research Collection - datasets](https://github.com/HzFu/COVID19_imaging_AI_paper_list/blob/master/README.md#dataset)
- [Hryniewska et al. "Checklist for responsible deep learning modeling of medical images based on COVID-19 detection studies"](https://doi.org/10.1016/j.patcog.2021.108035)
- [Çallı et al. "Deep learning for chest X-ray analysis: A survey"](https://doi.org/10.1016/j.media.2021.102125)
