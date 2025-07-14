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

    question = st.text_input("Tanyakan sesuatu tentang senyawa kimia (misal: kepolaran ester):")

    if question:
        q = question.lower()

        # Alkohol
        if "alkohol" in q:
            if "kepolaran" in q:
                st.success("Alkohol bersifat sangat polar karena memiliki gugus –OH dan membentuk ikatan hidrogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi alkohol: –OH.")
            elif "titik" in q:
                st.success("Titik leleh/didih alkohol: –114 °C / ~78 °C (etanol).")
            elif "fakta" in q:
                st.success("Gliserol dan etanol dihasilkan dari fermentasi.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")
            else:
                st.info("Alkohol mengandung gugus –OH dan bersifat sangat polar.")

        # Amina
        elif "amina" in q:
            if "kepolaran" in q:
                st.success("Amina bersifat polar dan bersifat basa lemah.")
            elif "gugus" in q:
                st.success("Gugus fungsi amina: –NH₂ / –NHR.")
            elif "titik" in q:
                st.success("Titik leleh/didih amina: –75 °C / ~184 °C (anilin).")
            elif "fakta" in q:
                st.success("Amina termasuk senyawa alkaloid seperti nikotin dan morfin.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")
            else:
                st.info("Amina adalah senyawa basa dengan gugus –NH₂.")

        # Ester
        elif "ester" in q:
            if "kepolaran" in q:
                st.success("Ester bersifat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi ester: –COO–R.")
            elif "titik" in q:
                st.success("Titik leleh/didih ester: –24 °C / ~77 °C (etil asetat).")
            elif "fakta" in q:
                st.success("Ester memberikan aroma buah seperti pisang dan stroberi.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # Asam Karboksilat
        elif "asam karboksilat" in q:
            if "kepolaran" in q:
                st.success("Asam karboksilat sangat polar karena membentuk ikatan hidrogen.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –COOH.")
            elif "titik" in q:
                st.success("Titik leleh/didih: ~16 °C / ~100 °C (asam format).")
            elif "fakta" in q:
                st.success("Asam sitrat ditemukan pada jeruk, dan asam malat pada apel.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # halida asam
        elif "halida asam" in q:
            if "kepolaran" in q:
                st.success("Halida asam cukup polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –COX.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –80 °C / ~50–100 °C.")
            elif "fakta" in q:
                st.success("Halida asam merupakan turunan sintetik.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        
        # amida
        elif "amida" in q:
            if "kepolaran" in q:
                st.success("Amida sangat polar karena adanya ikatan hidrogen.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –CONH₂.")
            elif "titik" in q:
                st.success("Titik leleh/didih: ~132 °C / ~221 °C (acetamida).")
            elif "fakta" in q:
                st.success("Amida adalah bagian dari ikatan peptida dalam protein.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        
        # nitril
        elif "nitril" in q:
            if "kepolaran" in q:
                st.success("Nitril bersifat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –C≡N.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –83 °C / ~82 °C (etanonitril).")
            elif "fakta" in q:
                st.success("Nitril termasuk senyawa metabolik sekunder.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        
        # aldehida
        elif "aldehida" in q:
            if "kepolaran" in q:
                st.success("Aldehida bersifat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –CHO.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –80 °C / ~21 °C (asetaldehida).")
            elif "fakta" in q:
                st.success("Aldehida memberi aroma pada daun, seperti cinnamaldehid pada kayu manis.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        
        # keton
        elif "keton" in q:
            if "kepolaran" in q:
                st.success("Keton bersifat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –CO–R₂.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –95 °C / ~56 °C (aseton).")
            elif "fakta" in q:
                st.success("Keton termasuk dalam senyawa terpenoid dan steroid tanaman.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # tiol`           
        elif "tiol" in q:
            if "kepolaran" in q:
                st.success("Tiol sedikit polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –SH.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –86 °C / ~97 °C (etanotiol).")
            elif "fakta" in q:
                st.success("Tiol menghasilkan bau khas seperti pada bawang.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # arene
        elif "arene" in q:
            if "kepolaran" in q:
                st.success("Arene bersifat nonpolar hingga moderat.")
            elif "gugus" in q:
                st.success("Gugus fungsi: C₆H₆ dan turunannya (cincin aromatik).")
            elif "titik" in q:
                st.success("Titik leleh/didih: ~6 °C / ~80 °C (benzena).")
            elif "fakta" in q:
                st.success("Arene terdapat dalam senyawa fenolik dan flavonoid.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # alkena
        elif "alkena" in q:
            if "kepolaran" in q:
                st.success("Alkena bersifat nonpolar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –C=C–.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –169 °C / –104 °C (etena).")
            elif "fakta" in q:
                st.success("Etilen merupakan hormon pematangan buah.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # alkuna
        elif "alkuna" in q:
            if "kepolaran" in q:
                st.success("Alkuna bersifat nonpolar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –C≡C–.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –84 °C / –75 °C (etuna).")
            elif "fakta" in q:
                st.success("Alkuna jarang ditemukan secara alami, biasanya pada senyawa kompleks.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # alkana
        elif "alkana" in q:
            if "kepolaran" in q:
                st.success("Alkana sangat nonpolar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: – (tidak memiliki gugus fungsi khusus).")
            elif "titik" in q:
                st.success("Titik leleh/didih: –183 °C / ~36 °C (pentana).")
            elif "fakta" in q:
                st.success("Alkana merupakan hidrokarbon sederhana dalam tanaman.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # eter
        elif "eter" in q:
            if "kepolaran" in q:
                st.success("Eter bersifat moderat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –O–.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –116 °C / ~35 °C (dietil eter).")
            elif "fakta" in q:
                st.success("Eter ditemukan dalam minyak atsiri seperti terpen eterik.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # alkil halida
        elif "alkil halida" in q:
            if "kepolaran" in q:
                st.success("Alkil halida bersifat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –R–X.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –123 °C / ~61 °C (kloroform).")
            elif "fakta" in q:
                st.success("Alkil halida merupakan senyawa sintetik.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        # nitro
        elif "nitro" in q:
            if "kepolaran" in q:
                st.success("Nitro bersifat sangat polar.")
            elif "gugus" in q:
                st.success("Gugus fungsi: –NO₂.")
            elif "titik" in q:
                st.success("Titik leleh/didih: –29 °C / ~101 °C (nitrometana).")
            elif "fakta" in q:
                st.success("Senyawa nitro jarang ditemukan di alam, lebih banyak sebagai senyawa sintetik.")
            elif "video" in q:
                st.success("https://www.youtube.com/watch?v=tvES-hSZKDY")

        else:
            st.warning("Maaf, senyawa tersebut belum tersedia atau belum dikenali.")

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
