import streamlit as st
import webbrowser

# Page configuration
st.set_page_config(
    page_title="Portal Navigasi Sekolah",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .nav-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 1rem 0;
        border: 2px solid #f0f2f6;
        transition: all 0.3s ease;
    }
    
    .nav-card:hover {
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
        border-color: #667eea;
    }
    
    .nav-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .nav-title {
        color: #2c3e50;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .nav-description {
        color: #7f8c8d;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #7f8c8d;
        font-size: 0.9rem;
        border-top: 1px solid #ecf0f1;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏫 Portal Navigasi Sekolah</h1>
    <p>Akses mudah kepada maklumat dan sumber sekolah</p>
</div>
""", unsafe_allow_html=True)

# Navigation options data
nav_options = [
    {
        "icon": "📊",
        "title": "Carta Organisasi",
        "description": "Struktur organisasi dan hierarki sekolah",
        "url": "https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit#gid=0",  # Replace with your Google Sheet URL
        "button_text": "Lihat Carta Organisasi"
    },
    {
        "icon": "🎥",
        "title": "Video Maklumat",
        "description": "Video pengenalan dan maklumat penting sekolah",
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Replace with your YouTube URL
        "button_text": "Tonton Video"
    },
    {
        "icon": "📚",
        "title": "PSS (Portal Sistem Sekolah)",
        "description": "Akses kepada sistem pengurusan sekolah",
        "url": "https://www.example.com/pss",  # Replace with your PSS URL
        "button_text": "Masuk ke PSS"
    },
    {
        "icon": "🔗",
        "title": "Lain-lain",
        "description": "Pautan dan maklumat tambahan",
        "url": "https://www.example.com/others",  # Replace with your other links URL
        "button_text": "Lihat Lain-lain"
    }
]

# Create navigation grid
col1, col2 = st.columns(2)

for i, option in enumerate(nav_options):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="nav-card">
            <div class="nav-icon">{option['icon']}</div>
            <div class="nav-title">{option['title']}</div>
            <div class="nav-description">{option['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(option['button_text'], key=f"btn_{i}", use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0; url={option["url"]}">', unsafe_allow_html=True)
            st.success(f"Membuka {option['title']}...")
            st.markdown(f"**Klik pautan ini jika tidak diarahkan secara automatik:** [{option['title']}]({option['url']})")

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Quick access section
st.subheader("🚀 Akses Pantas")

quick_col1, quick_col2, quick_col3, quick_col4 = st.columns(4)

with quick_col1:
    if st.button("📞 Hubungi Pejabat", use_container_width=True):
        st.info("📞 Nombor Telefon: +60 3-XXXX XXXX")

with quick_col2:
    if st.button("📧 E-mel Sekolah", use_container_width=True):
        st.info("📧 E-mel: info@sekolah.edu.my")

with quick_col3:
    if st.button("📍 Lokasi Sekolah", use_container_width=True):
        st.info("📍 Alamat sekolah dan peta lokasi")

with quick_col4:
    if st.button("⏰ Waktu Operasi", use_container_width=True):
        st.info("⏰ Isnin - Jumaat: 7:30 AM - 2:30 PM")

# Footer
st.markdown("""
<div class="footer">
    <p>© 2024 Portal Navigasi Sekolah | Dicipta untuk kemudahan akses maklumat sekolah</p>
    <p>💡 <strong>Tip:</strong> Bookmark halaman ini untuk akses yang lebih mudah!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional info
st.sidebar.markdown("## ℹ️ Maklumat Tambahan")
st.sidebar.info("""
**Cara Menggunakan Portal:**
1. Pilih kategori yang anda ingin akses
2. Klik butang untuk membuka pautan
3. Anda akan diarahkan ke laman yang berkaitan

**Sokongan Teknikal:**
Jika menghadapi masalah, sila hubungi unit IT sekolah.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 Akses Mudah Alih")
st.sidebar.info("Portal ini dioptimumkan untuk penggunaan pada telefon bimbit dan tablet.")

# Add some analytics tracking (optional)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Statistik Penggunaan")
if st.sidebar.button("Lihat Statistik"):
    st.sidebar.success("Ciri ini akan tersedia tidak lama lagi!")
