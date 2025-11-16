import streamlit as st
import math

# ----------------------------
# Streamlit Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Advanced Calculator")
st.write("Perform basic and scientific calculations easily!")

# ----------------------------
# Input for numbers
# ----------------------------
number1 = st.number_input("Enter first number:", value=0.0)
number2 = st.number_input("Enter second number (for binary operations):", value=0.0)

# ----------------------------
# Choose operation
# ----------------------------
operation = st.selectbox(
    "Select Operation",
    [
        "Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)",
        "Power (x^y)", "Square Root", "Factorial", 
        "Sin", "Cos", "Tan", "Logarithm (base 10)", "Natural Log (ln)"
    ]
)

result = None

# ----------------------------
# Perform Calculation
# ----------------------------
try:
    if operation == "Addition (+)":
        result = number1 + number2
    elif operation == "Subtraction (-)":
        result = number1 - number2
    elif operation == "Multiplication (*)":
        result = number1 * number2
    elif operation == "Division (/)":
        if number2 != 0:
            result = number1 / number2
        else:
            st.error("Error: Division by zero is not allowed")
    elif operation == "Power (x^y)":
        result = number1 ** number2
    elif operation == "Square Root":
        if number1 >= 0:
            result = math.sqrt(number1)
        else:
            st.error("Error: Square root of negative number is not allowed")
    elif operation == "Factorial":
        if number1 >= 0 and int(number1) == number1:
            result = math.factorial(int(number1))
        else:
            st.error("Error: Factorial is only defined for non-negative integers")
    elif operation == "Sin":
        result = math.sin(math.radians(number1))
    elif operation == "Cos":
        result = math.cos(math.radians(number1))
    elif operation == "Tan":
        result = math.tan(math.radians(number1))
    elif operation == "Logarithm (base 10)":
        if number1 > 0:
            result = math.log10(number1)
        else:
            st.error("Error: Logarithm undefined for non-positive numbers")
    elif operation == "Natural Log (ln)":
        if number1 > 0:
            result = math.log(number1)
        else:
            st.error("Error: Natural log undefined for non-positive numbers")
except Exception as e:
    st.error(f"Error: {e}")

# ----------------------------
# Show Result
# ----------------------------
if result is not None:
    st.success(f"Result: {result}")
