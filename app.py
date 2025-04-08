import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ------------------ Google Sheets Setup ------------------
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Hyuever_Vote_Results").sheet1

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="CMUxHyuever Feedback",
    page_icon="🍜",
    layout="centered"
)

# ------------------ Branding ------------------
st.image("hyuever_logo.png", width=220)
st.markdown("""
<h2 style='text-align: center; color: #D7263D;'>Welcome to CMUxHyuever!</h2>
<p style='text-align: center;'>Delicious Korean street food made by <b>Hyu</b>, for <b>whoever</b>!</p>
""", unsafe_allow_html=True)

# ------------------ Menu Section ------------------
st.markdown("## 🥢 Our Menu")

st.markdown("### 🍜 Cupbokki - $6.99")
st.write("- Spicy Korean rice cakes served in a cup.")
st.write("- Includes 1 Gimmari (seaweed roll), cut into two pieces.")
st.write("- Want it spicier? Ask for a free drizzle of Buldak sauce! 🔥")

st.markdown("### 🍬 Dalgona - $1.99")
st.write("- Traditional Korean sugar candy.")
st.write("- Crushed pieces available for sampling.")

st.markdown("### 🎉 Combo Set - $7.99")
st.write("- Includes Cupbokki + Dalgona — save $1!")

# ------------------ Heating Instructions ------------------
st.markdown("## ♨️ Heating Instructions")
st.write("All items are stored at room temperature.\nFor the best taste, please microwave for **2 minutes and 30 seconds** before eating.")

# ------------------ Feedback Survey ------------------
st.markdown("## 📊 Customer Satisfaction Survey")
st.write("This survey is anonymous and takes just 30 seconds. Your feedback helps us improve!")

# Likert-scale questions
taste = st.slider("How satisfied were you with the taste of Cupbokki?", 1, 5, 3)
price = st.slider("How reasonable was the price?", 1, 5, 3)
overall = st.slider("Overall, how satisfied were you with your experience?", 1, 5, 3)

# Comment section
comment = st.text_area("Any suggestions or message for Hyu? We'd love to hear from you! 😊")

# Privacy notice
st.caption("\u2728 This survey is anonymous. No personal data, email, or browser info is collected.")

# Submission control
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    if st.button("Submit Feedback"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([timestamp, taste, price, overall, comment])
        st.session_state.submitted = True
        st.success("Thank you so much for your feedback! 🌟")
else:
    st.info("You have already submitted feedback. Thank you again! 😊")

# ------------------ Footer ------------------
st.markdown("---")
st.markdown("### 👉 Follow Us")
st.write("Instagram: [@hyuever](https://www.instagram.com/hyuever)")
st.caption("Project: CMUxHyuever | Made with ❤️ in Pittsburgh")
