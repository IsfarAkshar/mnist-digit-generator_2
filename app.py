import streamlit as st
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.gen = nn.Sequential(
            nn.Linear(100 + 10, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, 784),
            nn.Tanh()
        )

    def forward(self, noise, labels):
        labels_one_hot = torch.nn.functional.one_hot(labels, num_classes=10).float()
        x = torch.cat([noise, labels_one_hot], 1)
        return self.gen(x)

device = torch.device("cpu")
model = Generator().to(device)
model.load_state_dict(torch.load("generator_epoch30.pth", map_location=device))
model.eval()

st.title("Handwritten Digit Image Generator")
digit = st.selectbox("Choose a digit to generate (0-9):", list(range(10)))
if st.button("Generate Images"):
    noise = torch.randn(5, 100)
    labels = torch.full((5,), digit, dtype=torch.long)
    with torch.no_grad():
        images = model(noise, labels).view(-1, 28, 28).numpy()

    st.write(f"Generated images of digit {digit}")
    cols = st.columns(5)
    for i in range(5):
        fig, ax = plt.subplots()
        ax.imshow(images[i], cmap='gray')
        ax.axis('off')
        cols[i].pyplot(fig)