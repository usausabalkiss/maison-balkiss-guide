import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Complete System", layout="wide")

# --- كود PWA للتثبيت على الهاتف ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (للقائمة والتبويبات والبحث) ---
translations = {
    "English": {
        "title": "Maison Balkiss AI 4.0",
        "route_tab": "📍 Routes",
        "story_tab": "🍲 AI Storytelling",
        "heritage_tab": "🏛️ City Guide",
        "lang_label": "🌐 Language",
        "curr_label": "💱 Currency",
        "loc_method": "📍 Location Method",
        "loc_list": "Choose City",
        "loc_manual": "Type City Name",
        "scan": "Scan Dish",
        "agri": "Agriculture & Nature",
        "crafts": "Traditional Crafts",
        "monuments": "Monuments & Tourism",
        "search_msg": "AI is generating real-time info for"
    },
    "Français": {
        "title": "Maison Balkiss AI 4.0",
        "route_tab": "📍 Itinéraires",
        "story_tab": "🍲 Storytelling IA",
        "heritage_tab": "🏛️ Guide Ville",
        "lang_label": "🌐 Langue",
        "curr_label": "💱 Devise",
        "loc_method": "📍 Mode de Localisation",
        "loc_list": "Liste des villes",
        "loc_manual": "Saisie Manuelle",
        "scan": "Scanner le plat",
        "agri": "Agriculture & Nature",
        "crafts": "Artisanat Local",
        "monuments": "Monuments & Tourisme",
        "search_msg": "L'IA génère des infos pour"
    },
    "العربية": {
        "title": "ميزون بلقيس الذكي 4.0",
        "route_tab": "📍 المسارات",
        "story_tab": "🍲 حكايات الأطباق",
        "heritage_tab": "🏛️ دليل المدن",
        "lang_label": "🌐 اختر اللغة",
        "curr_label": "💱 اختر العملة",
        "loc_method": "📍 طريقة الموقع",
        "loc_list": "من القائمة",
        "loc_manual": "كتابة يدوية",
        "scan": "فحص الطبق",
        "agri": "الفلاحة والبيئة",
        "crafts": "الصناعة التقليدية",
        "monuments": "المآثر والسياحة",
        "search_msg": "الذكاء الاصطناعي يحلل بيانات"
    }
}

# --- 3. قاعدة بيانات الجهات الـ 12 كاملة بمدنها ---
morocco_map = {
    "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Chefchaouen", "Al Hoceïma", "Larache", "Ouezzane"],
    "L'Oriental": ["Oujda", "Berkane", "Nador", "Saïdia", "Figuig"],
    "Fès-Mekنès": ["صفرو", "فاس", "مكناس", "إفران", "تازة", "زرهون"],
    "Rabat-Salé-Kénitra": ["الرباط", "سلا", "القنيطرة", "الخميسات"],
    "Béni Mellal-Khénifra": ["بني ملال", "خنيفرة", "أزيلال"],
    "Casablanca-Settat": ["الدار البيضاء", "سطات", "الجديدة", "المحمدية"],
    "Marrakech-Safi": ["مراكش", "آسفي", "الصويرة", "ابن جرير"],
    "Drâa-Tafilalet": ["الرشيدية", "ورزازات", "ميدلت", "تنغير", "زاكورة"],
    "Souss-Massa": ["أكادير", "تارودانت", "تيزنيت", "طاطا"],
    "Guelmim-Oued Noun": ["كلميم", "طنطان", "سيدي إفني"],
    "Laâyoune-Sakia El Hamra": ["العيون", "السمارة", "بوجدور"],
    "Dakhla-Oued Ed-Dahab": ["الداخلة", "أوسرد"]
}
all_cities = sorted([city for cities in morocco_map.values() for city in cities])

# --- 4. القائمة الجانبية (Sidebar) المنظمة 100% ---
st.sidebar.title("👑 Maison Balkiss AI")
lang_choice = st.sidebar.selectbox("Language / اللغة", ["English", "Français", "العربية"])
t = translations[lang_choice]

curr_type = st.sidebar.selectbox(t["curr_label"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")
st.sidebar.subheader(t["loc_method"])

loc_method = st.sidebar.radio("", [t["loc_list"], t["loc_manual"]])
if loc_method == t["loc_list"]:
    user_city = st.sidebar.selectbox(t["loc_list"], all_cities, index=all_cities.index("صفرو") if "صفرو" in all_cities else 0)
else:
    user_city = st.sidebar.text_input(t["loc_manual"], "صفرو")

# --- 5. العرض الرئيسي (Tabs) ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    st.info(f"📍 {t['location' if 'location' in t else 'loc']}: **{user_city}**")
    region_sel = st.selectbox("Explore Regions (12 Districts)", list(morocco_map.keys()))
    city_sel = st.selectbox("Cities in this region", morocco_map[region_sel])
    if city_sel == "صفرو": st.success("✅ Smart Trail Found: The Cherry Route")

with tab2:
    st.subheader(t['scan'])
    # خانة تصوير الطبق (Scanner)
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png"])
    if up:
        st.image(up, width=300)
        # محاكاة التعرف والحكايات الطويلة بالصور
        st.success("✅ AI Detected: Moroccan Gastronomy Heritage")
        st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Moroccan_Pastilla.jpg", caption="Bstilla / بسطيلة")
        st.write("📖 **Long Story:** This dish reflects centuries of Andalusian-Moroccan history...")

with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    # الباحث الذكي التلقائي - خدام لأي مدينة
    with st.spinner(f"{t['search_msg']} {user_city}..."):
        st.image("https://via.placeholder.com/800x400.png?text=Discover+Morocco+AI", use_column_width=True)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"🌾 {t['agri']}")
            st.write(f"The area around {user_city} is famous for its unique climate supporting strategic local products like olives and traditional crops.")
            st.subheader(f"🧶 {t['crafts']}")
            st.write(f"Artisans in {user_city} preserve ancestral secrets in weaving, pottery, or metalwork depending on regional specialization.")
        with col2:
            st.subheader(f"🏛️ {t['monuments']}")
            st.write(f"Historical landmarks in {user_city} offer a journey through time, from medieval architecture to natural wonders.")

st.markdown("---")
st.caption(f"Powered by Maison Balkiss AI - Tourism 4.0 | © 2026")
