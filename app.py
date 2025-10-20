import streamlit as st
import streamlit.components.v1 as components

# --- Cấu hình trang ---
st.set_page_config(page_title="🥦 from broccoli 🥦", page_icon="💗", layout="centered")

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

# --- HTML + CSS + JS ---
heart_html = """
<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:250px;">
  <div class="heart" onclick="showMessage()"></div>
  <p id="msg" style="opacity:0; transform: translateY(20px); transition: all 1s ease; 
     color:#ba6fa0; font-family:'Segoe UI', sans-serif; font-size:18px; text-align:center; margin-top:25px;">
     🌷 Người đẹp 20/10 vui vẻ nha 💕
  </p>
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
  cursor: pointer;
  box-shadow: 0 0 20px rgba(255,182,193,0.6);
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

<script>
function showMessage() {
  var msg = document.getElementById("msg");
  msg.style.opacity = "1";
  msg.style.transform = "translateY(0)";
}
</script>
"""

# --- Hiển thị ---
components.html(heart_html, height=400)

# --- Chữ ký ---
st.markdown(
    """
    <p style='text-align:center; color:#8b5c87; font-family:"Segoe UI", sans-serif;'>
        💬 Code by <a href="https://streamlit.io/cloud" target="_blank" 
        style="color:#8b5c87; text-decoration:none;">tranthikimngan2005</a>
    </p>
    """,
    unsafe_allow_html=True
)
