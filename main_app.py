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
    
# Membuat baris tombol horizontal
   cols = st.columns(5)
     with cols[0]:
         if st.button("🍷 Alkohol"):
            st.session_state.page = 'alkohol'
         if st.button("🕸️ Benzena"):
            st.session_state.page = 'benzena'
         if st.button("🌿 Fenol"):
            st.session_state.page = 'fenol'
         if st.button("🧪 Amina"):
            st.session_state.page = 'amina'
    with cols[1]:
         if st.button("🔬 Amida"):
            st.session_state.page = 'amida'
         if st.button("🧫 Aldehida"):
            st.session_state.page = 'aldehida'
    if st.button("⚡ Nitro"):
        st.session_state.page = 'nitro'
    if st.button("🧭 Nitril"):
        st.session_state.page = 'nitril'
with cols[2]:
    if st.button("🧬 Alkana"):
        st.session_state.page = 'alkana'
    if st.button("🌱 Alkena"):
        st.session_state.page = 'alkena'
    if st.button("🔥 Alkuna"):
        st.session_state.page = 'alkuna'
    if st.button("🍞 Karbohidrat"):
        st.session_state.page = 'karbohidrat'
with cols[3]:
    if st.button("🎯 Keton"):
        st.session_state.page = 'keton'
    if st.button("🧴 Ester"):
        st.session_state.page = 'ester'
    if st.button("💧 Eter"):
        st.session_state.page = 'eter'
    if st.button("🍗 Protein"):
        st.session_state.page = 'protein'
