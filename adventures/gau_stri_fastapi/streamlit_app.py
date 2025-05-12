import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

st.title("Gaussian Distribution Explorer")
st.write("Interactive demonstration of Gaussian properties")

tab1, tab2 = st.tabs(["Distribution Generator", "Probability Density Calculator"])

with tab1:
    st.header("Gaussian Distribution Generator")
    mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0, key="mean_gen")
    std_dev = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, key="std_gen")
    size = st.slider("Sample size", 100, 10000, 1000, key="size_gen")

    if st.button("Generate Distribution"):
        try:
            response = requests.get(
                f"http://localhost:8000/generate_gaussian?mean={mean}&std_dev={std_dev}&size={size}"
            )
            if response.status_code == 200:
                result = response.json()
                
                fig, ax = plt.subplots()
                ax.hist(result["data"], bins=30, alpha=0.7, density=True)
                
                # Plot theoretical curve
                x = np.linspace(mean-4*std_dev, mean+4*std_dev, 100)
                y = (1/(std_dev * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mean)/std_dev)**2)
                ax.plot(x, y, 'r-', label='Theoretical PDF')
                
                ax.set_title(f"Gaussian Distribution (μ={result['mean']:.2f}, σ={result['std_dev']:.2f})")
                ax.legend()
                st.pyplot(fig)
                
                st.write(f"Sample mean: {result['mean']:.4f}")
                st.write(f"Sample standard deviation: {result['std_dev']:.4f}")
        except requests.exceptions.ConnectionError:
            st.error("Backend not available")

with tab2:
    st.header("Probability Density Calculator")
    mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0, key="mean_dens")
    std_dev = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, key="std_dens")
    x = st.slider("Point x to evaluate", -10.0, 10.0, 0.0)

    if st.button("Calculate Density"):
        try:
            response = requests.get(
                f"http://localhost:8000/calculate_density?x={x}&mean={mean}&std_dev={std_dev}"
            )
            if response.status_code == 200:
                result = response.json()
                
                st.metric(
                    label=f"Probability Density at x = {result['x']}",
                    value=f"{result['density']:.4f}",
                    help=f"μ = {result['mean']}, σ = {result['std_dev']}"
                )
                
                # Visualize the point
                fig, ax = plt.subplots()
                x_vals = np.linspace(mean-4*std_dev, mean+4*std_dev, 100)
                y_vals = (1/(std_dev * np.sqrt(2*np.pi))) * np.exp(-0.5*((x_vals-mean)/std_dev)**2)
                ax.plot(x_vals, y_vals, 'b-', label='PDF')
                ax.axvline(x, color='red', linestyle='--', alpha=0.5)
                ax.plot(x, result['density'], 'ro', label=f'x = {x}')
                ax.set_title("Probability Density Function")
                ax.legend()
                st.pyplot(fig)
        except requests.exceptions.ConnectionError:
            st.error("Backend not available")
