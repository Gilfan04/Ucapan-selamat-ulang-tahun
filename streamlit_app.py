import streamlit as st
import time
import random

st.set_page_config(page_title="Happy Birthday 💖", layout="centered")

st.title("🎉 Selamat Ulang Tahun 🎉")
st.write("")

text = (
    "Halooo Nurul sayang cintaku duniakuuu...\n\n"
    "Selamat ulang tahun yaa cantik, aku sayaang banget sama kamu, "
    "aku harap apa yang kamu ingin capai segera kamu dapatkan.\n\n"
    "Terimakasih banyak ya sayang udah nemenin aku kurang lebih setengah tahun ini, "
    "aku harap kamu bakal terus sama aku kedepannya dan aku jadi orang yg nemenin kamu "
    "disaat kamu susah, senang, dan dikondisi apapun.\n\n"
    "Semoga kita saling tumbuh dan berkembang menjadi lebih baik ya sayangku. "
    "Aku janji aku bakal usahakan yang terbaik buat kamu sayang.\n\n"
    "Semangaat terus kuliahnya ya meski cape dan banyak tugas, "
    "jadiin aku tempat kamu cerita yang nyaman ya sayang.\n\n"
    "Jangan takut-takut terus buat masa depan kamu ya sayang, "
    "bagi cerita dan masa depan kamu sama aku biar kita bangun masa depan "
    "yang lebih cerah dan sukses ya sayang.\n\n"
    "Makasii buat semuanya ya sayaang,\n"
    "wish u all the best <3\n\n"
    "Salam hangat,\n"
    "Gilfan"
)

# efek mengetik
placeholder = st.empty()
current_text = ""

for char in text:
    current_text += char
    placeholder.text(current_text)
    time.sleep(0.02)

st.write("")
st.success("🎂 Selamat ulang tahun, semoga selalu bahagia 💐")

# animasi emoji sederhana
for _ in range(25):
    st.write(random.choice(["❤️", "💖", "💗", "🌸", "💐", "✨"]))
    time.sleep(0.08)
