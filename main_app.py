import streamlit as st
import time

# Tampilan nama website
if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.set_page_config(
    page_title="O-Kimiaku",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# tampilan beranda
def show_home():
    st.title("Selamat Datang di O-KimiaKu 👩‍🔬🧪")
    col1, col2 = st.columns([1, 3])  

    with col1:
        st.image("logo_O-KimiaKu.jpg", width=120)  # logo di kiri

    with col2:
        st.markdown("""
        <p style='font-size:18px; margin-top:0;'>Aplikasi pembelajaran interaktif kimia yang memberikan informasi penting tentang senyawa kimia.</p>
        """, unsafe_allow_html=True)
        st.markdown("""
        **O-KimiaKu** adalah aplikasi pembelajaran interaktif kimia yang memberikan informasi penting tentang senyawa kimia, seperti:
        - ✅ Tatanama Senyawa
        - 🌡️ Titik Didih dan Titik Leleh
        - 🤓 Deskripsi Singkat
        - ⚖️ Kepolaran
        - 🧬 Rumus Kimia
    
        Klik gambar senyawa untuk mengetahui detailnya lebih lanjut!
        """)

    st.subheader("🔍 Pilih Senyawa:")
    st.markdown(" Dengan klik tombol senyawa 2 kali")
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
         if st.button("🧪 Aldehida"):
            st.session_state.page = 'aldehida'
         if st.button("⚡ Nitro"):
            st.session_state.page = 'nitro'
         if st.button("🧪 Nitril"):
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
         if st.button("🧪 Keton"):
            st.session_state.page = 'keton'
         if st.button("🧴 Ester"):
            st.session_state.page = 'ester'
         if st.button("💧 Eter"):
            st.session_state.page = 'eter'
         if st.button("🍗 Protein"):
            st.session_state.page = 'protein'
    with cols[4]:
         if st.button("🧪 Asam Halida"):
            st.session_state.page = 'asam_halida'
         if st.button("🧪 Asam Karboksilat"):
            st.session_state.page = 'asam_karboksilat'
         if st.button("🧪 Alkil Halida"):
            st.session_state.page = 'alkil_halida'
         if st.button("🛢️ Lemak dan Minyak"):
            st.session_state.page = 'lemak_dan_minyak'
            st.experimental_rerun()

             
# tampilan alkana
def show_alkana():
    st.title("Detail Senyawa: Alkana")

    st.markdown("""
    **Deskripsi:** Alkana adalah senyawa hidrokarbon jenuh yang hanya mengandung ikatan tunggal (σ) antar atom karbon (C–C) dan antara karbon dengan hidrogen (C–H). Rumus umumnya adalah CₙH₂ₙ₊₂. Alkana termasuk senyawa nonpolar dan merupakan komponen utama dalam gas alam dan minyak bumi.

    **Titik Didih:**
    - Titik didih alkana meningkat seiring bertambahnya jumlah atom karbon (massa molekul).
    - Bentuk rantai lurus memiliki titik didih lebih tinggi dibanding bentuk bercabang, karena permukaan kontak antar molekul lebih luas.
    - Contoh:
        - Metana (CH₄): −161,5 °C
        - Etana (C₂H₆): −88,6 °C
        - Butana (C₄H₁₀): −0,5 °C

    **Kepolaran:** Nonpolar, karena distribusi elektron seimbang dan tidak ada perbedaan keelektronegatifan yang signifikan antara C dan H. Tidak larut dalam air, tapi larut dalam pelarut organik nonpolar seperti eter dan kloroform.

    **Ikatan Kimia:** Hanya memiliki ikatan tunggal kovalen (σ). Semua atom C dalam alkana bersifat sp³ hibridisasi dengan bentuk geometri tetrahedral.

    **Tata Nama (IUPAC):** Tata nama alkana berdasarkan:
    1. Jumlah atom karbon → menentukan nama dasar:
        - 1: met-, 2: et-, 3: prop-, 4: but-, 5: pent-, dst.
    2. Akhiran -ana untuk menandakan alkana.
    3. Jika ada cabang, nama dimulai dengan nomor posisi dan nama gugus alkil (metil, etil, dll).

    **Contoh:**
    - CH₄ → Metana
    - CH₃–CH₃ → Etana
    - CH₃–CH₂–CH₃ → Propana
    - CH₃–CH(CH₃)–CH₃ → 2-Metilpropana (bentuk bercabang)
    
    **Video Penjelasan:**
    - [Video 1](https://youtu.be/Vzp-PAMsz7M?si=1Cv0gbxOMEWuQfMj)
    - [Video 2](https://youtu.be/HXzUk70i0wU?si=n7QFVZj9mMkc9twR)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'

# tampilan alkena
def show_alkena():
    st.title("Detail Senyawa: Alkena")

    st.markdown("""
    **Deskripsi**: Alkena adalah senyawa hidrokarbon tak jenuh yang memiliki setidaknya satu ikatan rangkap dua (C=C) antar atom karbon. Rumus umumnya CₙH₂ₙ. Alkena lebih reaktif dibanding alkana karena keberadaan ikatan π.

    **Titik Didih:**
    - Titik didih alkena meningkat seiring bertambahnya jumlah atom karbon.
    - Titik didihnya mirip alkana dengan jumlah C yang sama, tapi sedikit lebih rendah karena ikatan rangkap membuat bentuk molekul kurang simetris.
    - Contoh:
        - Etena (C₂H₄): −103,7 °C
        - Propena (C₃H₆): −47,6 °C

    **Kepolaran:** Secara umum nonpolar, tapi sedikit lebih polar dari alkana karena kerapatan elektron di ikatan rangkap dua. Tidak larut dalam air, larut dalam pelarut organik nonpolar.

    **Ikatan Kimia:** Memiliki 1 ikatan sigma (σ) dan 1 ikatan pi (π) pada ikatan rangkap dua. Atom karbon pada ikatan rangkap bersifat sp² hibridisasi, dengan geometri planar trigonal (sudut 120°).

    **Tata Nama (IUPAC):** Penamaan alkena mengikuti:
    1. Rantai terpanjang yang mengandung ikatan rangkap dua.
    2. Nomor posisi ikatan rangkap diberikan serendah mungkin.
    3. Akhiran -ena menunjukkan alkena.

    **Contoh:**
    - CH₂=CH₂ → Etena
    - CH₂=CH–CH₃ → Propena
    - CH₃–CH=CH–CH₃ → But-2-ena (atau but-1-ena tergantung posisi ikatan)
    
    **Video Penjelasan:**
    - [Video 1](https://youtu.be/0PaL8klVuVk?si=uffV4qvXCCU3dECi)
    - [Video 2](https://youtu.be/q3DhWJGolc4?si=PaTK0I6EXThce20i)
    - [Video 3](https://youtu.be/dJmVLfJtqtw?si=Eu1-KVcokh717JkY)
    - [Video 4](https://youtu.be/Utu6uZG_Glk?si=0xjgh6JQT0QjoURW)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'

# tampilan alkuna
def show_alkuna():
    st.title("Detail Senyawa: Alkuna")

    st.markdown("""
    **Deskripsi:** Alkuna adalah senyawa hidrokarbon tak jenuh yang memiliki setidaknya satu ikatan rangkap tiga (C≡C) antar atom karbon. Rumus umumnya CₙH₂ₙ₋₂. Karena adanya ikatan rangkap tiga, alkuna sangat reaktif dan dapat mengalami reaksi adisi.

    **Titik Didih:**
    - Titik didih alkuna meningkat seiring jumlah atom karbon.
    - Hampir mirip dengan alkena dan alkana, tetapi sedikit lebih tinggi karena ikatan rangkap tiga memberikan bentuk molekul yang lebih linier dan polarizable.
    - Contoh:
        - Etuna (asetilena, C₂H₂): −84 °C
        - Butuna (C₄H₆): sekitar 0–4 °C

    **Kepolaran:** Sebagian besar alkuna adalah nonpolar. Tidak larut dalam air, tapi larut dalam pelarut organik nonpolar seperti eter atau benzena.

    **Ikatan Kimia:** Memiliki 1 ikatan sigma (σ) dan 2 ikatan pi (π) dalam ikatan rangkap tiga. Atom karbon pada ikatan rangkap tiga bersifat sp hibridisasi, dengan geometri linier (sudut ikatan 180°).

    **Tata Nama (IUPAC):** Penamaan alkuna mengikuti:
    1. Pilih rantai terpanjang yang mengandung ikatan rangkap tiga.
    2. Penomoran dari ujung terdekat ikatan rangkap tiga.
    3. Gunakan akhiran -una.

    **Contoh:**
    - CH≡CH → Etuna (asetilena)
    - CH≡C–CH₃ → Propuna
    - CH₃–C≡C–CH₃ → But-2-una

     **Video Penjelasan:**
    - [Video 1](https://youtu.be/pbDiXi3ny1E?si=sWfZ3UswqewTWuzm)
    - [Video 2](https://youtu.be/mGQprCdRZ4s?si=h5ST0P2OYVC0oYWs)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_alkohol():
    st.title("Detail Senyawa: Alkohol")

    st.markdown("""
    **Deskripsi:** Alkohol adalah senyawa organik yang memiliki gugus hidroksil (–OH) yang terikat pada atom karbon jenuh (sp³). Rumus umum: R–OH, di mana R adalah gugus alkil. Alkohol bersifat polar dan sering terlibat dalam pembentukan ikatan hidrogen.

    **Titik Didih:**
    - Tinggi dibanding alkana/alkena/alkuna dengan jumlah karbon yang sama, karena ada ikatan hidrogen antar molekul alkohol.
    - Semakin panjang rantai karbon → makin tinggi titik didih.
    - Contoh:
        - Metanol (CH₃OH): 64,7 °C
        - Etanol (CH₃CH₂OH): 78,4 °C
        - 1-Butanol: 117,7 °C

    **Kepolaran:** Polar, karena gugus –OH memiliki perbedaan keelektronegatifan besar antara O dan H. Dapat larut dalam air (terutama alkohol rantai pendek) karena membentuk ikatan hidrogen. Alkohol rantai panjang → kelarutan menurun karena sifat nonpolar dari rantai alkil mendominasi.

    **Ikatan Kimia:** Gugus –OH terdiri dari ikatan kovalen polar O–H dan C–O. Atom O pada –OH dapat membentuk ikatan hidrogen antar molekul atau dengan air. Atom C yang terikat –OH bersifat sp³ hibridisasi.

    **Tata Nama (IUPAC):** Penamaan alkohol:
    1. Pilih rantai utama yang mengandung gugus –OH.
    2. Nomor posisi –OH serendah mungkin.
    3. Akhiran diganti menjadi -ol.
    4. Jika lebih dari satu gugus –OH, gunakan akhiran -diol, -triol, dst.

    **Contoh:**
    - CH₃OH → Metanol
    - CH₃CH₂OH → Etanol
    - CH₃CH(OH)CH₃ → 2-Propanol
    - HO–CH₂–CH₂–OH → 1,2-Etanadiol (etilen glikol)

     **Video Penjelasan:**
    - [Video](https://youtu.be/1nfKdKFOxgw?si=FNi98kksQ-_FV0ki)
    - [Video](https://youtu.be/-GvgmYqdpHA?si=cn2Y7ulIVFOAKKSM)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_protein():
    st.title("Detail Senyawa: Protein")

    st.markdown("""
    **Deskripsi Pengetahuan Singkat:** Protein adalah polimer alami yang tersusun dari rantai panjang asam amino yang terhubung oleh ikatan peptida (sejenis ikatan amida). Protein berperan vital dalam struktur sel, enzim, hormon, antibodi, dan transportasi molekul. Struktur protein dibedakan menjadi:
    - **Struktur primer:** urutan asam amino
    - **Struktur sekunder:** bentuk lokal (α-heliks, β-sheet)
    - **Struktur tersier:** bentuk tiga dimensi
    - **Struktur kuartener:** asosiasi beberapa rantai polipeptida

    **Titik Didih:**
    - Tidak relevan untuk protein besar, karena protein tidak memiliki titik didih yang pasti—panas menyebabkan denaturasi (struktur rusak) sebelum menguap.
    - Denaturasi biasanya terjadi di kisaran suhu 40–80 °C, tergantung jenis protein.

    **Kepolaran:**
    - Amfipatik (mengandung bagian polar dan nonpolar)
    - Beberapa bagian protein polar dan larut dalam air (berinteraksi dengan lingkungan sel), bagian lain nonpolar dan tersembunyi di dalam struktur 3D.

    **Ikatan Kimia:**
    - Ikatan peptida (amida) antara gugus –COOH dan –NH₂ antar asam amino
    - Ikatan non-kovalen: ikatan hidrogen, gaya van der Waals, interaksi hidrofobik
    - Ikatan disulfida (–S–S–) antara dua sistein → membantu struktur stabil

    **Tata Nama:**
    - Tidak dinamai secara IUPAC seperti senyawa organik kecil.
    - Nama protein berdasarkan fungsi, struktur, atau asal biologis, misalnya:
        - Insulin → hormon pengatur gula darah
        - Hemoglobin → pengangkut oksigen
        - Amilase → enzim pemecah pati

    **Video Penjelasan:**
    - [Video 1](https://youtu.be/3kybW5T76Ek?si=dbybMp0ObIBrrqit)
    - [Video 2](https://youtu.be/DnTwLYWG1fQ?si=9tF5RLdkrA__M3bl)
    - [Video 3](https://youtu.be/tLdCWZvODXg?si=PeFbccfuF7hYveUV)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_fenol():
    st.title("Detail Senyawa: Fenol")

    st.markdown("""
    **Deskripsi:** Fenol (C₆H₅OH) adalah senyawa aromatik yang terdiri dari cincin benzena yang terikat pada gugus hidroksil (-OH). Fenol adalah padatan kristal putih yang mudah larut dalam pelarut organik dan sedikit larut dalam air. Berbau khas tajam dan bersifat korosif.

    **Titik Didih:**
    - Titik didih fenol: 181,7 °C
    - Titik leleh: 40,9 °C
    - Titik didihnya lebih tinggi dari benzena karena adanya ikatan hidrogen antar molekul fenol.

    **Kepolaran:** Polar, karena mengandung gugus hidroksil (-OH) yang bersifat polar. Meskipun cincin benzena bersifat nonpolar, gugus -OH membuat senyawa ini memiliki momen dipol.

    **Ikatan Kimia:** Ikatan kovalen antara atom karbon dan hidrogen dalam cincin benzena. Gugus -OH terikat secara kovalen ke cincin aromatik. Ikatan hidrogen dapat terbentuk antar molekul fenol karena adanya gugus -OH, menyebabkan titik didih tinggi. Interaksi resonansi juga terjadi antara cincin benzena dan gugus -OH, memengaruhi sifat keasaman fenol.

    **Tata Nama (IUPAC dan umum):**
    - Nama umum: Fenol
    - Nama IUPAC: Benzenol
    - Jika fenol memiliki substituen, penamaannya mengikuti posisi pada cincin, misalnya:
        - o-Kresol (2-metilfenol) → gugus metil di posisi orto
        - p-Nitrofenol (4-nitrobenzenol) → gugus nitro di posisi para

    **Video Penjelasan:**
    - [Video 1](https://youtu.be/euFL7iukzms?si=wzLy8DIb3YFjw3N6)
    - [Video 2](https://youtu.be/oXw9Pg6ekwc?si=0ry7qAdmJ9GOVk5b)
    - [Video 3](https://youtu.be/A8GQHwidRSI?si=_noRE0NT56t0GTFC)
    - [Video 4](https://youtu.be/-xGXGGM909M?si=RrCRHm2SlgTrIM00)
    - [Video 5](https://youtu.be/uQ7IcLkO9uE?si=Ar3XpPtTHi8hTaBD)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_eter():
    st.title("Detail Senyawa: Eter")

    st.markdown("""
    **Deskripsi:** Eter adalah senyawa organik yang memiliki dua gugus alkil atau aril yang terikat pada atom oksigen. Rumus umum untuk eter adalah R–O–R', di mana R dan R' adalah gugus alkil atau aril. Eter sering digunakan sebagai pelarut dalam reaksi kimia dan sebagai bahan bakar.

    **Titik Didih:**
    - Titik didih eter lebih rendah dibandingkan alkohol dengan massa molekul yang sama, karena eter tidak dapat membentuk ikatan hidrogen antar molekul.
    - Namun, titik didih eter lebih tinggi dibandingkan dengan hidrokarbon nonpolar seukuran.
    - Contoh:
        - Dietil eter (C₂H₅)₂O: 34,6 °C
        - Eter metil (CH₃)₂O: −24,9 °C

    **Kepolaran:** 
    - Eter bersifat polar, tetapi tidak sepolar alkohol. Eter dapat membentuk ikatan hidrogen dengan air, tetapi tidak dapat membentuk ikatan hidrogen antar molekul eter.
    - Eter rantai pendek larut dalam air, tetapi eter rantai panjang kurang larut.

    **Ikatan Kimia:**
    - Eter memiliki ikatan sigma (σ) antara atom karbon dan oksigen.
    - Struktur eter bersifat tetrahedral di sekitar atom oksigen, dengan sudut ikatan sekitar 110°.
    - Eter tidak memiliki ikatan pi (π) karena tidak ada ikatan rangkap.

    **Tata Nama (IUPAC):**
    - Penamaan eter dilakukan dengan menyebutkan nama gugus alkil yang terikat pada oksigen, diikuti dengan kata "eter".
    - Jika ada dua gugus alkil yang berbeda, nama yang lebih besar ditulis terlebih dahulu.

    **Contoh:**
    - CH₃OCH₃ → Dimetil eter
    - C₂H₅OCH₃ → Eter metil etil
    - C₃H₇OCH₂CH₃ → Eter etil propil

    **Video Penjelasan:**
    - [Video](https://youtu.be/YGLRGqprGcQ?si=iDnthU2BN_Ugqvh2)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_aldehida():
    st.title("Detail Senyawa: Aldehid")

    st.markdown("""
    **Deskripsi:** Aldehid adalah senyawa organik yang memiliki gugus karbonil (C=O) di ujung rantai karbon, dengan rumus umum R–CHO. Gugus fungsionalnya disebut formil. Aldehid banyak ditemukan dalam zat aroma dan zat antara dalam sintesis organik.

    **Titik Didih:**
    - Titik didih lebih tinggi daripada alkana/eter, tapi lebih rendah dari alkohol.
    - Ini karena aldehid memiliki ikatan dipol-dipol, tetapi tidak bisa membentuk ikatan hidrogen antar sesamanya.
    - Contoh:
        - Formaldehida (HCHO): −19 °C
        - Asetaldehida (CH₃CHO): 20,2 °C
        - Butanal: 75 °C

    **Kepolaran:** Sangat polar, karena gugus karbonil (C=O) memiliki perbedaan keelektronegatifan besar antara C dan O. Larut dalam air (terutama rantai pendek) karena dapat membentuk ikatan hidrogen dengan air.

    **Ikatan Kimia:** Gugus karbonil terdiri dari satu ikatan sigma (σ) dan satu ikatan pi (π). Atom karbon pada C=O bersifat sp² hibridisasi dengan bentuk planar trigonal. Ujung gugus –CHO memberikan reaktivitas tinggi, terutama dalam reaksi oksidasi dan adisi nukleofilik.

    **Tata Nama (IUPAC):** Penamaan aldehid:
    1. Pilih rantai utama yang mengandung gugus –CHO.
    2. Beri nomor dari karbon aldehid (selalu nomor 1).
    3. Ganti akhiran -a pada nama alkana menjadi -al.

    **Contoh:**
    - HCHO → Metanal (formaldehida)
    - CH₃CHO → Etanal (asetaldehida)
    - CH₃CH₂CH₂CHO → Butanal

     **Video Penjelasan:**
    - [Video 1](https://youtu.be/I8i8jr3lieo?si=rbVQW0x8nC8Lj8y7)
    - [Video 2](https://youtu.be/KbF0gH4BURY?si=ZvG64m-NHkVHnT0p)
    - [Video 3](https://youtu.be/p3jf_RKbdcI?si=WgZKm_4gXnY3SXQl)
    - [Video 4](https://youtu.be/-_nL-qb0xN4?si=vkFi5jboEEU5u5ov)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_keton():
    st.title("Detail Senyawa: Keton")

    st.markdown("""
    **Deskripsi:** Keton adalah senyawa organik yang memiliki gugus karbonil (C=O) di tengah rantai karbon, bukan di ujung seperti aldehid. Rumus umumnya R–CO–R′, di mana R dan R′ adalah gugus alkil atau aril. Keton sering ditemukan dalam pelarut dan zat aroma (misalnya: aseton).

    **Titik Didih:**
    - Titik didih lebih tinggi dari alkana/eter, tetapi lebih rendah dari alkohol.
    - Karena memiliki gaya dipol-dipol kuat, tetapi tidak membentuk ikatan hidrogen antar sesamanya.
    - Contoh:
        - Aseton (CH₃COCH₃): 56,5 °C
        - 2-Butanon (CH₃COCH₂CH₃): 79,6 °C

    **Kepolaran:** Polar, karena gugus karbonil bersifat polar. Keton rantai pendek larut dalam air karena bisa membentuk ikatan hidrogen dengan air, tapi rantai panjang → kelarutan berkurang. Umumnya larut baik dalam pelarut organik.

    **Ikatan Kimia:** Gugus karbonil mengandung 1 ikatan sigma (σ) dan 1 ikatan pi (π). Atom karbon dalam gugus C=O bersifat sp² hibridisasi dan memiliki bentuk planar trigonal. Karena karbonilnya di tengah, keton tidak mudah teroksidasi seperti aldehid.

    **Tata Nama (IUPAC):** Penamaan keton:
    1. Pilih rantai utama yang mengandung gugus karbonil.
    2. Penomoran dilakukan agar posisi karbonil mendapatkan nomor serendah mungkin.
    3. Ganti akhiran -a pada alkana menjadi -on.
    4. Sebutkan posisi gugus karbonil jika diperlukan.

    **Contoh:**
        - CH₃COCH₃ → Propanon (aseton)
        - CH₃CH₂COCH₃ → Butanon
        - CH₃COCH₂CH₂CH₃ → Pentan-2-on

         **Video Penjelasan:**
    - [Video 1](https://youtu.be/I8i8jr3lieo?si=rbVQW0x8nC8Lj8y7)
    - [Video 2](https://youtu.be/KbF0gH4BURY?si=ZvG64m-NHkVHnT0p)
    - [Video 3](https://youtu.be/p3jf_RKbdcI?si=WgZKm_4gXnY3SXQl)
    - [Video 4](https://youtu.be/-_nL-qb0xN4?si=vkFi5jboEEU5u5ov)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_amina():
    st.title("Detail Senyawa: Amina")

    st.markdown("""
    **Deskripsi:** Amina adalah senyawa organik turunan amonia (NH₃) di mana satu atau lebih atom hidrogen diganti dengan gugus alkil atau aril. Dibagi menjadi:
    - Amina primer (1°): R–NH₂
    - Amina sekunder (2°): R–NH–R′
    - Amina tersier (3°): R–N(R′)–R″
    Amina banyak terdapat dalam senyawa biologis (seperti asam amino, neurotransmitter) dan obat-obatan.

    **Titik Didih:**
    - Amina primer dan sekunder dapat membentuk ikatan hidrogen, sehingga titik didihnya lebih tinggi dari senyawa nonpolar (seperti alkana), tetapi lebih rendah dari alkohol.
    - Amina tersier tidak dapat membentuk ikatan hidrogen antar sesama molekul → titik didihnya lebih rendah.
    - Contoh:
        - Metilamina (CH₃NH₂): −6.3 °C
        - Dimetilamina (CH₃)₂NH: 7 °C
        - Trimetilamina (CH₃)₃N: 3.5 °C

    **Kepolaran:** Polar, karena adanya pasangan elektron bebas pada atom nitrogen dan perbedaan keelektronegatifan antara N dan H/C. Amina rantai pendek larut dalam air karena bisa membentuk ikatan hidrogen dengan air. Amina rantai panjang → kelarutan menurun.

    **Ikatan Kimia:** Amina memiliki ikatan sigma (σ) antara nitrogen dan karbon/hidrogen. Nitrogen dalam amina biasanya bersifat sp³ hibridisasi, dengan bentuk piramida trigonal dan satu pasangan elektron bebas. Bersifat basa lemah, karena nitrogen dapat menerima proton (donor pasangan elektron).

    **Tata Nama (IUPAC):** Penamaan amina:
    - Amina primer: Nama gugus alkil + amina
        - CH₃NH₂ → Metilamina
        - CH₃CH₂NH₂ → Etilamina
    - Amina sekunder/tersier:
        - Jika sederhana → sebutkan semua gugus alkil + “amina”
            - (CH₃)₂NH → Dimetilamina
        - Untuk yang lebih kompleks → dianggap substituen: “amino-”
            - NH₂CH₂CH₃ → 2-Aminoetana

     **Video Penjelasan:**
    - [Video](https://youtu.be/0aDWKCzWHuw?si=PEakWNqHfsdPiKK7)      
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_lemak_dan_minyak():
    st.title("Detail Senyawa: Lemak dan Minyak")

    st.markdown("""
    **Deskripsi:** Lemak dan minyak adalah bagian dari kelompok lipid yang terdiri dari ester dari gliserol dan asam lemak (disebut trigliserida).
    - **Lemak:** padat pada suhu ruang → biasanya berasal dari hewan.
    - **Minyak:** cair pada suhu ruang → biasanya berasal dari tumbuhan atau ikan.
    Perbedaan utama terletak pada tingkat kejenuhan:
    - Lemak jenuh → tidak ada ikatan rangkap (C–C)
    - Minyak tak jenuh → ada satu atau lebih ikatan rangkap (C=C)

    **Titik Didih:**
    - Titik didih trigliserida sangat tinggi (300 °C ke atas), tapi mudah rusak (terurai) saat dipanaskan berlebih.
    - Titik leleh:
        - Lemak jenuh → titik leleh tinggi (padat)
        - Minyak tak jenuh → titik leleh rendah (cair)

    **Kepolaran:** 
    - Nonpolar, karena struktur utamanya terdiri dari rantai hidrokarbon panjang.
    - Tidak larut dalam air, tapi larut dalam pelarut nonpolar seperti eter, kloroform, atau benzena.

    **Ikatan Kimia:**
    - Ikatan ester (–COO–) antara gugus –OH dari gliserol dan gugus –COOH dari asam lemak.
    - Asam lemak bisa:
        - Jenuh (tanpa ikatan rangkap) → lurus, mudah padat
        - Tak jenuh (mengandung ikatan rangkap) → bengkok, mencegah pemadatan
    - Dalam minyak nabati, sering mengandung asam lemak tak jenuh seperti asam oleat.

    **Tata Nama:**
    - Tidak dinamai secara sistem IUPAC penuh, tetapi:
        - Asam lemak dinamai seperti asam karboksilat panjang:
            - Asam stearat (C₁₇H₃₅COOH)
            - Asam oleat (C₁₇H₃₃COOH)
        - Trigliserida → dinamai berdasarkan kombinasi asam lemak dan gliserol.
        - Contoh:
            - Tristearin → dari 3 asam stearat + gliserol
            - Triolein → dari 3 asam oleat + gliserol

    **Video Penjelasan:**
    - [Video 1](https://youtu.be/PRyOFFzh9pc?si=PbSculDk-wzSFw4X)
    - [Video 2](https://youtu.be/RVcw6IdUJLo?si=1KdUGjLdsnToKNul)
    - [Video 3](https://youtu.be/aUdP3JJhBRA?si=AA331_st2qhTQi15)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_benzena():
    st.title("Detail Senyawa: Benzena")

    st.markdown("""
    **Deskripsi:** Benzena adalah senyawa hidrokarbon aromatik paling sederhana dengan rumus C₆H₆. Strukturnya berupa cincin planar dengan 6 atom karbon dan 6 atom hidrogen, di mana ikatan antar karbon mengalami resonansi → menghasilkan delokalisasi elektron pada cincin aromatik. Benzena bersifat stabil, tapi tetap bisa mengalami reaksi substitusi.

    **Titik Didih:**
    - Titik didih benzena: 80,1 °C
    - Lebih tinggi dari senyawa nonpolar kecil lainnya karena bentuk simetris dan interaksi π-π antar cincin aromatik.
    - Titik leleh: 5,5 °C

    **Kepolaran:** 
    - Nonpolar secara keseluruhan, karena simetris dan tidak memiliki gugus polar.
    - Tidak larut dalam air, tapi larut dalam pelarut organik nonpolar seperti eter, kloroform, atau heksana.

    **Ikatan Kimia:**
    - Setiap atom C terhubung dengan dua C lain dan satu H → membentuk ikatan sigma (σ).
    - Terdapat delokalisasi elektron π di atas dan di bawah cincin → menghasilkan resonansi aromatik.
    - Semua ikatan C–C pada benzena setara dengan panjang ikatan antara ikatan tunggal dan rangkap.

    **Tata Nama (IUPAC):**
    - Senyawa ini dinamai benzena jika murni.
    - Jika bercabang, penamaan dilakukan dengan memberi nomor pada cincin:
        - C₆H₅CH₃ → metilbenzena (toluena)
        - C₆H₅OH → hidroksibenzena (fenol)
        - C₆H₅NO₂ → nitrobenzena
    - Jika ada dua substituen: orto (1,2), meta (1,3), para (1,4) digunakan untuk posisi relatifnya.

    **Video Penjelasan:**
    - [Video 1](https://youtu.be/1aluQZqkqNE?si=c6fzD0HlqDrRDzgc)
    - [Video 2](https://youtu.be/YMHdLlx6WIw?si=3fy86L1X57yMDUiW)
    - [Playlist](https://youtube.com/playlist?list=PLWB5gICYvKUXBVat1VVyDzNhhCcz1Y4Wt&si=Cd5F1txXJxLR8Zg3)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_asam_karboksilat():
    st.title("Detail Senyawa: Asam Karboksilat")

    st.markdown("""
    **Deskripsi:** Asam karboksilat adalah senyawa organik yang memiliki gugus karboksil (–COOH), yaitu gabungan dari gugus karbonil (C=O) dan hidroksil (–OH) pada karbon yang sama. Rumus umum: R–COOH. Senyawa ini bersifat asam lemah dan banyak ditemukan dalam alam, seperti dalam cuka (asam asetat) dan lemak (asam lemak).

    **Titik Didih:**
    - Sangat tinggi dibanding alkohol, karena asam karboksilat membentuk ikatan hidrogen ganda (dimer) yang kuat antar molekul.
    - Titik didih meningkat seiring bertambahnya jumlah atom karbon.
    - Contoh:
        - Asam format (HCOOH): 100,8 °C
        - Asam asetat (CH₃COOH): 118,1 °C
        - Asam butirat (CH₃CH₂CH₂COOH): 163,7 °C

    **Kepolaran:** Sangat polar, karena mengandung gugus karbonil dan hidroksil sekaligus. Sangat larut dalam air (terutama rantai pendek), karena dapat membentuk ikatan hidrogen dengan air. Rantai panjang → kelarutan menurun karena bagian hidrokarbon makin dominan.

    **Ikatan Kimia:**
    - Mengandung:
        - Ikatan sigma (σ) dan pi (π) pada C=O.
        - Ikatan sigma antara C–O dan O–H.
        - Atom karbon pada –COOH bersifat sp² hibridisasi, dengan bentuk planar trigonal.
        - Dapat melepaskan proton (H⁺) dari gugus –OH → bersifat asam lemah.

    **Tata Nama (IUPAC):** Penamaan asam karboksilat:
    1. Rantai utama mencakup gugus –COOH.
    2. Nomor 1 selalu diberikan pada karbon karboksilat.
    3. Nama alkana diganti akhiran -a menjadi -oat (untuk garam/ester) atau -oat ion (untuk ionik), tetapi untuk asam murni: -oat tetap disebut “asam -oat”.

    **Contoh:**
    - HCOOH → Asam metanoat (asam format)
    - CH₃COOH → Asam etanoat (asam asetat)
    - CH₃CH₂CH₂COOH → Asam butanoat (asam butirat)

    **Video Penjelasan:**
    - [Video](https://youtu.be/6xoYyrJkboI?si=D78Rh0NJCbmykDyg)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_amida():
    st.title("Detail Senyawa: Amida")

    st.markdown("""
    **Deskripsi:** Amida adalah turunan dari asam karboksilat di mana gugus –OH pada gugus karboksil (–COOH) digantikan oleh gugus amina (–NH₂, –NHR, atau –NR₂). Rumus umum: R–CONH₂ untuk amida primer. Amida banyak ditemukan dalam protein (ikatan peptida adalah amida).

    **Titik Didih:**
    - Titik didih tinggi, karena dapat membentuk ikatan hidrogen yang kuat (terutama amida primer dan sekunder).
    - Titik didih amida biasanya lebih tinggi dari asam karboksilat dengan massa molekul setara.
    - Contoh:
        - Metanamida (formamida, HCONH₂): 210 °C
        - Etanamida (asetamida, CH₃CONH₂): 222 °C

    **Kepolaran:** 
    - Sangat polar, karena adanya gugus karbonil (C=O) dan gugus amino (–NH₂) yang keduanya bersifat polar.
    - Larut dalam air (terutama amida rantai pendek) karena mampu membentuk ikatan hidrogen dengan air.

    **Ikatan Kimia:**
    - Memiliki:
        - Ikatan sigma dan pi dalam gugus karbonil (C=O)
        - Ikatan sigma antara C–N dan N–H
    - Atom karbon dalam gugus –CONH₂ bersifat sp² hibridisasi, struktur planar.
    - Ikatan C–N dalam amida memiliki karakter ganda sebagian (resonansi) → membuatnya stabil dan kurang reaktif dibanding amina biasa.

    **Tata Nama (IUPAC):**
    - Penamaan amida:
        1. Nama berasal dari asam karboksilat asalnya, dengan akhiran -amida.
        2. Jika gugus N disubstitusi (pada amida sekunder/tersier), gugus tambahan diberi awalan N-.

    **Contoh:**
    - CH₃CONH₂ → Etanamida (asetamida)
    - HCONH₂ → Metanamida (formamida)
    - CH₃CONHCH₃ → N-Metiletanamida
    - CH₃CON(CH₃)₂ → N,N-Dimetiletanamida

     **Video Penjelasan:**
    - [Video 1](https://youtu.be/Lz78W5L6bR4?si=eJtoQx5LpYcMfwYv)
    - [Video 2](https://youtu.be/CYYGb1tCTAs?si=upVbkqTxI-3nPTGi)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_alkil_halida():
    st.title("Detail Senyawa: Alkil Halida")

    st.markdown("""
    **Deskripsi:** Alkil halida atau haloalkana adalah senyawa organik yang terbentuk dari alkana dengan menggantikan satu atau lebih atom H dengan atom halogen (F, Cl, Br, I). Rumus umum: R–X, di mana R = gugus alkil, X = halogen. Digunakan luas dalam industri, pelarut, refrigeran, dan sebagai senyawa antara dalam sintesis organik.

    **Titik Didih:**
    - Titik didih lebih tinggi dari alkana dengan jumlah karbon setara, karena interaksi dipol–dipol dari gugus halogen.
    - Titik didih meningkat dengan:
        - Meningkatnya massa molekul (dari F ke I)
        - Meningkatnya panjang rantai karbon
    - Contoh:
        - CH₃Cl: −24,2 °C
        - CH₃Br: 3,6 °C
        - CH₃I: 42,4 °C

    **Kepolaran:** 
    - Polar, karena perbedaan keelektronegatifan antara karbon dan halogen → menciptakan ikatan polar C–X.
    - Larut dalam pelarut organik, tetapi tidak larut baik dalam air, kecuali untuk haloalkana kecil.

    **Ikatan Kimia:**
    - Mengandung ikatan sigma (σ) polar antara C–X.
    - Halogen bersifat elektronegatif → menarik elektron dari C → C menjadi elektrofilik (suka diserang nukleofil).
    - Atom karbon dalam alkil halida umumnya sp³ hibridisasi.
    - Reaktif dalam reaksi substitusi dan eliminasi, tergantung kondisi.

    **Tata Nama (IUPAC):**
    - Penamaan alkil halida:
        1. Pilih rantai utama dari alkana.
        2. Nomori rantai agar posisi halogen (F, Cl, Br, I) serendah mungkin.
        3. Gunakan awalan fluoro-, kloro-, bromo-, iodo- sesuai halogennya.

    **Contoh:**
    - CH₃Cl → Klorometana
    - CH₃CH₂Br → Bromometana
    - CH₃CH(Cl)CH₃ → 2-Kloropropana
    - CH₃CHBrCH₂CH₃ → 2-Bromobutana

    **Video Penjelasan:**
    - [Video](https://youtu.be/zxUFOd1shr0?si=5IPjGEpazI6zGcDd)
    """)

    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_nitro():
    st.title("Detail Senyawa: Nitro")

    st.markdown("""
    **Deskripsi:** Senyawa nitro adalah senyawa organik yang mengandung gugus nitro (–NO₂), yaitu gugus nitrogen yang terikat pada dua atom oksigen: satu melalui ikatan rangkap (N=O), satu melalui ikatan tunggal (N–O⁻), membentuk struktur resonansi. Contoh umum: nitrobenzena (C₆H₅NO₂). Senyawa nitro penting dalam bahan peledak (seperti TNT), pelarut, dan sintesis kimia.

    **Titik Didih:**
    - Umumnya memiliki titik didih tinggi, karena:
        - Gugus nitro sangat polar
        - Terjadi gaya tarik dipol-dipol kuat antar molekul
    - Contoh:
        - Nitroetan: 114 °C
        - Nitrobenzena: 210,9 °C

    **Kepolaran:** 
    - Sangat polar, karena gugus –NO₂ memiliki distribusi muatan tidak merata (struktur resonansi dengan muatan parsial).
    - Larut dalam pelarut polar aprotik, tapi umumnya tidak larut dalam air (kecuali yang kecil seperti nitrometana).

    **Ikatan Kimia:**
    - Gugus nitro memiliki:
        - 1 ikatan sigma dan 1 ikatan pi antara N=O
        - 1 ikatan sigma antara N–O
    - Resonansi membuat muatan tersebar antara kedua oksigen → stabil.
    - Atom N dalam gugus –NO₂ bersifat sp² hibridisasi dan berbentuk planar.

    **Tata Nama (IUPAC):**
    - Gugus –NO₂ dinamai sebagai “nitro-” dan dianggap substituen.
    - Letaknya ditunjukkan dengan nomor posisi pada rantai utama atau cincin aromatik.

    **Contoh:**
    - CH₃NO₂ → Nitrometana
    - CH₃CH₂NO₂ → Nitroetana
    - C₆H₅NO₂ → Nitrobenzena
    - C₆H₄(NO₂)₂ → 1,3-Dinitrobenzena (atau meta-dinitrobenzena)

    **Video Penjelasan:**
    - [Video 1](https://youtu.be/LbL3qLDL1ww?si=BXQwimr12FWda-Up)
    - [Video 2](https://youtu.be/LbL3qLDL1ww?si=SyugwAr2P8SWabpU)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_nitril():
    st.title("Detail Senyawa: Nitril")

    st.markdown("""
    **Deskripsi:** Nitril adalah senyawa organik yang mengandung gugus –C≡N (gugus sianida), yaitu atom karbon yang berikatan rangkap tiga dengan atom nitrogen. Rumus umum: R–C≡N. Nitril sering digunakan sebagai bahan antara dalam sintesis senyawa farmasi, polimer (seperti akrilonitril), dan pelarut polar aprotik.

    **Titik Didih:**
    - Nitril memiliki titik didih sedang hingga tinggi, tergantung panjang rantai karbonnya.
    - Titik didih lebih tinggi dari alkana/alkil halida karena adanya interaksi dipol-dipol kuat dari gugus –C≡N.
    - Contoh:
        - Akrilonitril (CH₂=CH–CN): 77 °C
        - Propanonitril (CH₃CH₂–CN): 97 °C

    **Kepolaran:** 
    - Sangat polar, karena ikatan rangkap tiga C≡N menciptakan momen dipol yang besar.
    - Larut dalam pelarut polar (seperti air, alkohol) terutama untuk nitril rantai pendek.
    - Sering digunakan sebagai pelarut polar aprotik dalam kimia organik.

    **Ikatan Kimia:**
    - Mengandung ikatan rangkap tiga antara karbon dan nitrogen:
        - 1 ikatan sigma (σ)
        - 2 ikatan pi (π)
    - Atom karbon dalam gugus nitril bersifat sp hibridisasi, sehingga molekul bersifat linier di sekitar gugus –C≡N.
    - Gugus nitril bersifat elektrofilik → dapat mengalami reaksi adisi dan hidrolisis.

    **Tata Nama (IUPAC):**
    - Penamaan IUPAC menggunakan akhiran -nitril, dan rantai utama harus mencakup karbon dari gugus –C≡N.
    - Jika gugus –CN sebagai substituen → disebut “siano-”.

    **Contoh:**
    - CH₃–C≡N → Etanonitril (nama umum: asetonitril)
    - C₆H₅–C≡N → Benzenakarbonitril (nama umum: benzonitril)
    - CH₂=CH–C≡N → Akrilonitril
    - NC–CH₂–CH₂–COOH → Asam sianopropanoat

    **Video Penjelasan:**
    - [Video](https://youtu.be/JktYNjqt4wU?si=nc-IBD-rUnUPYFXU)
    """)

    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_ester():
    st.title("Detail Senyawa: Ester")

    st.markdown("""
    **Deskripsi:** Ester adalah senyawa turunan asam karboksilat di mana gugus –OH diganti dengan gugus alkoksi (–OR). Rumus umum: R–COOR′. Ester sering ditemukan dalam aroma buah, minyak esensial, dan sebagai pelarut organik atau bahan pembuatan plastik (poliester).

    **Titik Didih:**
    - Titik didih lebih rendah daripada asam karboksilat dan alkohol, karena ester tidak membentuk ikatan hidrogen antar molekulnya.
    - Namun, lebih tinggi dari eter atau alkana seukuran karena ada interaksi dipol-dipol.
    - Contoh:
        - Metil etanoat (CH₃COOCH₃): 57 °C
        - Etil etanoat (CH₃COOCH₂CH₃): 77 °C

    **Kepolaran:** 
    - Agak polar, karena mengandung gugus karbonil (C=O) dan gugus eter (C–O–C).
    - Ester rantai pendek larut dalam air (dapat membentuk ikatan hidrogen dengan air), namun rantai panjang tidak larut.
    - Larut dalam pelarut organik seperti eter dan alkohol.

    **Ikatan Kimia:**
    - Ester mengandung:
        - 1 ikatan σ dan 1 ikatan π dalam gugus karbonil (C=O)
        - Ikatan σ antara C–O dan C–C
    - Atom karbon dalam gugus karbonil bersifat sp² hibridisasi, membentuk struktur planar trigonal.
    - Ester mudah mengalami reaksi hidrolisis menjadi asam karboksilat dan alkohol, terutama dengan katalis asam atau basa.

    **Tata Nama (IUPAC):**
    - Penamaan ester terdiri dari dua bagian:
        1. Nama alkil dari bagian alkohol (yang terikat ke O)
        2. Nama rantai asam dengan akhiran diganti menjadi -oat

    **Contoh:**
    - CH₃COOCH₃ → Metil etanoat
    - CH₃COOCH₂CH₃ → Etil etanoat
    - CH₃CH₂COOCH₃ → Metil propanoat
    - CH₃CH₂COOCH₂CH₃ → Etil propanoat

    **Video Penjelasan:**
    - [Video](https://youtu.be/6BO-ZWmLLSU?si=fMfpCo91cfeRrnOq)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_asam_halida():
    st.title("Detail Senyawa: Asam Halida")

    st.markdown("""
    **Deskripsi:** Asam halida (lebih tepatnya: asil halida) adalah turunan dari asam karboksilat di mana gugus –OH diganti oleh halogen (umumnya Cl atau Br). Rumus umum: R–COX, dengan X = halogen. Asetil klorida (CH₃COCl) adalah contoh paling umum. Senyawa ini sangat reaktif, digunakan sebagai bahan antara dalam sintesis ester, amida, dan senyawa organik lainnya.

    **Titik Didih:**
    - Titik didih lebih rendah daripada asam karboksilat karena tidak ada ikatan hidrogen antar molekul.
    - Namun tetap relatif tinggi karena adanya gugus karbonil polar dan halogen elektronegatif.
    - Contoh:
        - Asetil klorida (CH₃COCl): 51 °C
        - Benzoyl klorida (C₆H₅COCl): 198 °C

    **Kepolaran:** 
    - Sangat polar, karena gugus karbonil (C=O) dan C–X (X = halogen) bersifat polar.
    - Tidak larut dalam air, karena sangat reaktif → akan bereaksi dengan air (terhidrolisis) membentuk asam karboksilat dan asam halida (seperti HCl).
    - Dilarutkan dalam pelarut aprotik kering (misal: eter, diklorometana).

    **Ikatan Kimia:**
    - Mengandung:
        - 1 ikatan σ dan 1 ikatan π dalam gugus karbonil (C=O)
        - Ikatan σ pada C–Cl (atau C–Br)
    - Karbon karbonil bersifat sp² hibridisasi, dan molekulnya planar trigonal di sekitar karbon pusat.
    - Sangat elektrofilik karena kombinasi gugus karbonil dan halogen → sangat mudah diserang nukleofil.

    **Tata Nama (IUPAC):**
    - Nama berasal dari nama asam karboksilat induk, ubah akhiran -oat menjadi -oyl halida (atau -il halida dalam bentuk umum).
    - Gunakan nama halogen sebagai akhiran.

    **Contoh:**
    - CH₃COCl → Etanoil klorida (asetil klorida)
    - C₂H₅COBr → Propanoil bromida
    - C₆H₅COCl → Benzoil klorida

    **Video Penjelasan:**
    - [Video](https://youtu.be/w3j3gNN4gSs?si=L7pmPIGBTUhbvh_D)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'
        
def show_karbohidrat():
    st.title("Detail Senyawa: Karbohidrat")

    st.markdown("""
    **Deskripsi Pengetahuan Singkat:** Karbohidrat adalah senyawa organik yang terdiri dari unsur C, H, dan O, dengan rumus umum (CH₂O)n. Fungsinya sebagai sumber energi utama, bahan struktural (seperti selulosa), dan penyimpan energi (seperti pati). Karbohidrat dibagi menjadi:
    - **Monosakarida:** (glukosa, fruktosa)
    - **Disakarida:** (sukrosa, laktosa)
    - **Polisakarida:** (pati, glikogen, selulosa)

    **Titik Didih:**
    - Tidak memiliki titik didih pasti, karena karbohidrat terurai atau terkarbonisasi sebelum menguap.
    - Monosakarida dan disakarida mudah larut dalam air dan bersifat padat kristalin pada suhu ruang.

    **Kepolaran:**
    - Sangat polar, karena banyak mengandung gugus hidroksil (–OH).
    - Larut dalam air (terutama monosakarida dan disakarida) karena bisa membentuk ikatan hidrogen dengan air.
    - Polisakarida besar (seperti pati dan selulosa) tidak larut, tapi bisa menyerap air.

    **Ikatan Kimia:**
    - Tersusun dari ikatan glikosidik (C–O–C) antara gugus –OH dari dua monosakarida.
    - Gugus fungsional penting: aldehid (–CHO) atau keton (–CO) pada monosakarida.
    - Ikatan hidrogen antargugus –OH penting untuk membentuk struktur tiga dimensi (misalnya heliks pada pati).

    **Tata Nama:**
    - Monosakarida dinamai berdasarkan jumlah atom karbon + tipe gugus karbonil:
        - Aldosa (gugus aldehid) → glukosa (aldoheksosa)
        - Ketosa (gugus keton) → fruktosa (ketoheksosa)
    - Disakarida/polisakarida dinamai berdasarkan jenis dan urutan monosakaridanya:
        - Glukosa + fruktosa → sukrosa
        - Glukosa + glukosa → maltosa
        - Polimer glukosa → amilosa (dalam pati), selulosa, glikogen

    **Video Penjelasan:**
    - [Playlist](https://youtube.com/playlist?list=PLWB5gICYvKUXj77oa7c6FOtQMAXtmXSVc&si=Y_aCjbigtRXHNUdJ)
    - [Video](https://youtu.be/xynTeSAl4Ts?si=EcQIPYeB5Y5k11Mf)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'

# tampilan chatbot
def show_chatbot():
    st.title("💬 Chatbot O-KIMIAKU")
    question = st.text_input("Tanyakan sesuatu tentang senyawa kimia (misal: kepolaran ester):", key="chat_input")
    if st.button("Kirim"):
        if question:
            st.write("Pertanyaan kamu:", question)
        else:
            st.warning("Silakan masukkan pertanyaan dulu.")

    if question:
        q = question.lower()
        ditemukan= True
        if "benzena" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Benzena bersifat nonpolar dan tidak larut dalam air.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus benzena: C₆H₆.")
            elif "titik" in q:
                st.success("Titik didih benzena: 80,1 °C.")
            elif "fakta" in q:
                st.success("Benzena adalah senyawa hidrokarbon aromatik paling sederhana.")
            elif "tata nama" in q:
                st.success("Tata nama benzena: Dinamai benzena jika murni.")
            elif "ikatan" in q:
                st.success("Ikatan kimia benzena: Setiap atom C terhubung dengan dua C lain dan satu H, membentuk ikatan sigma (σ).")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Benzena di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Benzena adalah senyawa aromatik dengan struktur cincin.")
        if "keton" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Keton bersifat polar karena memiliki gugus karbonil (C=O).")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi keton: R–CO–R'.")
            elif "titik" in q:
                st.success("Titik didih keton lebih tinggi dari alkana, tetapi lebih rendah dari alkohol.")
            elif "fakta" in q:
                st.success("Keton sering ditemukan dalam pelarut dan zat aroma.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Keton di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Keton adalah senyawa organik dengan gugus karbonil di tengah rantai.")
        if "amina" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Amina bersifat polar karena adanya pasangan elektron bebas pada nitrogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi amina: R–NH₂, R–NH–R', R–N(R')–R''.")
            elif "titik" in q:
                st.success("Titik didih amina primer dan sekunder lebih tinggi dari senyawa nonpolar.")
            elif "fakta" in q:
                st.success("Amina banyak terdapat dalam senyawa biologis seperti asam amino.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Amina di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Amina adalah turunan amonia di mana satu atau lebih atom hidrogen diganti dengan gugus alkil.")
        if "asam karboksilat" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Asam karboksilat sangat polar karena mengandung gugus karbonil dan hidroksil.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi asam karboksilat: R–COOH.")
            elif "titik" in q:
                st.success("Titik didih asam karboksilat sangat tinggi karena ikatan hidrogen.")
            elif "fakta" in q:
                st.success("Asam karboksilat banyak ditemukan dalam alam, seperti dalam cuka.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Asam Karboksilat di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Asam karboksilat adalah senyawa organik dengan gugus karboksil.")
        if "amida" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Amida sangat polar karena adanya gugus karbonil dan gugus amino.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi amida: R–CONH₂.")
            elif "titik" in q:
                st.success("Titik didih amida tinggi karena dapat membentuk ikatan hidrogen.")
            elif "fakta" in q:
                st.success("Amida banyak ditemukan dalam protein.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Amida di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Amida adalah turunan dari asam karboksilat dengan gugus amina.")
        if "protein" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Protein bersifat amfipatik, mengandung bagian polar dan nonpolar.")
            elif "rumus" in q or "gugus" in q:
                st.success("Protein tersusun dari rantai panjang asam amino.")
            elif "titik" in q:
                st.success("Titik didih protein tidak relevan karena denaturasi terjadi sebelum menguap.")
            elif "fakta" in q:
                st.success("Protein berperan vital dalam struktur sel dan fungsi biologis.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Protein di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Protein adalah polimer alami yang tersusun dari asam amino.")
        if "karbohidrat" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Karbohidrat sangat polar karena banyak mengandung gugus hidroksil.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum karbohidrat: (CH₂O)n.")
            elif "titik" in q:
                st.success("Karbohidrat tidak memiliki titik didih pasti karena terurai sebelum menguap.")
            elif "fakta" in q:
                st.success("Karbohidrat berfungsi sebagai sumber energi utama.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Karbohidrat di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Karbohidrat adalah senyawa organik yang terdiri dari C, H, dan O.")
        if "lemak" in q or "minyak" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Lemak dan minyak bersifat nonpolar dan tidak larut dalam air.")
            elif "rumus" in q or "gugus" in q:
                st.success("Lemak dan minyak adalah ester dari gliserol dan asam lemak.")
            elif "titik" in q:
                st.success("Titik didih trigliserida sangat tinggi, tetapi mudah rusak saat dipanaskan.")
            elif "fakta" in q:
                st.success("Lemak jenuh biasanya padat pada suhu ruang, sedangkan minyak tak jenuh cair.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Lemak dan Minyak di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Lemak dan minyak adalah bagian dari kelompok lipid.")
        if "alkil halida" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Alkil halida bersifat polar karena perbedaan elektronegativitas antara C dan halogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum alkil halida: R–X, di mana X adalah halogen.")
            elif "titik" in q:
                st.success("Titik didih alkil halida lebih tinggi dari alkana dengan jumlah karbon setara.")
            elif "fakta" in q:
                st.success("Alkil halida digunakan dalam industri dan sebagai pelarut.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Alkil Halida di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Alkil halida adalah senyawa organik yang terbentuk dari alkana dengan menggantikan atom H dengan halogen.")
        if "nitro" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Senyawa nitro sangat polar karena gugus nitro (–NO₂).")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi nitro: –NO₂.")
            elif "titik" in q:
                st.success("Titik didih nitro umumnya tinggi karena gaya tarik dipol-dipol.")
            elif "fakta" in q:
                st.success("Senyawa nitro penting dalam bahan peledak dan sintesis kimia.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Nitro di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Senyawa nitro adalah senyawa organik yang mengandung gugus nitro.")
        if "nitril" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Nitril sangat polar karena ikatan rangkap tiga C≡N.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi nitril: –C≡N.")
            elif "titik" in q:
                st.success("Titik didih nitril lebih tinggi dari alkana karena interaksi dipol-dipol.")
            elif "fakta" in q:
                st.success("Nitril sering digunakan sebagai bahan antara dalam sintesis senyawa.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Nitril di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Nitril adalah senyawa organik yang mengandung gugus sianida.")
        if "ester" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Ester agak polar, tetapi tidak membentuk ikatan hidrogen antar molekul.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi ester: R–COOR'.")
            elif "titik" in q:
                st.success("Titik didih ester lebih rendah daripada asam karboksilat.")
            elif "fakta" in q:
                st.success("Ester sering ditemukan dalam aroma buah dan minyak esensial.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Ester di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Ester adalah senyawa turunan asam karboksilat.")
        if "asam halida" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Asam halida sangat polar karena gugus karbonil dan halogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum asam halida: R–COX, di mana X adalah halogen.")
            elif "titik" in q:
                st.success("Titik didih asam halida lebih rendah daripada asam karboksilat.")
            elif "fakta" in q:
                st.success("Asam halida sangat reaktif dan digunakan dalam sintesis.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Asam Halida di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Asam halida adalah turunan dari asam karboksilat.")
        if "alkohol" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Alkohol bersifat polar karena adanya gugus hidroksil (–OH).")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum alkohol: R–OH.")
            elif "titik" in q:
                st.success("Titik didih alkohol lebih tinggi dibandingkan alkana dan alkena.")
            elif "fakta" in q:
                st.success("Alkohol dapat larut dalam air karena membentuk ikatan hidrogen.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Alkohol di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Alkohol adalah senyawa organik yang memiliki gugus hidroksil (–OH).")
        if "fenol" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Fenol adalah senyawa polar karena adanya gugus hidroksil (–OH).")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus fenol: C₆H₅OH.")
            elif "titik" in q:
                st.success("Titik didih fenol lebih tinggi dari benzena karena ikatan hidrogen.")
            elif "fakta" in q:
                st.success("Fenol bersifat korosif dan memiliki bau khas tajam.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Fenol di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Fenol adalah senyawa aromatik yang terdiri dari cincin benzena dan gugus hidroksil.")        
        if "alkana" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Alkana adalah senyawa nonpolar karena distribusi elektron seimbang.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum alkana: CnH₂n+2.")
            elif "titik" in q:
                st.success("Titik didih alkana meningkat seiring bertambahnya jumlah atom karbon.")
            elif "fakta" in q:
                st.success("Alkana merupakan komponen utama dalam gas alam dan minyak bumi.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Alkana di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Alkana adalah senyawa hidrokarbon jenuh yang hanya mengandung ikatan tunggal.")
        if "alkena" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Alkena umumnya nonpolar, tetapi sedikit lebih polar dari alkana.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum alkena: CnH₂n.")
            elif "titik" in q:
                st.success("Titik didih alkena sedikit lebih rendah dibandingkan alkana dengan jumlah C yang sama.")
            elif "fakta" in q:
                st.success("Alkena lebih reaktif dibanding alkana karena adanya ikatan rangkap.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Alkena di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Alkena adalah senyawa hidrokarbon tak jenuh dengan setidaknya satu ikatan rangkap dua.")
        if "alkuna" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Sebagian besar alkuna adalah nonpolar.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum alkuna: CnH₂n−2.")
            elif "titik" in q:
                st.success("Titik didih alkuna meningkat seiring jumlah atom karbon.")
            elif "fakta" in q:
                st.success("Alkuna sangat reaktif dan dapat mengalami reaksi adisi.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Alkuna di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Alkuna adalah senyawa hidrokarbon tak jenuh dengan setidaknya satu ikatan rangkap tiga.")
        if "aldehid" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Aldehid sangat polar karena gugus karbonil (C=O).")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum aldehid: R–CHO.")
            elif "titik" in q:
                st.success("Titik didih aldehid lebih tinggi dari alkana, tetapi lebih rendah dari alkohol.")
            elif "fakta" in q:
                st.success("Aldehid banyak ditemukan dalam zat aroma dan sintesis organik.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Aldehid di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Aldehid adalah senyawa organik dengan gugus karbonil di ujung rantai.")
        if "eter" in q:
            ditemukan = True
            if "kepolaran" in q:
                st.success("Eter umumnya nonpolar, tetapi dapat sedikit polar tergantung pada struktur.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum eter: R–O–R′, di mana R dan R′ adalah gugus alkil.")
            elif "titik" in q:
                st.success("Titik didih eter lebih rendah dibandingkan alkohol, tetapi lebih tinggi dari alkana.")
            elif "fakta" in q:
                st.success("Eter sering digunakan sebagai pelarut dalam reaksi kimia.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Eter di YouTube](https://www.youtube.com/watch?v=example)")
            else:
                st.info("Eter adalah senyawa organik yang mengandung gugus eter (–O–) antara dua gugus alkil.")    
        if not ditemukan:
            st.warning("Maaf, hal yang kamu tanyakan bukan lingkup senyawa organik")

# tampilan quiz
def show_quiz():
    st.title("🔬 Quiz Kimia Organik – 15 Soal")

    with st.form("quiz_form"):
        st.markdown("Jawab semua pertanyaan berikut, lalu klik **Kirim Jawaban** di bawah:")

        # 15 soal dipilih dari bank soal kamu
        q1 = st.radio("1. Apa gugus fungsi utama pada alkohol?", 
                      ["-COOH", "-OH", "-NH₂", "-C=O"], key="q1")
        q2 = st.radio("2. Berapakah jumlah atom karbon pada cincin benzena?", 
                      ["4", "5", "6", "7"], key="q2")
        q3 = st.radio("3. Fenol adalah senyawa aromatik dengan gugus utama ...", 
                      ["-OH", "-COOH", "-NH₂", "-NO₂"], key="q3")
        q4 = st.radio("4. Amina adalah turunan dari ...", 
                      ["Amonia", "Benzena", "Alkohol", "Ester"], key="q4")
        q5 = st.radio("5. Amida merupakan turunan dari ...", 
                      ["Asam karboksilat", "Alkohol", "Amina", "Alkana"], key="q5")
        q6 = st.radio("6. Gugus fungsi khas pada aldehida adalah ...", 
                      ["-COOH", "-CHO", "-NH₂", "-OH"], key="q6")
        q7 = st.radio("7. Gugus fungsi nitro ditulis sebagai ...", 
                      ["-NO₂", "-COO-", "-CN", "-OH"], key="q7")
        q8 = st.radio("8. Gugus fungsi utama pada nitril adalah ...", 
                      ["-C≡N", "-COOH", "-NH₂", "-C=O"], key="q8")
        q9 = st.radio("9. Rumus umum alkana adalah ...", 
                      ["CnH₂n+2", "CnH₂n", "CnH₂n-2", "CnH₂n+1OH"], key="q9")
        q10 = st.radio("10. Alkena memiliki ikatan rangkap ...", 
                       ["dua", "tiga", "empat", "tunggal"], key="q10")
        q11 = st.radio("11. Apa ciri khas ikatan pada alkuna?", 
                       ["Ikatan rangkap tiga", "Ikatan rangkap dua", "Ikatan tunggal", "Ikatan peptida"], key="q11")
        q12 = st.radio("12. Manakah berikut ini yang termasuk monosakarida?", 
                       ["Glukosa", "Sukrosa", "Pati", "Selulosa"], key="q12")
        q13 = st.radio("13. Gugus fungsi keton terletak di ...", 
                       ["Tengah rantai karbon", "Ujung rantai karbon", "Cincin aromatik", "Gugus amina"], key="q13")
        q14 = st.radio("14. Ester terbentuk dari reaksi antara asam karboksilat dan ...", 
                       ["Alkohol", "Amina", "Keton", "Nitro"], key="q14")
        q15 = st.radio("15. Ciri utama eter adalah ...", 
                       ["Dua gugus alkil terhubung oleh oksigen", "Adanya gugus amina", "Cincin benzena", "Gugus nitro"], key="q15")

        submitted = st.form_submit_button("Kirim Jawaban")

    if submitted:
        score = 0
        explanations = []

        # Kunci jawaban dan pembahasan
        answers = {
            "q1": "-OH",
            "q2": "6",
            "q3": "-OH",
            "q4": "Amonia",
            "q5": "Asam karboksilat",
            "q6": "-CHO",
            "q7": "-NO₂",
            "q8": "-C≡N",
            "q9": "CnH₂n+2",
            "q10": "dua",
            "q11": "Ikatan rangkap tiga",
            "q12": "Glukosa",
            "q13": "Tengah rantai karbon",
            "q14": "Alkohol",
            "q15": "Dua gugus alkil terhubung oleh oksigen"
        }

        explanations = {
            "q1": "Gugus fungsi utama pada alkohol adalah -OH, yang memberikan sifat polar dan kemampuan membentuk ikatan hidrogen.",
            "q2": "Cincin benzena terdiri dari 6 atom karbon yang terikat dalam struktur planar.",
            "q3": "Fenol memiliki gugus -OH yang membuatnya bersifat asam lemah.",
            "q4": "Amina adalah turunan dari amonia, di mana satu atau lebih atom hidrogen diganti dengan gugus alkil.",
            "q5": "Amida adalah turunan dari asam karboksilat, di mana gugus -OH diganti dengan -NH₂.",
            "q6": "Gugus fungsi khas pada aldehida adalah -CHO, yang terletak di ujung rantai karbon.",
            "q7": "Gugus fungsi nitro ditulis sebagai -NO₂, yang memberikan sifat polar pada senyawa.",
            "q8": "Gugus fungsi utama pada nitril adalah -C≡N, yang memberikan sifat polar.",
            "q9": "Rumus umum alkana adalah CnH₂n+2, yang menunjukkan bahwa alkana adalah hidrokarbon jenuh.",
            "q10": "Alkena memiliki ikatan rangkap dua, yang membuatnya lebih reaktif dibandingkan alkana.",
            "q11": "Ciri khas ikatan pada alkuna adalah ikatan rangkap tiga, yang membuatnya sangat reaktif.",
            "q12": "Glukosa adalah contoh monosakarida, yang merupakan unit dasar karbohidrat.",
            "q13": "Gugus fungsi keton terletak di tengah rantai karbon, berbeda dengan aldehida yang di ujung.",
            "q14": "Ester terbentuk dari reaksi antara asam karboksilat dan alkohol, menghasilkan senyawa yang memiliki aroma.",
            "q15": "Ciri utama eter adalah dua gugus alkil terhubung oleh oksigen, yang membuatnya bersifat nonpolar."
        }

        # Hitung skor dan tampilkan pembahasan
        for i in range(1, 16):
            user_answer = locals()[f'q{i}']
            correct_answer = answers[f'q{i}']
            if user_answer == correct_answer:
                score += 1
            else:
                st.warning(f"Jawaban {i} salah! {explanations[f'q{i}']}")

        st.success(f"Skor akhir kamu: {score} / 15")
        if score == 15:
            st.balloons()
            st.info("Sempurna! Semua jawaban benar 🎉")
        elif score >= 12:
            st.info("Hebat! Kamu paham betul senyawa kimia organik 👏")
        elif score >= 8:
            st.info("Bagus! Terus belajar dan tingkatkan pemahaman 💪")
        else:
            st.warning("Yuk belajar lagi. Jangan menyerah! 📘")
            
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'

# tampilan about us
def show_about():
    st.title("Tentang Kami 👨‍💻")
    st.markdown("""
**Developer:**  
KELOMPOK 11 KELAS 1C 
1. Nama : Azizah Putri Azzahra (2460340)  
2. Nama : Aszharra Kusumaningtyas (2460336)
3. Nama : Nadifah Adya Anggita (2460449)
4. Nama : Raudhatul Dahlia (2460493)
5. Nama : Zahira Dwi Safitri (2460542) 
   
Kami membuat aplikasi ini untuk mempermudah pembelajaran kimia dengan cara yang interaktif.
""")
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'

# tampilan rating
def show_rating():
    st.title("Rating aplikasi ini ⭐")
    st.markdown("""
    Terimakasih telah menggunakan O-KimiaKu, tolong beri pendapat dan masukan kamu agar O-KimiaKu makin berkembang! 😊
    
    **Kirimkan pendapat kamu melalui link dibawah ini:**
    
    [link rating O-KimiaKu⭐](https://forms.gle/KRoCrL1Vmngdv2SR6)
    """)
    
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state.page = 'home'

# ------------- UI & PAGE CONTROL --------------
if 'page' not in st.session_state:
    st.session_state.page = 'home'
        
# Sidebar Navigasi TANPA LINGKARAN
st.sidebar.title("📚 Navigasi")

if st.sidebar.button("🏠 Beranda"):
    st.session_state.page = 'home'

if st.sidebar.button("📝 Quiz"):
    st.session_state.page = 'quiz'

if st.sidebar.button("💬 Chatbot"):
    st.session_state.page = 'chatbot'

if st.sidebar.button("👥 About Us"):
    st.session_state.page = 'about'
    
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
elif st.session_state.page == 'alkil_halida':
    show_alkil_halida()
elif st.session_state.page == 'nitril':
    show_nitril()
elif st.session_state.page == 'aldehida':
    show_aldehida()
elif st.session_state.page == 'nitro':
    show_nitro()
elif st.session_state.page == 'keton':
    show_keton()
elif st.session_state.page == 'asam_halida':
    show_asam_halida()
elif st.session_state.page == 'ester':
    show_ester()
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
elif st.session_state.page == 'asam_karboksilat':
    show_asam_karboksilat()
elif st.session_state.page == 'amida':
    show_amida()
elif st.session_state.page == 'protein':
    show_protein()
elif st.session_state.page == 'lemak_dan_minyak':
    show_lemak_dan_minyak()
elif st.session_state.page == 'eter':
    show_eter()
elif st.session_state.page == 'karbohidrat':
    show_karbohidrat()
elif st.session_state.page == 'quiz':
    show_quiz()
