import streamlit as st
import pandas as pd
import joblib

def app():
    model = joblib.load('Final_model.h5')
    st.set_page_config(page_title="Car Prediction ")
    st.title("Used Car Prediction")
    st.header("Epsilon Diploma Project")

    st.write("This project predicts Used Car Prices based on some features")

    
    year = st.number_input("Year", value=0)
    fuel = st.radio('Select Kind', ['Benzine', 'Natural Gas'])
    kilometers = st.number_input("Kilometers 0 - 200000", value=0)
    engine = st.radio("engine", ['1300CC', '1500CC', '1600CC'])
    transmission = st.radio('Select Type of Transmission', ['Manual', 'Automatic'])
    Age_of_Car = st.selectbox('Select Type of Transmission', ['Old', 'New'])
    body = st.selectbox('Select Type of body', ['Sedan', 'Hatchback','SUV'])
    brand = st.selectbox('Select Brand', ['Hyundai', 'Fiat','Chevrolet'])
    color = st.selectbox('Select Color', ['Beige', 'Black','Blue- Navy Blue', 'Brown', 'Burgundy','Gold', 'Gray', 'Green', 'Orange', 'Red','Silver','White','Yellow', 'Other Color'])
    
    
    predict = st.button("Predict")
    if predict:
        df = pd.DataFrame.from_dict(
            {
                'Year':[year],
                'Fuel':[0 if fuel == 'Benzine' else 1],
                'Kilometers':[kilometers],
                'Engine':[1300 if engine == '1300CC' else (1500 if engine == '1500CC' else 1600)],
                'Transmission':[0 if transmission == 'Manual' else 1],
                'Age_of_Car':[0 if Age_of_Car == 'Old' else 1],
                'Body':[0 if body == 'Sedan' else (1 if body == 'Hatchback' else 2)],
                'Brand':[0 if brand == 'Hyundai' else (1 if body == 'Fiat' else 2)],
                'Color':[0 if color == 'Beige' else (1 if color == 'Black' else  (2 if color == 'Blue- Navy Blue' else  (3 if color == 'Brown' else  (4 if color == 'Burgundy' else  (5 if color == 'Gold' else  (6 if color == 'Gray' else  (7 if color == 'Green' else  (8 if color == 'Orange' else (9 if color == 'Red' else (10 if color == 'Silver' else(11 if color == 'White' else(12 if color == 'Yellow' else 13 ))))))))))))]
            }
        )

        st.write("Input Data: ")
        st.dataframe(df)

        pred = model.predict(df)
        st.write(F"Prediction: {pred}")

app()
