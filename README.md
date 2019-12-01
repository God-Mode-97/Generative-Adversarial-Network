# Generative-Adversarial-Network
**This project was carried out during my internship at IIIT-Allahabad for generating new videos using generative adversarial networks.**

1. **UCF-101** video dataset is used for this project.
2. Firstly, the **frames** from each video are are extracted using **openCV** on which our model is trained. 
3. Next we train two models, one **generative model** and another **discriminative model** on a video dataset and created new videos using **GANs**.
4. A **Deep Convolutional Neural Network** is used as our architecture in our Generative Adversarial Network.
5. **Adam** and **SGD** are the optimizers used in our model.
6. The main objective is to use the general GAN architecture for 2D images but in this we need to train it for every **time step** as each frame is not independent but depends on the previous frames. 
7. The generated frames are arranged in **sequential form** to generate a video.

