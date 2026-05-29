import pickle
import numpy as np
import streamlit as st

# ---------------- Load Model ----------------
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- Page Config ----------------
st.set_page_config(page_title="Weight Prediction App", page_icon="⚖️", layout="centered")

# ---------------- UI Styling ----------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 34px;
    color: #FF4B4B;
    font-weight: bold;
}

.sub-text {
    text-align: center;
    font-size: 18px;
    color: #6C3483;
}

.result-box {
    background-color: #F4ECF7;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown('<p class="main-title">⚖️ Weight Prediction AI App</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Predict weight from height using Machine Learning</p>', unsafe_allow_html=True)

st.write("---")

# ---------------- Input ----------------
height = st.number_input("Enter height (in feet)", min_value=1.0, max_value=8.0, value=5.8)

weight_actual = st.number_input("Enter actual weight (kg)", min_value=10.0, max_value=200.0, value=60.0)

# ---------------- Prediction ----------------
if st.button("Predict Weight 🚀"):

    # Convert input to 2D array
    input_data = np.array([[height]])

    # Prediction (FIXED)
    predicted_weight = model.predict(input_data).item()

    # ---------------- BMI Calculation ----------------
    height_m = height * 0.3048
    bmi = weight_actual / (height_m ** 2)

    bmi = float(bmi)  # safety fix

    # BMI Category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # ---------------- Output ----------------
    st.markdown("### 📊 Results")

    st.markdown(f"""
    <div class="result-box">
        Predicted Weight: {predicted_weight:.2f} kg <br>
        BMI: {bmi:.2f} <br>
        Health Category: {category}
    </div>
    """, unsafe_allow_html=True)

    # Difference
    diff = predicted_weight - weight_actual

    if diff > 0:
        st.info(f"You are {abs(diff):.2f} kg under predicted weight.")
    else:
        st.warning(f"You are {abs(diff):.2f} kg above predicted weight.")