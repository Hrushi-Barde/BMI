import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function for the app
def main():
    st.title("BMI Calculator")
    
    # Input fields
    st.header("Enter your details:")
    name = st.text_input("Name")
    height = st.number_input("Height (in meters)", format="%.2f")
    weight = st.number_input("Weight (in kilograms)", format="%.2f")
    blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    contact_number = st.text_input("Contact Number")
    
    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            st.success(f"{name}, your BMI is {bmi} ({category})")
        else:
            st.error("Please enter valid height and weight.")
    
    # Display entered information
    if st.button("Show Details"):
        st.subheader("Entered Information")
        st.write(f"**Name:** {name}")
        st.write(f"**Height:** {height} meters")
        st.write(f"**Weight:** {weight} kg")
        st.write(f"**Blood Group:** {blood_group}")
        st.write(f"**Contact Number:** {contact_number}")

if __name__ == "__main__":
    main()
