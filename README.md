# Heart Condition Prediction

## Overview

The **Heart Condition Prediction** project is a Streamlit application designed to assess the likelihood of heart conditions based on various input parameters. Users provide information such as age, sex, blood pressure, cholesterol levels, and more, and the application delivers a result indicating whether the user is safe or if further medical attention is advisable.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vijaytakbhate2002/heart-condition-prediction.git
   cd heart-condition-prediction
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the Application:**
   Open your web browser and go to [http://localhost:8501](http://localhost:8501).

5. **Input Parameters:**
   - Age
   - Sex (0 for female, 1 for male)
   - Chest Pain Type (cp_num)
   - Resting Blood Pressure (trestbps)
   - Cholesterol (chol)
   - Fasting Blood Sugar (fps_num)
   - Resting Electrocardiographic Results (restecg_num)
   - Maximum Heart Rate Achieved (thalach)
   - Exercise-Induced Angina (exang_num)
   - Oldpeak
   - Slope of the Peak Exercise ST Segment (slope_num)
   - Number of Major Vessels Colored by Fluoroscopy (ca_num)
   - Thalassemia (thal_num)

6. **Result:**
   - "You are Safe! :thumbsup: 🤓" if safe
   - "You need to check up for heart. Don't worry, I am just 97% accurate. 😞" if unsafe.

## Folder Structure

- `app.py`: Main Streamlit application file.
- `heart_disease_model`: Folder containing the heart disease prediction model.
- `requirements.txt`: List of project dependencies.
