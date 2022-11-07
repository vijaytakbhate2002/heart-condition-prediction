import streamlit as st
import joblib as jb
import numpy as np
import pandas as pd

model = jb.load('heart disease model')

st.title("Heart Disease Prediction")

st.markdown('### Enter age 👇')
age = st.number_input('',1,130)

st.markdown('''### Gender 👇''')
genlis = ['female','male']
sex = st.selectbox('',genlis)
sex_num =  genlis.index(sex)
st.write(sex_num)

# Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain -- Value 4: asymptomatic
st.markdown('''### Chest pain type (4 values) 👇''')
chestpainlis = ['typical angina 1','atypical angina 2','non-anginal pain 3','asymptomatic 4']
cp = st.selectbox("cp",chestpainlis)
cp_num = chestpainlis.index(cp)
st.write(cp_num)

st.markdown("### Resting blood pressure (90,250) 👇")
trestbps = st.number_input("trestbps",90,250,)
st.write(trestbps)

st.markdown("### Serum cholestoral in mg/dl (70,600) 👇")
chol = st.number_input("chol",70,600)
st.write(chol)
if st.button("chol",help="How to calculate serum cholesterol level"):
    st.write("Add your HDL and LDL cholesterol levels, plus 20 percent of your triglycerides, to calculate your serum cholesterol levels. If you have an LDL of 150 mg/dL")

st.markdown('''### fasting blood sugar((1 = true; 0 = false)) 👇''')
fpslis = ['False','True']
fps = st.selectbox("fps",fpslis)
fps_num = fpslis.index(fps)
st.write(fps_num)

st.markdown("### Resting electrocardiographic results 👇")
restecglis = ['normal','having','hypertrophy']
restecg = st.selectbox("restecg",restecglis)
restecg_num = restecglis.index(restecg)
st.write(restecg_num)
if st.button("restecg",help="information about resting electrocardiographic"):
    st.write('''restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)''')

st.markdown("### maximum heart rate achieved (50,250) 👇")
thalach = st.slider("thalach",50,250)
st.write(thalach)

st.markdown("### exercise induced angina (1 = yes; 0 = no) 👇")
exanglis = ['no','yes']
exang = st.selectbox("exang",exanglis)
exang_num = exanglis.index(exang)
st.write(exang_num)

st.markdown("### ST depression induced by exercise relative to rest (0.0,7.5) 👇")
oldpeak = st.slider("oldpeak",0.0,7.5)
st.write(oldpeak)
if st.button('oldpeak',help="information Exercise induced ST segment depression"):
    st.write("Exercise induced ST segment depression is considered a reliable ECG finding for the diagnosis of obstructive coronary atherosclerosis.\n It has also been associated with a worse prognosis for patients with a documented coronary artery disease (CAD).")

st.markdown("### slope of the peak exercise ST segment 👇")
slopelis = ['upsloping','flat','downsloping']
slope = st.selectbox("slope",slopelis)
slope_num = slopelis.index(slope)
st.write(slope_num)

st.markdown("### number of major vessels (0-3) colored by flourosopy 👇")
calis = [0,1,2,3,4]
ca = st.selectbox("ca",calis)
ca_num = ca
st.write(ca_num)

st.markdown("### thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
thallis = ['normal defect','fixed defect','reversible defect','other']
thal = st.selectbox("thal",thallis)
thal_num = thallis.index(thal)
if st.button("thal info",help="Information about thal"):
    st.write('''What does Thal mean in heart disease dataset? thal: A blood disorder called thalassemia Value 0: NULL (dropped from the dataset previously. Value 1: fixed defect (no blood flow in some part of the heart) Value 2: normal blood flow.''')
st.write("🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐🧐")

def prediction():
    row = np.array([age, sex_num, cp_num, trestbps, chol, fps_num, restecg_num,thalach, exang_num, oldpeak, slope_num, ca_num,thal_num])
    X = pd.DataFrame([row])
    result = model.predict(X)
    if result == 0:
        st.success("You are Safe Cill :thumbsup: 🤓 ")
    else:
        st.error("You need to check up for heart, Dont worry I am just 97% accurate 😞")

st.button("Prediction",on_click=prediction)


