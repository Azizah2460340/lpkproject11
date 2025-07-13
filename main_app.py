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

    # Contoh Senyawa: Alkohol
    st.subheader("🔍 Jelajahi Senyawa: Alkohol")
    col1, col2 = st.columns([1, 2])
    with col1:
        alkohol_img = Image.open("alkohol.jpg")  # Ganti dengan path gambar lokal kamu
        if st.button("Klik untuk lihat detail Alkohol"):
            st.session_state.page = 'alkohol'
        st.image(alkohol_img, caption="Senyawa Alkohol", use_column_width=True)
    with col2:
        st.write("Alkohol adalah senyawa organik dengan gugus -OH (hidroksil)...")

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
    question = st.sidebar.text_input("Tanya tentang senyawa (mis. alkohol):")
    if question:
        if "alkohol" in question.lower():
            st.sidebar.write("Alkohol memiliki gugus hidroksil (-OH) dan bersifat polar.")
        else:
            st.sidebar.write("Maaf, informasi senyawa belum tersedia.")

def show_about():
    st.title("Tentang Kami 👨‍💻")
    st.markdown("""
    **Developer:**  
    - Nama: [Nama Kamu]  
    - Email: nama@email.com  
    - Universitas: Universitas Kimia Hebat

    Kami membuat aplikasi ini untuk mempermudah pembelajaran kimia dengan cara yang interaktif dan menyenangkan.
    """)

def show_rating():
    st.title("Sebelum Keluar, Beri Rating Aplikasi Ini ⭐")
    rating = st.slider("Seberapa bermanfaat aplikasi ini?", 1, 5)
    feedback = st.text_area("Masukan atau saran:")
    if st.button("Kirim"):
        st.success("Terima kasih atas feedback Anda! 🙏")
        time.sleep(2)
        st.stop()

# ------------- UI & PAGE CONTROL --------------
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar Navigasi
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
if st.session_state.page == 'alkohol':
    show_alkohol()
elif page == "Beranda":
    show_home()
elif page == "About Us":
    show_about()
elif page == "Chatbot":
    show_chatbot()
elif page == "Keluar":
    show_rating()

