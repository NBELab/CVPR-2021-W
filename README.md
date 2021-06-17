# Image Reconstruction from Neuromorphic Event Cameras using Laplacian Prediction and Poisson Integration with Spiking and Artificial Neural Networks

![Model](https://github.com/NBELab/CVPR-2021-W/blob/main/figures/model_new.png)

## Install

Dependencies:

- [NumPy](https://www.numpy.org/)
- [Scipy](https://www.scipy.org/)
- [Tensorflow](https://www.tensorflow.org/)
- [Nengo](https://www.nengo.ai/)
- [Nengo-dl](https://www.nengo.ai/nengo-dl/)
- [Opencv-python](https://pypi.org/project/opencv-python/)

## Notebooks

The code for the shared weighed model :[shared_weight_model.ipynb](https://github.com/NBELab/CVPR-2021-W/blob/main/notebooks/shared_weight_model.ipynb)

The code for the spiking neural network: [nengo_snn_PI_model_5.ipynb](https://github.com/NBELab/CVPR-2021-W/blob/main/notebooks/nengo_snn_PI_model_5.ipynb)

## Dataset

We converted each event-file from [N-Caltech Dataset](https://www.garrickorchard.com/datasets/n-caltech101) to a 6 channels tesnsor.
[Download the full converted dataset](https://drive.google.com/file/d/112HOcpBoR2dr2Xlq4QT3yvxjZ17zmuaU/view?usp=sharing).

Or download subset of the dataset: [testX](https://drive.google.com/file/d/1iMwDNw7k6r-uN7--6oYCjf_12Dw4G4xY/view?usp=sharing) is the inputs to model.
[testY](https://drive.google.com/file/d/1a9RfKLQCXPTnaT-GbWXjY88bGr5qmTiL/view?usp=sharing) is the targets (Laplacians of the original [Caltech 101](http://www.vision.caltech.edu/Image_Datasets/Caltech101/) image)


## Paper

[Paper](https://openaccess.thecvf.com/content/CVPR2021W/EventVision/html/Duwek_Image_Reconstruction_From_Neuromorphic_Event_Cameras_Using_Laplacian-Prediction_and_Poisson_CVPRW_2021_paper.html)

```bibtex
@InProceedings{Duwek_2021_CVPR,
    author    = {Duwek, Hadar Cohen and Shalumov, Albert and Tsur, Elishai Ezra},
    title     = {Image Reconstruction From Neuromorphic Event Cameras Using Laplacian-Prediction and Poisson Integration With Spiking and Artificial Neural Networks},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2021},
    pages     = {1333-1341}
}
```
