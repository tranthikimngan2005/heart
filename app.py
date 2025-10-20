import streamlit as st

# --- Giao diện chính ---
st.set_page_config(page_title="🥦 from broccoli 🥦", page_icon="💝", layout="centered")
st.title(" ✨✨for you✨✨ ")
st.markdown("### Made with ❤️ bằng Python và Streamlit")

# --- Hiển thị hiệu ứng trái tim bằng CSS ---
heart_html = """
<style>
@keyframes heartbeat {
  0% { transform: scale(1); }
  25% { transform: scale(1.2); }
  40% { transform: scale(1); }
  60% { transform: scale(1.2); }
  100% { transform: scale(1); }
}
.heart {
  position: relative;
  width: 100px;
  height: 90px;
  margin: 50px auto;
  transform: rotate(-45deg);
  animation: heartbeat 1s infinite;
}
.heart::before,
.heart::after {
  content: "";
  position: absolute;
  width: 100px;
  height: 90px;
  background: radial-gradient(circle at 30% 30%, #ff5f6d, #ff0844);
  border-radius: 50%;
}
.heart::before {
  top: -50px;
  left: 0;
}
.heart::after {
  left: 50px;
  top: 0;
}
</style>
<div class="heart"></div>
"""

st.markdown(heart_html, unsafe_allow_html=True)

# --- Thêm lời chúc ---
st.write("💬 **happy women's dayyyy 💕")
st.write("🌷 Code by [tranthikimngan2005](https://streamlit.io/cloud)")
