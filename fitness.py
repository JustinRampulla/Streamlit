import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def calculate(weight, height, unit):
    bmi = weight / ((height / 100) ** 2) 
    return bmi

st.title('Fitness Checker')
st.write('Welcome! Let us find out about your BMI.')

unit = st.selectbox('Select preferred units', ['Metric', 'Imperial']) #NEW

if unit == 'Metric':
    weight = st.slider('Enter your weight (kg)', 30.0, 300.0, 70.0, 0.1) #NEW
    height = st.slider('Enter your height (cm)', 100.0, 300.0, 170.0, 0.1)
else:
    weight = st.slider('Enter your weight (lbs)', 66.0, 661.0, 154.0, 0.1)
    feet = st.slider('Enter your height (feet)', 3, 9, 5)
    inches = st.slider('Enter your height (inches)', 0, 11, 7)
    
if st.button('Calculate BMI'): #NEW
    if unit == 'Imperial':
        inches += (12 * feet)
        height = inches * 2.54  
    result = calculate(weight, height, unit)
    st.write(f'Your BMI is: {result:.2f}')
    if result < 18.5:
        st.write('You are underweight.')
    elif 18.5 <= result < 25:
        st.write('You are in the healthy weight range.')
    elif 25 <= result < 30:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')
    category = ['Underweight', 'Healthy Weight', 'Overweight', 'Obese']
    value = [calculate(18.5, height, unit), calculate(25, height, unit),
                  calculate(30, height, unit), result]
    
    df = pd.DataFrame({
        'BMI Category': category,
        'BMI Value': value
    })

    fig, ax = plt.subplots()
    ax.barh(df['BMI Category'], df['BMI Value'], color='skyblue')
    ax.set_xlabel('BMI Value')  
    ax.set_title('BMI Categories')
    st.pyplot(fig) #NEW
    
    trend = [result, 25.0, 27.0, 24.5, 26.0] 
    dates = pd.date_range('2023-01-01', periods=5)
    bmiData = pd.DataFrame({'Date': dates, 'BMI': trend})
    bmiData.set_index('Date', inplace=True)
    st.header('BMI Trends Over Time')
    st.line_chart(bmiData) #NEW
