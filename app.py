import streamlit as st
# Custom CSS for background image
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://t3.ftcdn.net/jpg/05/07/66/60/360_F_507666066_J8zsoPcCnW0uGcEYzoT0RElpHACKxd6e.jpg");
    background-size: cover;
    background-position: center;
}
</style>
'''
# Applying the background image
st.markdown(page_bg_img, unsafe_allow_html=True)
# Calculator with Emojis
st.write('# 🧮 CALCULATOR')  # Emoji for the calculator title
# Input fields for numbers
number1 = st.number_input('🔢 Please, enter first number')
number2 = st.number_input('🔢 Please, enter second number')
# Add a submit button
if st.button('Calculate 💡'):  # Button with emoji
    num3 = number1 + number2
    st.write('# 📝 The answer is: ', num3)  # Show result after clicking the button
