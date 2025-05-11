import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Gaussian Distribution Section
st.header("Gaussian Distribution Demo")

# Generate synthetic data
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=1000)  # mean=0, std=1

# Calculate statistics
mu = np.mean(data)
sigma = np.std(data)

# Create figure
fig, ax = plt.subplots(figsize=(8, 4))

# Plot histogram
ax.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')

# Plot PDF
xmin, xmax = ax.get_xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
ax.plot(x, p, 'k', linewidth=2, label=f'PDF (μ={mu:.2f}, σ={sigma:.2f})')

# Add labels and legend
ax.set_title('Gaussian Distribution')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.legend()

# Display in Streamlit
st.pyplot(fig)

# Show statistics
st.subheader("Statistics")
st.write(f"- Mean (μ): {mu:.4f}")
st.write(f"- Standard Deviation (σ): {sigma:.4f}")
st.write(f"- Sample Size: {len(data)} points")

# Add some explanation
st.markdown("""
### What's this showing?
- We generated 1000 random points from a normal distribution
- The green bars show the histogram of the actual data
- The black curve shows the theoretical probability density function (PDF)
- μ (mu) is the mean (center) of the distribution
- σ (sigma) is the standard deviation (spread) of the distribution
""")
