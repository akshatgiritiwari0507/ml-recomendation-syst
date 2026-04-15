from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "1234"

# ===================== Load Datasets ======================
precautions = pd.read_csv("recommender systems/antibiotic recommendation system/datasets/disease_precaution_plan_with_uniqueness.csv")
workout = pd.read_csv("recommender systems/antibiotic recommendation system/datasets/disease_workout_plan_unique.csv")
antib = pd.read_csv('recommender systems/antibiotic recommendation system/datasets/updated_antibiotics (1).csv')
diet = pd.read_csv("recommender systems/antibiotic recommendation system/datasets/disease_diet_plan_unique.csv")

# ===================== Load Models ======================
svc = pickle.load(open('recommender systems/antibiotic recommendation system/svc.pkl', 'rb'))

# Load random forest model correctly
with open('recommender systems/antibiotic recommendation system/random_forest_model.pkl', 'rb') as model_file:
    model_data = pickle.load(model_file)
    
    if isinstance(model_data, dict) and "model" in model_data:
        model = model_data["model"]
        feature_names = model_data["feature_names"]
    else:
        model = model_data  # If it's directly a model
        feature_names = []  # Set an empty list if feature names are unknown

# Load scaler
with open('recommender systems/antibiotic recommendation system/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# ======================= Helper Function ======================
def helper(dis):
    pre = precautions[precautions['Disease'] == dis][['Precaution 1', 'Precaution 2', 'Precaution 3', 'Precaution 4', 'Precaution 5']].values.tolist()
    anti = antib[antib['Disease'] == dis][['Primary Antibiotic', 'Alternate Antibiotic 1', 'Alternate Antibiotic 2', 'Reason for Recommendation', 'Primary Antibiotic Description']].values.tolist()
    die = diet[diet['Disease'] == dis][['Morning', 'Lunch', 'Snacks', 'Dinner', 'Night']].values.tolist()
    work = workout[workout['Disease'] == dis][['Workout 1', 'Workout 2', 'Workout 3', 'Workout 4', 'Workout 5']].values.tolist()
    return pre, anti, die, work

# ===================== Symptoms and Disease Mapping ======================
symptoms_dict = { "abdominal_pain": 0, "cough": 14, "fever": 31, "fatigue": 29, "headache": 33, "joint_pain": 41, "nausea": 49, "sore_throat": 69, "vomiting": 81 }
disease_list = { 3: "bacterial_pneumonia", 26: "tuberculosis", 28: "urinary_tract_infection", 14: "lyme_disease" }

# ============ Model Prediction Function =============
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for symptom in patient_symptoms:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
    return disease_list.get(svc.predict([input_vector])[0], "Unknown Disease")

# ==================== Routes ====================
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('email')
#     password = request.form.get('password')
    
#     if username == USERNAME and password == PASSWORD:
#         session['logged_in'] = True
#         return redirect(url_for('home'))
#     return "<h1>Invalid Credentials. Please <a href='/'>try again</a>.</h1>"

@app.route('/home')
def home():
    if 'logged_in' in session and session['logged_in']:
        return render_template('home.html')
    return redirect(url_for('index'))

@app.route('/general')
def general():
    if 'logged_in' in session and session['logged_in']:
        return render_template('general.html')
    return redirect(url_for('index'))

@app.route('/specific')
def specific():
    if 'logged_in' in session and session['logged_in']:
        return render_template('specific.html')
    return redirect(url_for('index'))

@app.route('/predict', methods=['POST'])
def predict():
    if 'logged_in' in session and session['logged_in']:
        symptoms = request.form.get('symptoms', '')
        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        predicted_disease = get_predicted_value(user_symptoms)
        pre, anti, die, work = helper(predicted_disease)

        return render_template('specific.html', predicted_disease=predicted_disease, dis_pre=pre, dis_anti=anti, dis_die=die, dis_work=work)
    return redirect(url_for('index'))

@app.route('/resistance', methods=['GET', 'POST'])
def resistance():
    if request.method == 'POST':
        form_data = request.json

        species = {f"Species_{key}": 0 for key in ["Clostridium difficile", "Enterococcus faecium", "Escherichia coli"]}
        species[f"Species_{form_data['species']}"] = 1

        demographics = {
            "Gender_Male": int(form_data.get("gender", 0)),
            "MIC (μg/mL)": float(form_data.get("mic", 0.0)),
            "Age": int(form_data.get("age", 0)),
            "Year": int(form_data.get("year", 0))
        }

        user_input = {**species, **demographics}
        user_df = pd.DataFrame([user_input])

        if feature_names:
            user_df = user_df.reindex(columns=feature_names, fill_value=0)

        scaled_data = scaler.transform(user_df)
        prediction = model.predict(scaled_data)

        return jsonify({"Resistance_Level": prediction[0]})

    if 'logged_in' in session and session['logged_in']:
        return render_template('resistance.html')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
