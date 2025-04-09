import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ------------------ Google Sheets Setup ------------------
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets["google_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
client = gspread.authorize(creds)
sheet = client.open("Hyuever_Vote_Results").sheet1

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="CMUxHyuever Feedback",
    page_icon="🍜",
    layout="centered"
)

# ------------------ Branding ------------------
st.markdown("""
<div style='text-align: center;'>
  <img src='https://raw.githubusercontent.com/diziba213/Hyuever/main/hyuever_logo.png' width='220'>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align: center; color: #D7263D;'>Welcome to CMUxHyuever!</h2>
<p style='text-align: center;'>Delicious Korean street food made by <b>Hyu</b>, for <b>whoever</b>!</p>
""", unsafe_allow_html=True)

# ------------------ Menu Section ------------------
st.markdown("## 🍲 Our Menu")

st.markdown("""
<div style='text-align: center;'>
  <img src='https://raw.githubusercontent.com/diziba213/Hyuever/main/hyuever_logo.png' width='360'>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div style='border: 1px solid #eee; border-radius: 10px; padding: 16px; margin-top: 20px; margin-bottom: 20px; background-color: #fffaf0;'>
        <h3 style='color:#D7263D;'>🔥 Cupbokki - $6.99</h3>
        <ul style='color:#333;'>
            <li><b>Spicy</b> Korean rice cakes served in a cup</li>
            <li>Includes <span style='color:#444'><b>1 Gimmari</b></span> (seaweed roll), cut into two pieces</li>
            <li>Want it spicier? <span style='color:#D7263D;'>Free Buldak Sauce drizzle!</span> 🔥</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div style='border: 1px solid #eee; border-radius: 10px; padding: 16px; margin-bottom: 20px; background-color: #fffdf7;'>
        <h3 style='color:#D4A017;'>⭐ Dalgona - $1.99</h3>
        <ul style='color:#333;'>
            <li>Traditional Korean sugar candy</li>
            <li>Crushed pieces available for sampling</li>
        </ul>
        <p style='font-size: 0.9em; color: #aa0000'><b>⚠ Contains sugar. Manufactured in a facility that may process nuts.</b></p>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div style='border: 1px solid #eee; border-radius: 10px; padding: 16px; margin-bottom: 20px; background-color: #f7faff;'>
        <h3 style='color:#007ACC;'>🥡 Combo Set - $7.99</h3>
        <ul style='color:#333;'>
            <li>Includes <b>Cupbokki + Dalgona</b> — <span style='color:green;'>Save $1!</span></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------ Heating Instructions ------------------
st.markdown("## ♨️ Heating Instructions")
st.write("All items are stored at room temperature.\nFor the best taste, please microwave for **2 minutes and 30 seconds** before eating.")

# ------------------ Feedback Survey ------------------
st.markdown("## 📝 Customer Satisfaction Survey")
st.write("This survey is anonymous and takes just 30 seconds. Your feedback helps us improve!")

star_options = ["⭐", "⭐ ⭐", "⭐ ⭐ ⭐", "⭐ ⭐ ⭐ ⭐", "⭐ ⭐ ⭐ ⭐ ⭐"]

taste = st.select_slider("How satisfied were you with the taste of Cupbokki?", options=star_options, value="⭐ ⭐ ⭐")
price = st.select_slider("How reasonable was the price?", options=star_options, value="⭐ ⭐ ⭐")
overall = st.select_slider("Overall, how satisfied were you with your experience?", options=star_options, value="⭐ ⭐ ⭐")

comment = st.text_area("Any suggestions or message for Hyu? We'd love to hear from you! 😊")

st.caption("✨ This survey is anonymous. No personal data, email, or browser info is collected.")

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
