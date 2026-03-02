# ⚕️ Obesity Level Prediction Web App 

An end-to-end Machine Learning application that predicts a person's obesity category based on lifestyle habits and provides personalized health recommendations through an interactive web interface.

---

## 🌐 Live Concept

This project simulates a real-world healthcare assistant where a user enters daily lifestyle information and instantly receives:

* Predicted obesity category
* BMI indicator
* Personalized improvement tips

> Goal: Move beyond model accuracy → deliver **actionable insights** to users.

---

## 🧠 Machine Learning Workflow

1. Data Cleaning & Validation
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Handling Missing Values
5. Encoding Categorical Variables (OneHotEncoder)
6. Scaling Numerical Features (StandardScaler)
7. Model Training (Logistic Regression Classifier)
8. Pipeline Creation (Preprocessing + Model)
9. Model Serialization (Pickle)
10. Deployment using Streamlit UI

---

## 📊 Input Features

| Feature                | Description                  |
| ---------------------- | ---------------------------- |
| Gender                 | Male / Female                |
| Age                    | User age                     |
| Height                 | Height in meters             |
| Weight                 | Weight in kg                 |
| Family Obesity History | Genetic risk factor          |
| High Calorie Food      | Frequent junk food intake    |
| Vegetable Consumption  | Daily vegetable frequency    |
| Meals Per Day          | Eating frequency             |
| Snacking Habit         | Between-meal eating behavior |
| Smoking                | Smoking habit                |
| Water Intake           | Hydration level              |
| Monitor Calories       | Tracks calorie consumption   |
| Physical Activity      | Exercise frequency           |
| Screen Time            | Technology usage hours       |
| Alcohol                | Alcohol consumption          |
| Transportation         | Daily movement type          |

---

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Pickle (Model Serialization)

---

## ✨ Features

✔ Predicts obesity level (multi-class classification)
✔ Real-time BMI calculation
✔ Personalized health suggestions
✔ Responsive modern UI
✔ Clean preprocessing pipeline
✔ Production-style deployment

---

## 📂 Project Structure

```
Obesity-Prediction/
│
├── Obesity.pkl_Logistic_regression   # Trained ML model
├── obesity_streamlit_ui.py           # Streamlit web app
├── dataset.csv                       # Dataset used for training
├── requirements.txt                  # Required libraries
└── README.md                         # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/Obesity-Prediction.git
cd Obesity-Prediction
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\\Scripts\\activate   (Windows)
source venv/bin/activate  (Linux/Mac)
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Application

```
streamlit run obesity_streamlit_ui.py
```

---

## 📈 Model Details

* Algorithm: Logistic Regression
* Problem Type: Multi-Class Classification
* Preprocessing: StandardScaler + OneHotEncoder
* Pipeline: ColumnTransformer + Pipeline

---

## 🧪 Example Output

User Input → Model Prediction → Personalized Advice

Example:

```
Prediction: Obesity_Type_I
Advice: Increase daily cardio and avoid late-night meals
```

---

## 🧩 Common Issues & Fixes

### Model not loading error

If you see sklearn attribute errors while loading model:

```
AttributeError: Can't get attribute '_RemainderColsList'
```

Install the same sklearn version used during training:

```
pip install scikit-learn==1.2.2
```

---

## 🔮 Future Improvements

* SHAP explainability visualization
* Diet recommendation engine
* Cloud deployment (Render / AWS / GCP)
* Mobile-friendly UI
* Database logging

---

## 🎯 Learning Outcomes

* Building ML pipelines correctly
* Handling categorical & numerical preprocessing
* Deploying ML models to web apps
* Designing usable ML interfaces
* Debugging real deployment issues

---

## 🤝 Contribution

Pull requests and suggestions are welcome.

---

## 📬 Contact

If you liked this project, connect with me on LinkedIn and share feedback!
