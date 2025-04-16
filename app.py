import streamlit as st
import pickle
from PIL import Image
import base64

def add_background_image(image_file):
    with open(image_file, "rb") as file:
        base64_image = base64.b64encode(file.read()).decode()

    css_style = f"""
     <style>
     .stApp {{
         background-image: url("data:image/jpg;base64,{base64_image}");
         background-size: cover;
         background-position: center;
         background-repeat: no-repeat;
     }}
     </style>
     """
    st.markdown(css_style, unsafe_allow_html=True)

def main():
    add_background_image("smoke.jpg")
  
    st.sidebar.title('Guidance 🧭')
    page=st.sidebar.radio('Go to',['Home','Prediction'])

    if page=='Home':
        st.title(":green[🚬 WELCOME TO THE SMOKING DETECTION APP]")
        st.markdown(
            """ <p style='color:black;'>Smoking has significant implications for individual and public health, 
            making early detection and monitoring crucial in combating its adverse effects. 
            With advancements in technology, biosignal analysis has emerged as a powerful tool for identifying behavioral patterns,
             including smoking habits. This app leverages Streamlit, a cutting-edge framework, 
             to deliver a user-friendly platform for determining smoking behaviors through biosignals. 
             By analyzing key physiological signals, the app offers a novel approach to smoking detection, 
             fostering awareness and aiding in the development of effective intervention strategies. 
            Go to Prediction to enter your details and check whether there is a presence of smoking.</p>
            """,
            unsafe_allow_html=True
        )


    elif page=='Prediction':
        st.title(":green[🚬 DETERMINE THE PRESENCE OF SMOKING THROUGH BIO-SIGNALS]")
        gender = st.radio("Select Gender: ", ('Male', 'Female'))
        age= st.text_input("Enter Your age","Type here...")
        height= st.slider("Select your height in cm", 120, 200,step=1)
        weight= st.slider("Select your weight in kg", 30, 150,step=1)
        waist = st.slider("Select your waist size in cm", 40.0, 150.0,step=0.1)
        eyesight_left = st.slider("Select the left eyesight", 0.1, 9.9, step=0.1)
        eyesight_right = st.slider("Select the right eyesight", 0.1, 9.9, step=0.1)
        hearing_left = st.radio("Can you hear clearly on the left side?", ('yes', 'no'))
        hearing_right = st.radio("Can you hear clearly on the right side?", ('yes', 'no'))
        systolic = st.slider("Select your systolic blood pressure level", 71.0, 240.0, step=0.1)
        relaxation = st.slider("Select your relaxation blood pressure level", 40.0, 146.0, step=0.1)
        fasting_blood_sugar = st.slider("Select your fasting blood sugar level", 46.0, 505.0, step=0.1)
        triglyceride = st.slider("Select your triglyceride level", 5.0, 1000.0,step=0.1)
        HDL = st.slider("Select your HDL level", 4, 620, step=1)
        hemoglobin = st.slider("Select your hemoglobin level", 3.9, 25.1,step=0.1)
        serum_creatinine = st.slider("Select your serum_creatinine level", 0.1, 11.6, step=0.1)
        ALT = st.slider("Select your ALT level", 1.0, 1000.0, step=0.1)
        Gtp = st.slider("Select your Gtp level", 1.0, 1000.0,step=0.1)
        dental_caries = st.radio("Do you have any dental cavities? ",('yes', 'no'))
        tartar = st.radio("Do you have any hardened plaque on the teeth?", ('yes', 'no'))

        gender_map = {'Male': 1, 'Female': 0}
        tartar_map = {'yes': 1, 'no': 0}
        hearing_left_map={'yes':1,'no':2}
        hearing_right_map = {'yes': 1, 'no': 2}
        dental_caries_map={'yes':1,'no':0}

        features=[gender_map[gender],age,height,weight,waist,eyesight_left,eyesight_right,hearing_left_map[hearing_left],hearing_right_map[hearing_right],systolic,relaxation,fasting_blood_sugar,triglyceride,HDL,hemoglobin,serum_creatinine,ALT,Gtp,dental_caries_map[dental_caries],tartar_map[tartar]]
        scaler = pickle.load(open("smoking_scaler.sav", 'rb'))
        model = pickle.load(open("smoking_model.sav", 'rb'))
        pred = st.button("PREDICT")
        if pred:
            result = model.predict(scaler.transform([features]))
            if result == 0:
                st.info("Absence of Smoking detected")
            else:
                st.info("Presence of Smoking detected")

main()














