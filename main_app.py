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

    st.subheader("🔍 Jelajahi Senyawa:")

# Ambil query param agar klik link bisa ganti halaman
query_params = st.query_params()
if 'page' in query_params:
    st.session_state.page = query_params['page'][0]

    cards_html = """
    <style>
    .card-container {
      display: flex;
      gap: 20px;
      justify-content: start;
      flex-wrap: wrap;
    }
    .card {
      position: relative;
      width: 300px;
      height: 180px;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      cursor: pointer;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      text-decoration: none;
      color: white;
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }
    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    .card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(70%);
      transition: filter 0.3s ease;
    }
    .card:hover img {
      filter: brightness(100%);
    }
    .card-title {
      position: absolute;
      bottom: 15px;
      left: 20px;
      font-size: 24px;
      font-weight: bold;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
    }
    </style>

    <div class="card-container">
      <a href="?page=alkohol" class="card">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Ethanol-2D-flat.svg/320px-Ethanol-2D-flat.svg.png" alt="Alkohol">
        <div class="card-title">Alkohol</div>
      </a>
      <a href="?page=amina" class="card">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Amines-structure-1.svg/320px-Amines-structure-1.svg.png" alt="Amina">
        <div class="card-title">Amina</div>
      </a>
      <!-- Tambah kartu lain di sini -->
    </div>
    """

    st.markdown(cards_html, unsafe_allow_html=True)

# Routing halaman
page = st.session_state.page
if page == 'home':
    show_home()
elif page == 'alkohol':
    show_alkohol()
elif page == 'amina':
    show_amina()
elif page == 'chatbot':
    show_chatbot()
elif page == 'about':
    show_about()
elif page == 'rating':
    show_rating()

    # Tampilkan 2 senyawa dalam satu baris
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧪 Alkohol")
        alkohol_img = Image.open("alkohol.jpg")
        if st.button("Lihat Detail Alkohol"):
            st.session_state.page = 'alkohol'
        st.image(alkohol_img, caption="Alkohol", use_column_width=True)

    with col2:
        st.markdown("### 🧪 Amina")
        amina_img = Image.open("amina.jpg")
        if st.button("Lihat Detail Amina"):
            st.session_state.page = 'amina'
        st.image(amina_img, caption="Amina", use_column_width=True)

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
def show_amina():
    st.title("🧪 Detail Senyawa: Amina")

    col1, col2 = st.columns([1, 2])

    with col1:
        amina_img = Image.open("amina.jpg")
        st.image(amina_img, caption="Struktur Amina", use_column_width=True)

    with col2:
        st.markdown("""
        ### 📘 Informasi Umum
        - **Tatanama IUPAC:** Metilamina, Dimetilamina, dll.
        - **Rumus Umum:** R-NH₂ (amina primer)
        - **Jenis Ikatan:** Kovalen Polar
        - **Kelas:** Amina primer, sekunder, tersier

        ### 🌡️ Sifat Fisik
        - **Bau:** Menyengat seperti ikan busuk
        - **Kelarutan:** Larut dalam air (jika berat molekul rendah)

        ### ⚛️ Kepolaran
        - Amina bersifat **polar** dan dapat membentuk ikatan hidrogen.

        ### 🤓 Fun Fact
        - Amina banyak ditemukan pada obat-obatan, pestisida, dan bahan biologis!

        ### 🎥 Video Pembelajaran
        🔗 [Tonton Penjelasan Amina di YouTube](https://www.youtube.com/watch?v=dFOVrxzS5pk)
        """)

def show_chatbot():
    st.title("💬 Chatbot O-KIMIAKU")

    question = st.text_input("Tanya tentang senyawa kimia (contoh: alkohol):")
    if question:
        if "alkohol" in question.lower():
            st.success("✅ Alkohol memiliki gugus hidroksil (-OH), bersifat polar, dan digunakan sebagai pelarut.")
        else:
            st.warning("❗ Maaf, informasi senyawa tersebut belum tersedia.")

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
