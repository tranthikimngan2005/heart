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

heart_html = """
<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:250px;">
  <div class="heart" onclick="showMessage()"></div>
  <p id="msg" style="opacity:0; transition: opacity 1.5s ease; 
     color:#ba6fa0; font-family:'Segoe UI', sans-serif; font-size:18px; text-align:center; margin-top:25px;">
     🌷 Người đẹp 20/10 vuôi vỏe 💕
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

<script>
function showMessage() {
  var msg = document.getElementById("msg");
  msg.style.opacity = "1";
}
</script>
"""

# --- Hiển thị ---
st.markdown(heart_html, unsafe_allow_html=True)

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
