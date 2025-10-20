import streamlit as st

# --- Giao diện chính ---
st.set_page_config(page_title="🥦 from broccoli 🥦", page_icon="💝", layout="centered")
# --- Tiêu đề ---
st.markdown(
    """
    <h1 style='text-align:center; font-family:"Segoe UI", sans-serif;'>
        ✨✨for you✨✨
    </h1>
    <h2 style='text-align:center; color:#d47fa6; font-family:"Segoe UI", sans-serif;'>
        💗 little heart for you 💗
    </h2>
    """,
    unsafe_allow_html=True
)

# --- CSS & HTML trái tim ---
heart_html = """
<div style="display:flex; justify-content:center; align-items:center; height:200px;">
  <div class="heart"></div>
</div>

<style>
@keyframes softbeat {
  0%   { transform: scale(1) rotate(-45deg); }
  30%  { transform: scale(1.08) rotate(-45deg); }
  60%  { transform: scale(0.97) rotate(-45deg); }
  100% { transform: scale(1) rotate(-45deg); }
}

.heart {
  position: relative;
  width: 100px;
  height: 90px;
  transform: rotate(-45deg);
  background: radial-gradient(circle at 30% 30%, #f8c8dc, #f2a2b6);
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
</style>
"""

# --- Hiển thị trái tim ---
st.markdown(heart_html, unsafe_allow_html=True)

# --- Lời nhắn ---
st.markdown(
    """
    <p style='text-align:center; color:#ba6fa0; font-family:"Segoe UI", sans-serif; font-size:18px;'>
        🌷 all good things come to you💕
    </p>
    <p style='text-align:center; color:#8b5c87;'>
        💬 Code by <a href="https://streamlit.io/cloud" target="_blank" style="color:#8b5c87; text-decoration:none;">tranthikimngan2005</a>
    </p>
    """,
    unsafe_allow_html=True
)



st.write("💬 **happy women's dayyyy 💕")
st.write("🌷 Code by [tranthikimngan2005](https://streamlit.io/cloud)")