with cols[4]:
    if st.button("🧂 Asam Halida"):
        st.session_state.page = 'asam_halida'
    if st.button("🍋 Asam Karboksilat"):
        st.session_state.page = 'asam_karboksilat'
    if st.button("🔌 Alkil Halida"):
        st.session_state.page = 'alkil_halida'
    if st.button("🛢️ Lemak dan Minyak"):
        st.session_state.page = 'lemak_dan_minyak'

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
    st.title("Detail Senyawa: Amina")
    st.markdown("""
    **Tatanama:** Anilin  
    **Gugus Fungsi:** –NH₂  
    **Titik Didih:** ~184°C  
    **Titik Leleh:** –75°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Amina banyak ditemukan dalam alkaloid seperti nikotin dan morfin.

    🔗 [Tonton Penjelasan Amina di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)
def show_ester():
    st.title("Detail Senyawa: Ester")

    st.markdown("""
    **Tatanama:** Etil Asetat  
    **Gugus Fungsi:** –COO–R  
    **Titik Didih:** ~77°C  
    **Titik Leleh:** –24°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Ester memberikan aroma buah seperti pisang dan stroberi.

    🔗 [Tonton Penjelasan Ester di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_halida_asam():
    st.title("Detail Senyawa: Halida Asam")

    st.markdown("""
    **Tatanama:** -  
    **Gugus Fungsi:** –COX  
    **Titik Didih:** ~50–100°C  
    **Titik Leleh:** –80°C  
    **Kepolaran:** Cukup polar  
    **Fun Fact:** Merupakan turunan sintetik dari asam karboksilat.

    🔗 [Tonton Penjelasan Halida Asam di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_amida():
    st.title("Detail Senyawa: Amida")

    st.markdown("""
    **Tatanama:** Acetamida  
    **Gugus Fungsi:** –CONH₂  
    **Titik Didih:** ~221°C  
    **Titik Leleh:** ~132°C  
    **Kepolaran:** Sangat polar (H-bond)  
    **Fun Fact:** Amida menyusun ikatan peptida pada protein.

    🔗 [Tonton Penjelasan Amida di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_nitril():
    st.title("Detail Senyawa: Nitril")

    st.markdown("""
    **Tatanama:** Etanonitril  
    **Gugus Fungsi:** –C≡N  
    **Titik Didih:** ~82°C  
    **Titik Leleh:** –83°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Digunakan dalam sintesis senyawa metabolik sekunder.

    🔗 [Tonton Penjelasan Nitril di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_aldehida():
    st.title("Detail Senyawa: Aldehida")

    st.markdown("""
    **Tatanama:** Asetaldehida  
    **Gugus Fungsi:** –CHO  
    **Titik Didih:** ~21°C  
    **Titik Leleh:** –80°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Memberikan aroma khas pada daun, seperti cinnamaldehid pada kayu manis.

    🔗 [Tonton Penjelasan Aldehida di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_keton():
    st.title("Detail Senyawa: Keton")

    st.markdown("""
    **Tatanama:** Aseton  
    **Gugus Fungsi:** –CO–R₂  
    **Titik Didih:** ~56°C  
    **Titik Leleh:** –95°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Keton termasuk senyawa penting dalam terpenoid dan steroid tanaman.

    🔗 [Tonton Penjelasan Keton di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_tiol():
    st.title("Detail Senyawa: Tiol")

    st.markdown("""
    **Tatanama:** Etanotiol  
    **Gugus Fungsi:** –SH  
    **Titik Didih:** ~97°C  
    **Titik Leleh:** –86°C  
    **Kepolaran:** Sedikit polar  
    **Fun Fact:** Menghasilkan bau khas seperti bawang.

    🔗 [Tonton Penjelasan Tiol di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_arene():
    st.title("Detail Senyawa: Arene")

    st.markdown("""
    **Tatanama:** Benzena  
    **Gugus Fungsi:** C₆H₆ & Turunan  
    **Titik Didih:** ~80°C  
    **Titik Leleh:** ~6°C  
    **Kepolaran:** Nonpolar – Moderat  
    **Fun Fact:** Digunakan dalam senyawa fenolik dan flavonoid.

    🔗 [Tonton Penjelasan Arene di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_alkena():
    st.title("Detail Senyawa: Alkena")

    st.markdown("""
    **Tatanama:** Etena  
    **Gugus Fungsi:** –C=C–  
    **Titik Didih:** –104°C  
    **Titik Leleh:** –169°C  
    **Kepolaran:** Nonpolar  
    **Fun Fact:** Etilen adalah hormon pematangan buah.

    🔗 [Tonton Penjelasan Alkena di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_alkuna():
    st.title("Detail Senyawa: Alkuna")

    st.markdown("""
    **Tatanama:** Etuna  
    **Gugus Fungsi:** –C≡C–  
    **Titik Didih:** –75°C  
    **Titik Leleh:** –84°C  
    **Kepolaran:** Nonpolar  
    **Fun Fact:** Jarang ditemukan di alam, biasanya pada senyawa kompleks.

    🔗 [Tonton Penjelasan Alkuna di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_alkana():
    st.title("Detail Senyawa: Alkana")

    st.markdown("""
    **Tatanama:** Pentana  
    **Gugus Fungsi:** –  
    **Titik Didih:** ~36°C  
    **Titik Leleh:** –183°C  
    **Kepolaran:** Sangat nonpolar  
    **Fun Fact:** Merupakan hidrokarbon sederhana dalam tanaman.

    🔗 [Tonton Penjelasan Alkana di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_eter():
    st.title("Detail Senyawa: Eter")

    st.markdown("""
    **Tatanama:** Dietil Eter  
    **Gugus Fungsi:** –O–  
    **Titik Didih:** ~35°C  
    **Titik Leleh:** –116°C  
    **Kepolaran:** Moderat polar  
    **Fun Fact:** Terdapat dalam minyak atsiri seperti terpen eterik.

    🔗 [Tonton Penjelasan Eter di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_alkil_halida():
    st.title("Detail Senyawa: Alkil Halida")

    st.markdown("""
    **Tatanama:** Kloroform  
    **Gugus Fungsi:** –R–X  
    **Titik Didih:** ~61°C  
    **Titik Leleh:** –123°C  
    **Kepolaran:** Polar  
    **Fun Fact:** Merupakan senyawa sintetik yang sering digunakan di laboratorium.

    🔗 [Tonton Penjelasan Alkil Halida di YouTube](https://www.youtube.com/watch?v=tvES-hSZKDY)
    """)

def show_nitro():
    st.title("Detail Senyawa: Nitro")

    st.markdown("""
    **Tatanama:** Nitrometana  
    **Gugus Fungsi:** –NO₂  
    **Titik Didih:** ~101°C  
    **Titik Leleh:** –29°C  
    **Kepolaran:** Sangat polar  
    **Fun Fact:** Senyawa nitro jarang ditemukan di alam, kebanyakan dibuat secara sintetik.

    🔗 [Tonton Penjelasan Nitro di YouTube](https://www.youtube.com/watch?v=tvES
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

        # tiol          
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
1. Nama : Azizah Putri Azzahra (2460340)  
2. Nama : Nadifah Adya Anggita (2460
3. Nama : Raudhatul Dahlia (2460493)
4. Nama : Zahira Dwi Safitri (2460542) 
   
Kami membuat aplikasi ini untuk mempermudah pembelajaran kimia dengan cara yang interaktif.
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

if st.sidebar.button("💬 Chatbot"):
    st.session_state.page = 'chatbot'
    
if st.sidebar.button(" ⭐ Rating"):
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
elif st.session_state.page == 'alkil halida':
    show_alkil_halida()
elif st.session_state.page == 'eter':
    show_eter()
elif st.session_state.page == 'amida':
    show_amida()
elif st.session_state.page == 'nitril':
    show_nitril()
elif st.session_state.page == 'aldehida':
    show_aldehida()
elif st.session_state.page == 'nitro':
    show_nitril()
elif st.session_state.page == 'keton':
    show_keton()
elif st.session_state.page == 'asam halida':
    show_nitro()
elif st.session_state.page == 'ester':
    show_ester()
elif st.session_state.page == 'tiol':
    show_tiol()
elif st.session_state.page == 'alkana':
    show_alkana()
elif st.session_state.page == 'alkena':
    show_alkena()
elif st.session_state.page == 'alkuna':
    show_alkuna()
elif st.session_state.page == 'fenol':
    show_fenol()
elif st.session_state.page == 'benzena':
    show_benzena()









