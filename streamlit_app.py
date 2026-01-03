import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Happy Birthday Nurul 💖", layout="centered")

# Fungsi load file
def load_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = load_file("background.jpg")
music = load_file("lover.mp3")

html_code = f"""
<style>
body {{
    margin:0;
    background:url("data:image/jpg;base64,{bg}") center/cover no-repeat fixed;
    font-family:'Pacifico',cursive;
}}
.paper {{
    max-width:760px;
    margin:40px auto;
    padding:40px;
    background:#c9a36a;
    background-image:radial-gradient(rgba(0,0,0,.15) 1px,transparent 0);
    background-size:6px 6px;
    border-radius:14px;
    box-shadow:0 12px 30px rgba(0,0,0,.4);
    color:#4b2e1f;
    font-size:20px;
    line-height:1.8;
}}
.signature {{
    text-align:right;
    margin-top:25px;
}}
.float {{
    position:fixed;
    top:-50px;
    font-size:24px;
    animation:fall linear forwards;
    pointer-events:none;
}}
@keyframes fall {{
    to {{
        transform:translateY(110vh) rotate(360deg);
        opacity:0;
    }}
}}
</style>

<audio autoplay loop>
  <source src="data:audio/mp3;base64,{music}" type="audio/mp3">
</audio>

<div class="paper">
<p>
Halooo Nurul sayang cintaku duniakuuu...<br><br>

Selamat ulang tahun yaa cantik, aku sayaang banget sama kamu,
aku harap apa yang kamu ingin capai segera kamu dapatkan.
Terimakasih banyak ya sayang udah nemenin aku kurang lebih setengah tahun ini,
aku harap kamu bakal terus sama aku kedepannya dan aku jadi orang yg nemenin kamu
disaat kamu susah, senang, dan dikondisi apapun.<br><br>

Semoga kita saling tumbuh dan berkembang menjadi lebih baik ya sayangku.
Aku janji aku bakal usahakan yang terbaik buat kamu sayang.
Semangaat terus kuliahnya ya meski cape dan banyak tugas,
jadiin aku tempat kamu cerita yang nyamam ya sayang.
Jangan takut-takut terus buat masa depan kamu ya sayang,
bagi cerita dan masa depan kamu sama aku biar kita bangun masa depan
yang lebih cerah dan sukses ya sayang.<br><br>

Makasii buat semuanya ya sayaang,
wish u all the best &lt;3

<div class="signature">
Salam hangat,<br>Gilfan
</div>
</p>
</div>

<script>
setInterval(() => {{
  const e = document.createElement("div");
  e.className = "float";
  e.innerHTML = ["🌸","🌼","🌺","🌷","💐","❤️","💖","💗"][Math.floor(Math.random()*8)];
  e.style.left = Math.random()*100 + "vw";
  e.style.animationDuration = (3 + Math.random()*4) + "s";
  document.body.appendChild(e);
  setTimeout(() => e.remove(), 7000);
}}, 300);
</script>
"""

st.markdown(html_code, unsafe_allow_html=True)
