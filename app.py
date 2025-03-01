import streamlit as st

# Title of the app
st.title("Unit Converter")

# Define conversion functions
def length_conversion(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * conversions[to_unit] / conversions[from_unit]

def weight_conversion(value, from_unit, to_unit):
    conversions = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274,
    }
    return value * conversions[to_unit] / conversions[from_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    else:
        return value  # Same unit

# Sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Input fields
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "miles", "feet", "inches"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "miles", "feet", "inches"])
    result = length_conversion(value, from_unit, to_unit)
elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To Unit", ["grams", "kilograms", "pounds", "ounces"])
    result = weight_conversion(value, from_unit, to_unit)
elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = temperature_conversion(value, from_unit, to_unit)

# Display the result
if st.button("Convert"):
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

st.markdown("""
    <style>
        .streamlit-expanderHeader {
            cursor: pointer !important;
        }
        .stSelectbox div {
            cursor: pointer !important;
        }
    </style>
""", unsafe_allow_html=True)


# Add footer
st.markdown("""
    <style>
        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 10px 0;
            background-color: #f1f1f1;
            text-align: center;
            font-size: 14px;
            color: #555;
        }
    </style>
    <footer>
        <p>Unit Converter App | Created by Jargina Chohan | © 2025</p>
    </footer>
""", unsafe_allow_html=True)