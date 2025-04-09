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
  <img src='https://raw.githubusercontent.com/diziba213/Hyuever/main/hyuever_logo.png' style='max-width: 100%; height: auto;' width='220'>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align: center; color: #D7263D;'>Welcome to CMUxHyuever!</h2>
<p style='text-align: center; font-size: 1.05rem;'>Delicious Korean street food made by <b>Hyu</b>, for <b>whoever</b>!</p>
""", unsafe_allow_html=True)

# ------------------ Styling ------------------
st.markdown("""
<style>
div.stButton > button {
    background-color: #D7263D;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 0.5em 1.2em;
}
.card {
    border: 1px solid #eee;
    border-radius: 10px;
    padding: 16px;
    margin: 24px auto;
    background-color: #fffdf7;
}
.emoji-radio label {
    font-size: 1.6rem;
    margin-right: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Menu Section ------------------
st.markdown("## 🍽️ Our Menu")

st.markdown("""
<div style='text-align: center;'>
  <img src='https://raw.githubusercontent.com/diziba213/Hyuever/main/hyuever_logo.png' style='max-width: 100%; height: auto;' width='360'>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class='card'>
        <h3 style='color:#007ACC;'>🥡 Set Menu (세트메뉴)
        <span style='font-size: 1.25rem; margin-left: 10px;'>
            <del>$8.99</del> <span style='font-size: 1.25rem; color:#D7263D; font-weight:bold;'>$7.99</span>
        </span>
        </h3>
        <ul style='color:#333; font-size: 1.05rem;'>
            <li>Includes <b>TTEOKBOKKI + DALGONA</b> (떡볶이 + 달고나) — <span style='color:green;'>Save $1!</span></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# ------------------ Tteokbokki Section ------------------
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://raw.githubusercontent.com/diziba213/Hyuever/main/cupbokki.png", width=240)
    with col2:
        st.markdown("""
        <div class='card' style='background-color: #fffaf0;'>
            <h3 style='color:#D7263D;'>🔥 Tteokbokki (떡볶이)</h3><p style='font-size: 1.25rem; color: #000000'><b>$6.99</b></p>
            <ul style='color:#333; font-size: 1.05rem;'>
                <li><b>Spicy</b> Korean rice cakes served in a cup</li>
                <li>Includes <b>1 Gimmari</b> (김말이, seaweed roll), cut into two pieces</li>
                <li>Want it spicier? <span style='color:#D7263D; font-weight:bold;'>Free Buldak (불닭) Sauce drizzle!</span> 🔥</li>
            </ul>
            <p style='font-size: 0.75rem; color: #000000'><b>Contains wheat, soy, fish, egg, sesame oil, and may contain traces of nuts and shellfish.</b></p>
        </div>
        """, unsafe_allow_html=True)

# ------------------ Dalgona Section ------------------
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://raw.githubusercontent.com/diziba213/Hyuever/main/dalgona.png", width=160)
    with col2:
        st.markdown("""
        <div class='card'>
            <h3 style='color:#D4A017;'>⭐ Dalgona (달고나)</h3><p style='font-size: 1.25rem; color: #000000'><b>$1.99</b></p>
            <ul style='color:#333; font-size: 1.05rem;'>
                <li>Traditional Korean sugar candy featured in <b>Squid Game</b> (오징어 게임)</li>
            </ul>
            <p style='font-size: 0.75rem; color: #000000'>⚠ Contains sugar. Manufactured in a facility that may process nuts.</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------ Heating Instructions ------------------
st.markdown("## ♨️ Heating Instructions")
st.markdown("""
<p style='font-size: 1.05rem;'>All items are stored at room temperature. For the best taste and to feel the warmth of Korea, <b style='color:#D4A017;'>microwave for 2 minutes and 30 seconds is <u>highly recommended</u></b>.</p>
""", unsafe_allow_html=True)



# ------------------ Payment Instructions ------------------
with st.container():
    st.markdown("## 💸 Payment via Zelle")

    st.markdown("""
    <p style='font-size: 1.05rem;'>
        Please complete your payment <b>in person</b> via <b>Zelle</b>.<br><br>
        Our staff will provide you with the Zelle ID at the stand.  
        Once sent, simply <b>show the confirmation screen</b> to confirm your order ✅
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 0.9rem; color: gray;'>
        *For your privacy and safety, we do not display any payment information online.
    </p>
    """, unsafe_allow_html=True)


# ------------------ Feedback Survey ------------------
st.markdown("## 📝 Quick Feedback")
st.markdown("<p style='font-size: 1.05rem;'>This survey is anonymous and takes just 30 seconds. Your feedback helps us improve!</p>", unsafe_allow_html=True)

emoji_options = ["😠", "😕", "😐", "🙂", "🤩"]

taste = st.radio("Taste", emoji_options, index=2, horizontal=True)
price = st.radio("Price", emoji_options, index=2, horizontal=True)
overall = st.radio("Overall Experience", emoji_options, index=2, horizontal=True)

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
