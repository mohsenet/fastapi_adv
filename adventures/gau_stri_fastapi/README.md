# 1. FastAPI Backend (The Brain)  
**What it does:**  
This is like a math wizard that works behind the scenes. It has two special skills:

1. **"Generate Gaussian" Skill**  
   - Creates bell-curve shaped data (like height measurements in a population)  
   - Needs to know:  
     - Where the bell curve should center (`mean`)  
     - How wide/spread out it should be (`std_dev`)  
     - How many data points to create  

2. **"Calculate Density" Skill**  
   - For any point on the bell curve, it calculates how "likely" that value is  
   - Example: If average height is 170cm (mean), it can tell you how common 180cm would be  

**How you use it:**  
You don't interact directly with this - it quietly runs in the background waiting for requests.

# 2. Streamlit Frontend (The Friendly Interface)  
**What it does:**  
This is the pretty face of the app with two tabs:

# Tab 1: Bell Curve Generator  
- **What you see:**  
  - Sliders to adjust the curve's shape  
  - A "Generate" button  
  - A beautiful bell curve that updates instantly  

- **What you learn:**  
  - How changing the mean moves the curve left/right  
  - How changing standard deviation makes it wider/narrower  

# 🔍 Tab 2: Probability Finder  
- **What you see:**  
  - Sliders to set up your curve  
  - A marker you can drag along the curve  
  - The exact probability number at that point  

- **What you learn:**  
  - Where the highest probability is (always at the center!)  
  - How probabilities decrease as you move away from center  

# Real-world Example  
Imagine we're studying **pizza delivery times**:
1. **Tab 1** would show:  
   - Most deliveries arrive around 30 minutes (mean)  
   - Some come in 25-35 minutes (small std_dev = consistent)  
   - Or maybe 20-40 minutes (large std_dev = inconsistent)  

2. **Tab 2** could tell you:  
   - How likely is a 15-minute delivery? (Very unlikely!)  
   - How likely is a 28-32 minute delivery? (Very likely!)  

# How to Use It  
1. Open two terminals:  
   - First run `python fastapi_app.py` (starts the brain)  
   - Then run `streamlit run streamlit_app.py` (opens the interface)  

2. Play with the sliders - see how the curves change in real-time!
