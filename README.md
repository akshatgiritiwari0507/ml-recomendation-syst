# ml-recomendation-syst
# 🩺 Antibiotic Recommendation & Resistance Prediction System

A machine learning-powered healthcare web application that predicts bacterial diseases based on symptoms, recommends suitable antibiotics, and analyzes antibiotic resistance levels using patient demographics and bacterial species data.

This project was developed as a **hackathon healthcare solution** to assist in early disease identification, safe antibiotic suggestions, and resistance awareness.

---

## 🚀 Features

- 🔍 **Disease Prediction**
  - Predicts possible bacterial diseases from user-entered symptoms.

- 💊 **Antibiotic Recommendation**
  - Suggests:
    - Primary antibiotic
    - Alternate antibiotics
    - Recommendation reason
    - Antibiotic description

- 🛡️ **Precaution Plans**
  - Provides disease-specific precautions.

- 🥗 **Diet Recommendations**
  - Personalized meal plans:
    - Morning
    - Lunch
    - Snacks
    - Dinner
    - Night

- 🏋️ **Workout Suggestions**
  - Recovery-friendly exercise plans.

- 🧪 **Antibiotic Resistance Prediction**
  - Predicts resistance level based on:
    - Species
    - MIC value
    - Age
    - Gender
    - Year

- 🌐 **Flask Web Interface**
  - User-friendly UI with multiple pages and interactive forms.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript
- **Model Storage:** Pickle (.pkl)
- **Templates:** Jinja2

---

## 📂 Project Structure

```bash
project/
├── main.py
├── templates/
├── static/
└── recommender systems/
    └── antibiotic recommendation system/
        ├── datasets/
        ├── svc.pkl
        ├── scaler.pkl
        └── random_forest_model.pkl





⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the project
python main.py
▶️ Usage
Open browser:
http://127.0.0.1:5000
Enter symptoms in comma-separated format
Example:
fever,cough,fatigue
Get:
Disease prediction
Antibiotic suggestions
Precautions
Diet plan
Workout plan
Use resistance prediction module for advanced ML-based resistance analysis.
📊 ML Models Used
Support Vector Classifier (SVC) → disease prediction
Random Forest Classifier → antibiotic resistance prediction
StandardScaler → feature normalization
⚠️ Important Note

Large model files may be excluded from GitHub due to file size limitations.

If random_forest_model.pkl is missing, add it manually before running the resistance prediction module.

🌟 Future Enhancements
User authentication system
Real-time medical API integration
Cloud deployment
More bacterial species support
Improved symptom database
Better UI/UX dashboard
👨‍💻 Developed For

🏆 Hackathon Project
Healthcare + Machine Learning + Antibiotic Resistance Awareness

📜 License

This project is for educational and hackathon purposes only.
Not intended for real-world medical diagnosis without professional validation.
