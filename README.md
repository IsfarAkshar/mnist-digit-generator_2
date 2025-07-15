
# 🧠 MNIST Digit Generator (DCGAN)

This project trains a Deep Convolutional GAN (DCGAN) on the MNIST dataset to generate realistic handwritten digits 5 times. The webpage is published and you can check it out here https://mnist-digit-generator2-fxfpjhvvgceejz2f7jcrsk.streamlit.app/ 

---

## ⚙️ Tools & Tech Used

- **Python (PyTorch)** – DCGAN implementation using neural networks  
- **Torchvision** – For loading the MNIST dataset and image transformations  
- **Matplotlib** – For plotting generated digit samples  
- **Jupyter / Python Scripts** – For training and visualizing model output  

---

## 📊 Features

- 🧠 **DCGAN Architecture** – Generator & Discriminator models built using Conv/TransposeConv layers  
- 🔁 **Training Loop** – Epoch-wise training with visual logging  
- 📁 **Output Directory** – Saves generated digits per epoch  
- 📷 **Image Sampling** – Real-time visualization of model progress  
- 🧪 **Evaluation** – Visual inspection of digit quality across epochs  

---

## 🧠 Key Learning Outcomes

- Understand how GANs work (Generator vs. Discriminator)  
- Build deep neural networks with convolutional layers in PyTorch  
- Generate synthetic data (handwritten digits)  
- Monitor model training with visual samples  
- Learn the importance of adversarial loss and training stability  

---

## 🚀 How to Run

1. Install dependencies:

    ```bash
    pip install torch torchvision matplotlib
    ```

2. Run the training script:

    ```bash
    python train.py
    ```

3. Check generated digit samples in the `outputs/` folder after each epoch.

---

## 📷 Sample Outputs

Below are example generated images saved during training:

![Epoch 1](outputs/epoch_1.png)  
![Epoch 10](outputs/epoch_10.png)  

---

## 💡 References

- [DCGAN Paper](https://arxiv.org/abs/1511.06434)  
- [PyTorch DCGAN Tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)

---

## 🧑‍💼 Add to Your CV

> Built a GAN-based digit generation model using PyTorch and trained it on MNIST to produce realistic handwritten digit images.  
> Tools used: PyTorch, torchvision, matplotlib.

---

## 📬 Connect

**Author**: *Isfar Ibn Mufty*  
📫 isfarakshar@gmail.com

Feel free to fork or adapt this for exploring GANs, synthetic image generation, or computer vision education.
