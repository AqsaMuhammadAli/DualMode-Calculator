import streamlit as st
import sympy as sp

# Set up streamlit interface
st.title("Simple and Scientific Calculator")

# Define allowed functions for the scientific calculator
allowed_functions = {
    'sin': sp.sin,
    'cos': sp.cos,
    'tan': sp.tan,
    'log': sp.log,   # Natural logarithm (ln)
    'exp': sp.exp,   # Exponential function
    'sqrt': sp.sqrt, # Square root
    'pi': sp.pi,
    'e': sp.E,
    'factorial': sp.factorial
}

# Simple calculator function
def simple_calculator(a, operator, b):
    if operator == 'Add':
        return a + b
    elif operator == 'Subtract':
        return a - b
    elif operator == 'Multiply':
        return a * b
    elif operator == 'Divide':
        return a / b
    else:
        return "Invalid Operator!"

# Scientific calculator function
def scientific_calculator(expression):
    try:
        result = sp.sympify(expression, locals=allowed_functions)
        return result.evalf()  # Evaluate with floating point precision
    except Exception as e:
        return f"Error: {e}"

# Select mode
mode = st.selectbox("Select Calculator Mode", ["Simple", "Scientific"])

if mode == "Simple":
    # Simple calculator interface
    st.write("### Simple Calculator")
    a = st.number_input("Enter first number", format="%f")
    operator = st.selectbox("Select operator", ["Add", "Subtract", "Multiply", "divide"])
    b = st.number_input("Enter second number", format="%f")
    
    if st.button("Calculate"):
        result = simple_calculator(a, operator, b)
        st.write(f"Result: {result}")

elif mode == "Scientific":
    # Scientific calculator interface
    st.write("### Scientific Calculator")
    expression = st.text_input("Enter a mathematical expression (e.g. sin(pi/2) + log(10)):")
    
    if st.button("Calculate"):
        result = scientific_calculator(expression)
        st.write(f"Result: {result}")
