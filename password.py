import streamlit as st
import re

def password_strength(password):
    score = 0
    feedback=[]

   # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter")

    if re.search (r'[a-z]',password):
        score +=1
    else:
        feedback.append("passsword should contain at least one lowercase letter (a-z)")

    if re.search (r'[0-9]',password):
        score += 1
    else:
        feedback.append("password should contain atleast one digit (0-9)")

    if  re.search (r'[!@#$%^&*]', password):
        score +=1
    else:
        feedback.append("password at least **one special character** (!@#$%^&*).")

        return score, feedback
    
    def get_password_strength(score):
        if score < 2:
            return "Weak"
        elif score < 4:
            return "Moderate"
        else:
            return "Strong"
        
        # Streamlit UI with CSS styling
st.markdown("""
<style>
    .title {
        text-align: center;
        color: #2C3E50;
        font-size: 40px;
        font-weight: bold;
    }
    .feedback {
        color: #E74C3C;
    }
    .success {
        color: #27AE60;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Password Strength Meter</p>', unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        score, feedback = password_strength(password)
        password_strength = password_strength(score)

        st.write(f"Password Strength: **{password_strength}** (Score: {score})")

        if password_strength == "Weak":
            st.markdown("### Suggestions to improve your password:")
            for suggestion in feedback:
                st.markdown(f"- {suggestion}", unsafe_allow_html=True)
        elif password_strength == "Strong":
            st.markdown('<p class="success">Your password is strong! Great job!</p>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a password to check its strength.")

