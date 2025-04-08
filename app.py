import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Hyuever",
    page_icon="🍜",
    layout="centered"
)

# --- Section 1: Welcome ---
st.markdown("## 🍜 Welcome to Hyuever")
st.write("Delicious Korean street food made by **Hyu**, for **whoever**. Come taste the warmth and spice!")

# --- Section 2: Menu ---
st.markdown("## 🥢 Our Menu")

st.markdown("### 🍜 Cupbokki - $6.99")
st.write("- Spicy rice cakes served in a cup.")
st.write("- Includes **1 Gimmari**, cut into two pieces.")
st.write("- Want it hotter? Ask for a **free drizzle of Buldak sauce**.")

st.markdown("### 🍬 Dalgona - $1.99")
st.write("- Traditional Korean sugar candy.")
st.write("- Crushed pieces available as samples.")

st.markdown("### 🎉 Combo Set - $7.99")
st.write("Includes **Cupbokki + Dalgona**. Save $1!")

# --- Section 3: Heating Instructions ---
st.markdown("## ♨️ Heating Instructions")
st.write("""
All items are stored at **room temperature**.
For the best taste, please microwave for **2 minutes and 30 seconds** before eating.
""")

# --- Section 4: Vote for the Next Item ---
st.markdown("## 🗳️ Vote for the Next Item!")

vote = st.radio(
    "What should we serve next?",
    ["Hotteok (호떡)", "Kimbap (김밥)", "Fried Mandu (군만두)"]
)

if st.button("Vote"):
    st.success(f"Thanks for voting for {vote}!")

# --- Section 5: Instagram Follow ---
st.markdown("## 📱 Follow Us on Instagram")
st.write("Stay connected with the Hyuever journey!")
st.write("🔗 Coming soon: [@hyuever.food](https://instagram.com/hyuever.food)")

# --- Section 6 (Optional): Korean Food Culture ---
with st.expander("🇰🇷 Learn about Korean Street Food Culture"):
    st.write("Cupbokki, Dalgona, and Gimmari are beloved treats from Korean street vendors.")
    st.write("They’re comforting, affordable, and made to be enjoyed by everyone—just like at Hyuever.")
