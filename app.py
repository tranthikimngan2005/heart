import streamlit as st

# --- Giao diện chính ---
st.set_page_config(page_title="🥦 from broccoli 🥦", page_icon="💝", layout="centered")
st.title(" ✨✨for you✨✨ ")

# --- Tiêu đề ---
st.markdown(
    """
    <h2 style='text-align:center; color:#d47fa6; font-family:"Segoe UI", sans-serif;'>
        💗 Một trái tim nhỏ gửi đến bạn 💗
    </h2>
    """,
    unsafe_allow_html=True
)

# --- CSS trái tim pastel đập nhẹ nhàng ---
heart_html = """
<style>
@keyframes softbeat {
  0%   { transform: scale(1); }
  30%  { transform: scale(1.08); }
  60%  { transform: scale(0.98); }
  100% { transform: scale(1); }
}

.heart {
  position: relative;
  width: 100px;
  height: 90px;
  margin: 60px auto;
  transform: rotate(-45deg);
  animation: softbeat 2.5s ease-in-out infinite;
}

.heart::before,
.heart::after {
  content: "";
  position: absolute;
  width: 100px;
  height: 90px;
  background: radial-gradient(circle at 30% 30%, #f8c8dc, #f2a2b6);
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

body {
  background-color: #fff8fa;
}
</style>
<div class="heart"></div>
"""

# --- Hiển thị trái tim ---
st.markdown(heart_html, unsafe_allow_html=True)


# --- Thêm lời chúc ---
st.write("💬 **happy women's dayyyy 💕")
st.write("🌷 Code by [tranthikimngan2005](https://streamlit.io/cloud)")
