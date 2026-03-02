import streamlit as st
import pandas as pd
import pickle

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Obesity Prediction", page_icon="⚕️", layout="wide")

# -------------------- ADVANCED CUSTOM CSS --------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg,#eef5ff,#f9fbff,#ffffff);
}

/* Title */
.main-title {
    font-size:44px;
    font-weight:800;
    background: linear-gradient(90deg,#1f77ff,#00b894);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.section-card {
    padding:22px;
    border-radius:18px;
    background:white;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    margin-bottom:20px;
    transition:0.3s ease;
}
.section-card:hover {
    transform: translateY(-3px);
    box-shadow:0 10px 25px rgba(0,0,0,0.12);
}

/* Buttons */
.stButton>button {
    height:55px;
    font-size:18px;
    font-weight:600;
    border-radius:14px;
    background: linear-gradient(90deg,#1f77ff,#00b894);
    color:white;
    border:none;
}
.stButton>button:hover {
    background: linear-gradient(90deg,#1254c7,#009e74);
}

/* Metric box */
[data-testid="stMetric"] {
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
}

/* Prediction result */
.result-box {
    padding:25px;
    border-radius:18px;
    text-align:center;
    font-size:26px;
    font-weight:700;
    background:linear-gradient(90deg,#1f77ff,#00b894);
    color:white;
    box-shadow:0 10px 25px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Load trained model
model = pickle.load(open('Obesity.pkl_Logistic_regression','rb'))

# -------------------- HEADER --------------------
st.markdown('<div class="main-title">⚕️ Obesity Level Prediction</div>', unsafe_allow_html=True)
st.caption("AI powered lifestyle based health assessment")

st.divider()

# -------------------- LAYOUT --------------------
left, right = st.columns([2,1])

with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🧍 Personal Information")
    c1, c2, c3 = st.columns(3)

    with c1:
        Gender = st.selectbox("Gender", ["Male","Female"])
    with c2:
        Age = st.number_input("Age", 1, 100, 25)
    with c3:
        Height = st.number_input("Height (meters)", 1.0, 2.5, 1.70)

    Weight = st.number_input("Weight (kg)", 20.0, 200.0, 70.0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🍔 Food Habits")
    c4, c5, c6 = st.columns(3)

    with c4:
        family_history_with_overweight = st.selectbox("Family Obesity History", ["yes","no"])
        FAVC = st.selectbox("High Calorie Food", ["yes","no"])
    with c5:
        FCVC = st.slider("Vegetable Consumption",1,3,2)
        NCP = st.slider("Meals per Day",1,4,3)
    with c6:
        CAEC = st.selectbox("Snacking Habit", ["no","Sometimes","Frequently","Always"])
        CH2O = st.slider("Water Intake",1,3,2)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🏃 Lifestyle")
    c7, c8, c9 = st.columns(3)

    with c7:
        SMOKE = st.selectbox("Smoking", ["yes","no"])
        SCC = st.selectbox("Monitor Calories", ["yes","no"])
    with c8:
        FAF = st.slider("Physical Activity",0,3,1)
        TUE = st.slider("Screen Time (hrs)",0,10,2)
    with c9:
        CALC = st.selectbox("Alcohol", ["no","Sometimes","Frequently","Always"])
        MTRANS = st.selectbox("Transportation", ["Walking","Bike","Motorbike","Public_Transportation","Automobile"])
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- SIDE PANEL --------------------
with right:
    st.markdown("### 📊 Health Indicator")
    bmi = Weight/(Height**2)
    st.metric("BMI", round(bmi,2))
    if bmi < 18.5:
        st.info("Underweight")
    elif bmi < 25:
        st.success("Healthy Range")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")

    st.markdown("---")
    

# Create dataframe
input_data = pd.DataFrame({
    'Gender':[Gender],
    'Age':[Age],
    'Height':[Height],
    'Weight':[Weight],
    'family_history_with_overweight':[family_history_with_overweight],
    'FAVC':[FAVC],
    'FCVC':[FCVC],
    'NCP':[NCP],
    'CAEC':[CAEC],
    'SMOKE':[SMOKE],
    'CH2O':[CH2O],
    'SCC':[SCC],
    'FAF':[FAF],
    'TUE':[TUE],
    'CALC':[CALC],
    'MTRANS':[MTRANS]
})

st.divider()

# Prediction
center = st.columns([1,2,1])[1]
with center:
    if st.button("🔍 Predict Obesity Level", use_container_width=True):
        prediction = model.predict(input_data)[0]
        st.markdown(f'<div class="result-box">Predicted Category: {prediction}</div>', unsafe_allow_html=True)

        st.markdown("### 🥗 Recommended Tips")

        tips = {
            "Insufficient_Weight": [
                "Increase calorie intake with healthy foods",
                "Eat more frequently",
                "Include protein rich foods",
                "Strength training exercises"
            ],
            "Normal_Weight": [
                "Maintain balanced diet",
                "Continue regular physical activity",
                "Stay hydrated",
                "Sleep 7-8 hours daily"
            ],
            "Overweight_Level_I": [
                "Reduce sugary drinks",
                "Walk at least 30 minutes daily",
                "Control portion sizes",
                "Increase vegetable intake"
            ],
            "Overweight_Level_II": [
                "Start structured exercise routine",
                "Avoid fried foods",
                "Monitor calorie intake",
                "Drink more water"
            ],
            "Obesity_Type_I": [
                "Daily cardio exercise",
                "Consult diet plan",
                "Avoid late night meals",
                "Track daily calories"
            ],
            "Obesity_Type_II": [
                "Medical consultation recommended",
                "Strict low calorie diet",
                "Regular physical activity",
                "Limit processed foods"
            ],
            "Obesity_Type_III": [
                "Immediate medical supervision required",
                "Personalized diet plan",
                "Low impact exercise only",
                "Monitor health parameters regularly"
            ]
        }

        for tip in tips.get(prediction, ["Maintain healthy lifestyle"]):
            st.write(f"• {tip}")
