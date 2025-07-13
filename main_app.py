import streamlit as st
import pandas as pd
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="O-Kimiaku",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Data senyawa kimia
chemical_data = {
    "Alcohol": {
        "name": "Alkohol",
        "formula": "R-OH",
        "boiling_point": "Tergantung rantai (Metanol: 64.7°C, Etanol: 78.37°C)",
        "melting_point": "Tergantung rantai (Metanol: -97.6°C, Etanol: -114.1°C)",
        "polarity": "Polar",
        "fun_fact": "Etanol adalah alkohol yang terdapat dalam minuman beralkohol",
        "image": "alcohol.png",
        "youtube_link": "https://www.youtube.com/watch?v=7ATl2vgPYBs"
    },
    "Aldehyde": {
        "name": "Aldehida",
        "formula": "R-CHO",
        "boiling_point": "Bervariasi (Formaldehida: -19°C)",
        "melting_point": "Bervariasi (Formaldehida: -92°C)",
        "polarity": "Polar",
        "fun_fact": "Formaldehida digunakan dalam pengawetan spesimen biologis",
        "image": "aldehyde.png",
        "youtube_link": "https://www.youtube.com/watch?v=Nq9xhxFXot4"
    }
}

# Fungsi untuk halaman beranda
def home_page():
    st.title("Selamat Datang di O-Kimiaku 🧪")
    st.write("""
    O-Kimiaku adalah aplikasi pembelajaran senyawa kimia organik yang menyediakan informasi tentang:
    - Tatanama senyawa kimia
    - Titik didih dan titik leleh
    - Fakta menarik
    - Kepolaran
    - Rumus kimia
    """)
    
    st.subheader("Pilih Jenis Senyawa Kimia:")
    cols = st.columns(3)
    
    for i, (chemical_type, data) in enumerate(chemical_data.items()):
        with cols[i % 3]:
            try:
                img = Image.open(f"images/{data['image']}")
                st.image(img, caption=data['name'], use_column_width=True)
            except:
                st.image("https://placehold.co/400x300?text=Chem+Image", caption=data['name'], use_column_width=True)
            
            if st.button(f"Pelajari {data['name']}"):
                st.session_state['current_page'] = 'chemical_detail'
                st.session_state['selected_chemical'] = chemical_type

# Fungsi untuk halaman detail senyawa
def chemical_detail_page():
    chemical_type = st.session_state['selected_chemical']
    data = chemical_data[chemical_type]
    
    st.title(f"Detail {data['name']}")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            img = Image.open(f"images/{data['image']}")
            st.image(img, use_column_width=True)
        except:
            st.image("https://placehold.co/400x300?text=Chem+Image", use_column_width=True)
    
    with col2:
        st.subheader("Informasi Senyawa:")
        st.write(f"**Rumus Kimia:** {data['formula']}")
        st.write(f"**Titik Didih:** {data['boiling_point']}")
        st.write(f"**Titik Leleh:** {data['melting_point']}")
        st.write(f"**Kepolaran:** {data['polarity']}")
        st.write(f"**Fakta Menarik:** {data['fun_fact']}")
        
        st.subheader("Video Pembelajaran:")
        st.video(data['youtube_link'])
    
    if st.button("Kembali ke Beranda"):
        st.session_state['current_page'] = 'home'

# Fungsi untuk chatbot
def chat_bot():
    st.sidebar.title("Chatbot O-Kimiaku")
    st.sidebar.write("Tanyakan tentang senyawa kimia yang tersedia")
    
    user_input = st.sidebar.text_input("Tanyakan sesuatu tentang senyawa kimia:")
    
    if user_input:
        response = generate_bot_response(user_input)
        st.sidebar.write(f"Bot: {response}")

def generate_bot_response(query):
    query = query.lower()
    for chemical_type, data in chemical_data.items():
        if chemical_type.lower() in query or data['name'].lower() in query:
            return f"Tentang {data['name']} ({data['formula']}): Titik didih {data['boiling_point']}, titik leleh {data['melting_point']}, bersifat {data['polarity']}. Fakta menarik: {data['fun_fact']}"
    
    return "Maaf, saya hanya bisa menjawab pertanyaan tentang senyawa kimia yang tersedia. Coba tanyakan tentang alkohol atau aldehida."

# Fungsi untuk about us
def about_us():
    st.title("Tentang Kami")
    st.write("""
    ## Tim Pengembang O-Kimiaku
    
    ### John Doe
    - Lead Developer
    - Spesialisasi: Kimia Komputasional
    
    ### Jane Smith
    - UI/UX Designer
    - Spesialisasi: Desain Aplikasi Edukasi
    
    ### Ahmad Budi
    - Content Specialist
    - Spesialisasi: Kimia Organik
    """)

# Fungsi untuk rating
def rating_page():
    st.title("Penilaian Anda")
    rating = st.slider("Beri rating untuk O-Kimiaku (1-5)", 1, 5)
    feedback = st.text_area("Masukkan feedback Anda (opsional)")
    
    if st.button("Submit Rating"):
        st.success("Terima kasih atas penilaian Anda!")
        st.balloons()
        st.session_state['rating_submitted'] = True
        st.session_state['current_page'] = 'close_app'

# Fungsi untuk menutup aplikasi
def close_app():
    if st.session_state.get('rating_submitted', False):
        st.write("Terima kasih telah menggunakan O-Kimiaku! Aplikasi akan ditutup.")
    else:
        rating_page()

# Main App
def main():
    # Sidebar navigation
    st.sidebar.title("Navigasi")
    page_options = {
        "Beranda": "home",
        "Tentang Kami": "about_us",
        "Keluar Aplikasi": "close_app"
    }
    
    selected_page = st.sidebar.radio("Pilih halaman:", list(page_options.keys()))
    st.session_state['current_page'] = page_options[selected_page]
    
    # Chatbot
    chat_bot()
    
    # Router halaman
    if st.session_state['current_page'] == 'home':
        home_page()
    elif st.session_state['current_page'] == 'chemical_detail':
        chemical_detail_page()
    elif st.session_state['current_page'] == 'about_us':
        about_us()
    elif st.session_state['current_page'] == 'close_app':
        close_app()

if __name__ == "__main__":
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'home'
    main()
