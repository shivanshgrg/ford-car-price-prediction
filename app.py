import streamlit as st
import pandas as pd
import pickle

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Ford Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# ===============================
# LOAD MODEL
# ===============================
model = pickle.load(open("car_model.pkl", "rb"))

# ===============================
# TITLE
# ===============================
st.title("🚗 Ford Car Price Predictor")
st.write("Machine Learning Based Used Ford Car Price Prediction")

st.metric("Model Accuracy (R²)", "0.83")

st.divider()

# ===============================
# INPUTS
# ===============================
year = st.slider("Year", 1996, 2023, 2018)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=25000
)

tax = st.number_input(
    "Road Tax",
    min_value=0,
    value=150
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=55.0
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    value=1.5,
    step=0.1
)

car_model = st.selectbox(
    "Car Model",
    [
        ' C-MAX',
        ' EcoSport',
        ' Edge',
        ' Escort',
        ' Fiesta',
        ' Focus',
        ' Fusion',
        ' Galaxy',
        ' Grand C-MAX',
        ' Grand Tourneo Connect',
        ' KA',
        ' Ka+',
        ' Kuga',
        ' Mondeo',
        ' Mustang',
        ' Puma',
        ' Ranger',
        ' S-MAX',
        ' Streetka',
        ' Tourneo Connect',
        ' Tourneo Custom',
        ' Transit Tourneo',
        'Focus'
    ]
)

transmission = st.selectbox(
    "Transmission",
    [
        "Automatic",
        "Manual",
        "Semi-Auto"
    ]
)

fuel = st.selectbox(
    "Fuel Type",
    [
        "Diesel",
        "Electric",
        "Hybrid",
        "Other",
        "Petrol"
    ]
)

# ===============================
# PREDICT
# ===============================
if st.button("Predict Price"):

    data = {
        'year':year,
        'mileage':mileage,
        'tax':tax,
        'mpg':mpg,
        'engineSize':engineSize,

        'model_ C-MAX':0,
        'model_ EcoSport':0,
        'model_ Edge':0,
        'model_ Escort':0,
        'model_ Fiesta':0,
        'model_ Focus':0,
        'model_ Fusion':0,
        'model_ Galaxy':0,
        'model_ Grand C-MAX':0,
        'model_ Grand Tourneo Connect':0,
        'model_ KA':0,
        'model_ Ka+':0,
        'model_ Kuga':0,
        'model_ Mondeo':0,
        'model_ Mustang':0,
        'model_ Puma':0,
        'model_ Ranger':0,
        'model_ S-MAX':0,
        'model_ Streetka':0,
        'model_ Tourneo Connect':0,
        'model_ Tourneo Custom':0,
        'model_ Transit Tourneo':0,
        'model_Focus':0,

        'transmission_Manual':0,
        'transmission_Semi-Auto':0,

        'fuelType_Electric':0,
        'fuelType_Hybrid':0,
        'fuelType_Other':0,
        'fuelType_Petrol':0
    }

    # Model Encoding
    if f"model_{car_model}" in data:
        data[f"model_{car_model}"] = 1

    # Transmission Encoding
    if transmission == "Manual":
        data['transmission_Manual'] = 1

    elif transmission == "Semi-Auto":
        data['transmission_Semi-Auto'] = 1

    # Fuel Encoding
    if fuel == "Electric":
        data['fuelType_Electric'] = 1

    elif fuel == "Hybrid":
        data['fuelType_Hybrid'] = 1

    elif fuel == "Other":
        data['fuelType_Other'] = 1

    elif fuel == "Petrol":
        data['fuelType_Petrol'] = 1

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    st.success(
        f"Predicted Price: £{prediction:,.0f}"
    )

st.divider()

st.caption(
    "Built using Python • Pandas • Scikit-Learn • Streamlit"
)