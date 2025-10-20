import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Happyyyy 💖")

# Tạo hình trái tim
t = np.linspace(0, 2*np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# Vẽ hình
fig, ax = plt.subplots()
ax.fill(x, y, color='red')
ax.axis('equal')
ax.axis('off')

st.pyplot(fig)
st.write("Happy women day")
