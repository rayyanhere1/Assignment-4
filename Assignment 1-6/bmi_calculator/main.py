import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("BMI Calculator 📊")
st.markdown("Welcome to the BMI Calculator. Please enter your weight (in kg) and height (in meters) to calculate your Body Mass Index (BMI).")

weight = st.number_input("Enter your weight (kg):", min_value=1, max_value=300, value=70)
height = st.number_input("Enter your height (m):", min_value=0.5, max_value=3.0, value=1.75)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")


        if bmi < 18.5:
            st.error("You are underweight. 🏃‍♂️ Eat a balanced diet!")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight. ✅ Keep up the good work!")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight. 🚶‍♂️ Exercise regularly.")
        else:
            st.danger("You are obese. 💪 Consult a healthcare provider.")
    else:
        st.error("Please enter valid weight and height values.")

st.markdown("---")
st.markdown("Made with ❤️ using **Streamlit** and **Python**.")
