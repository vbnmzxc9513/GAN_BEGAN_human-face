# GAN_BEGAN for human face
0857214 student: 蔡詠平


## Tool: Pytorch
## Method: BEGAN

# Step
1.face detect and cut the ROI in the image (Data/face_detect.py)

2.random flip the image left to right

3.train the model by BEGAN algo (began5.py)

4.generate image (generate2.py)

# Config5
I try a lot of paramater this one is the best one in 48000 iter.

## Massive reference
Boundary Equilibrium Generative Adversarial Networks: https://arxiv.org/abs/1703.10717

DCGAN: https://github.com/chenyuntc/pytorch-book/tree/master/chapter7-GAN%E7%94%9F%E6%88%90%E5%8A%A8%E6%BC%AB%E5%A4%B4%E5%83%8F

BEGAN implement: https://github.com/sunshineatnoon/Paper-Implementations/tree/master/BEGAN

# Result
![image](https://github.com/vbnmzxc9513/GAN_BEGAN_hw2/blob/master/500_image.png)
