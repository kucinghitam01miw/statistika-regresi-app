import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

st.set_page_config(page_title="Statistika Regresi", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f3d8c1;  /* peach */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    h1.judul-retro {
        font-family: 'Press Start 2P', cursive;
        color: #596cad;
        margin-bottom: 10px;
    }
    h3.subjudul-retro {
        font-family: 'Press Start 2P', cursive;
        color: #596cad;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="judul-retro">Aplikasi Statistika Regresi</h1>', unsafe_allow_html=True)

st.write("""
Masukkan data X dan Y kamu (pisahkan dengan koma).
Contoh: 1, 2, 3, 4
""")

# Input data X
x_input = st.text_input("Masukkan data X:", "1, 2, 3, 4, 5")
# Input data Y
y_input = st.text_input("Masukkan data Y:", "2, 4, 5, 4, 5")

def parse_input(text):
    try:
        return np.array([float(i.strip()) for i in text.split(",")])
    except:
        st.error("Format input salah! Gunakan angka dipisah koma.")
        return None

x = parse_input(x_input)
y = parse_input(y_input)

if x is not None and y is not None:
    if len(x) != len(y):
        st.error("Jumlah data X dan Y harus sama!")
    elif len(x) < 2:
        st.error("Data harus minimal 2 titik.")
    else:
        # Hitung regresi linear
        slope, intercept, r_value, p_value, std_err = linregress(x, y)

        st.markdown('<h3 class="subjudul-retro">Hasil Perhitungan</h3>', unsafe_allow_html=True)
        st.write(f"Persamaan Regresi:  Y = {intercept:.3f} + {slope:.3f}X")
        st.write(f"Koefisien Korelasi (r): {r_value:.3f}")
        st.write(f"Koefisien Determinasi (r²): {r_value**2:.3f}")

        # Plot grafik
        fig, ax = plt.subplots()
        ax.scatter(x, y, label="Data")
        ax.plot(x, intercept + slope * x, color='red', label="Garis Regresi")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        st.pyplot(fig)