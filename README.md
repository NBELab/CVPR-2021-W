# Image Reconstruction from Neuromorphic Event Cameras using Laplacian Prediction and Poisson Integration with Spiking and Artificial Neural Networks

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
