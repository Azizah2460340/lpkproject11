import streamlit as st
from PIL import Image
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="O-Kimiaku",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)
    
# ------------- FUNGSI --------------
def show_home():
    st.title("Selamat Datang di O-KIMIAKU 👩‍🔬🧪")

    st.markdown("""
    **O-KIMIAKU** adalah aplikasi pembelajaran interaktif kimia yang memberikan informasi penting tentang senyawa kimia, seperti:
    - ✅ Tatanama Senyawa
    - 🌡️ Titik Didih dan Titik Leleh
    - 🤓 Fun Fact Kimia
    - ⚖️ Kepolaran
    - 🧬 Rumus Kimia

    Klik gambar senyawa untuk mengetahui detailnya lebih lanjut!
    """)

    st.subheader("🔍 Pilih Senyawa:")

    if st.button("🧪 Alkohol"):
        st.session_state.page = 'alkohol'

    if st.button("🧬 Amina"):
        st.session_state.page = 'amina'

def show_alkohol():
    st.title("Detail Senyawa: Alkohol")

    st.markdown("""
    **Tatanama:** Etanol (Ethanol)  
    **Rumus Kimia:** C₂H₅OH  
    **Titik Didih:** 78.37°C  
    **Titik Leleh:** -114.1°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Etanol dapat digunakan sebagai bahan bakar ramah lingkungan!

    🔗 [Tonton Penjelasan Alkohol di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)
    """)

def show_chatbot():
    st.title("💬 Chatbot O-KIMIAKU")

    question = st.text_input("Tanyakan sesuatu tentang alkohol atau amina:")

    if question:
        q = question.lower()

        # Alkohol
        if "alkohol" in q:
            if "kepolaran" in q:
                st.success("Alkohol bersifat polar karena memiliki gugus -OH.")
            elif "rumus" in q:
                st.success("Rumus kimia alkohol (etanol) adalah C₂H₅OH.")
            elif "titik didih" in q:
                st.success("Titik didih alkohol adalah 78.37°C.")
            elif "titik leleh" in q or "titik meleh" in q:
                st.success("Titik leleh alkohol adalah -114.1°C.")
            elif "fun fact" in q or "fakta" in q:
                st.success("Etanol bisa digunakan sebagai bahan bakar ramah lingkungan!")
            else:
                st.info("Alkohol adalah senyawa dengan gugus -OH dan bersifat polar.")

        # Amina
        elif "amina" in q:
            if "kepolaran" in q:
                st.success("Amina bersifat polar karena mengandung gugus -NH₂.")
            elif "rumus" in q:
                st.success("Rumus kimia amina (metilamina) adalah CH₃NH₂.")
            elif "titik didih" in q:
                st.success("Titik didih amina adalah -6.3°C.")
            elif "titik leleh" in q or "titik meleh" in q:
                st.success("Titik leleh amina adalah -93.5°C.")
            elif "fun fact" in q or "fakta" in q:
                st.success("Amina digunakan dalam produksi obat dan pewarna.")
            else:
                st.info("Amina adalah senyawa dengan gugus -NH₂ yang bersifat polar.")
        
        else:
            st.warning("Maaf, saya hanya tahu tentang alkohol dan amina untuk saat ini.")

def show_about():
    st.title("Tentang Kami 👨‍💻")
    st.markdown("""
    **Developer:**  
    KELOMPOK 11 KELAS 1C
    1. Nama:  Azizah Putri Azzahra (2460340)
    2. Nama:  Nadifah (2460340)
    3. Nama:  NAdifah (2460340)
    4. Nama:  NAdifah (2460340)
       
    Kami membuat aplikasi ini untuk mempermudah pembelajaran kimia dengan cara yang interaktif dan menyenangkan.
    """)

def show_rating():
    st.title("Sebelum Keluar, Beri Rating Aplikasi Ini ⭐")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
       st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

# ------------- UI & PAGE CONTROL --------------
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar Navigasi TANPA LINGKARAN
st.sidebar.title("📚 Navigasi")

if st.sidebar.button("🏠 Beranda"):
    st.session_state.page = 'home'

if st.sidebar.button("👥 About Us"):
    st.session_state.page = 'about'

if st.sidebar.button("💬Chatbot"):
    st.session_state.page = 'chatbot'
    
if st.sidebar.button(" ⭐Rating"):
    st.session_state.page = 'rating'
    
# Routing
if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'alkohol':
    show_alkohol()
elif st.session_state.page == 'about':
    show_about()
elif st.session_state.page == 'chatbot':
    show_chatbot()
elif st.session_state.page == 'rating':
    show_rating()
elif st.session_state.page == 'amina':
    show_amina()
