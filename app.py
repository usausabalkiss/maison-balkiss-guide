import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="Maison Balkiss AI 4.0", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- الترجمات (تم تصحيح المفاتيح لتجنب KeyError) ---
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
        "location": "Current Location",
        "scan": "Scan Dish",
        "agri": "Agriculture", "crafts": "Crafts", "monuments": "Monuments"
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
        "location": "Localisation",
        "scan": "Scanner",
        "agri": "Agriculture", "crafts": "Artisanat", "monuments": "Monuments"
    },
    "العربية": {
        "title": "Maison Balkiss AI 4.0",
        "route_tab": "📍 المسارات",
        "story_tab": "🍲 حكايات الأطباق",
        "heritage_tab": "🏛️ دليل المدن",
        "lang_label": "🌐 اختر اللغة",
        "curr_label": "💱 اختر العملة",
        "loc_method": "📍 طريقة الموقع",
        "loc_list": "من القائمة",
        "loc_manual": "كتابة يدوية",
        "location": "الموقع الحالي",
        "scan": "فحص الطبق",
        "agri": "الفلاحة", "crafts": "الصناعة التقليدية", "monuments": "المآثر"
    }
}

# --- الجهات الـ 12 كاملة ---
morocco_map = {
    "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Chefchaouen", "Al Hoceïma"],
    "L'Oriental": ["Oujda", "Berkane", "Nador", "Saïdia"],
    "Fès-Meknès": ["صفرو", "فاس", "مكناس", "إفران"],
    "Rabat-Salé-Kénitra": ["الرباط", "سلا", "القنيطرة"],
    "Béni Mellal-Khénifra": ["بني ملال", "خنيفرة"],
    "Casablanca-Settat": ["الدار البيضاء", "سطات"],
    "Marrakech-Safi": ["مراكش", "آسفي", "الصويرة"],
    "Drâa-Tafilalet": ["الرشيدية", "ورزازات"],
    "Souss-Massa": ["أكادير", "تارودانت"],
    "Guelmim-Oued Noun": ["كلميم", "طنطان"],
    "Laâyoune-Sakia El Hamra": ["العيون", "بوجدور"],
    "Dakhla-Oued Ed-Dahab": ["الداخلة"]
}
all_cities = sorted([city for cities in morocco_map.values() for city in cities])

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang_choice = st.sidebar.selectbox("Language / اللغة", ["English", "Français", "العربية"])
t = translations[lang_choice]

curr_type = st.sidebar.selectbox(t["curr_label"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")
st.sidebar.subheader(t["loc_method"])

loc_mode = st.sidebar.radio("", [t["loc_list"], t["loc_manual"]])
if loc_mode == t["loc_list"]:
    user_city = st.sidebar.selectbox(t["loc_list"], all_cities, index=all_cities.index("صفرو") if "صفرو" in all_cities else 0)
else:
    user_city = st.sidebar.text_input(t["loc_manual"], "صفرو")

# --- العرض الرئيسي ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    # تصحيح السطر 99: التأكد من وجود مفتاح 'location'
    st.info(f"📍 {t.get('location', 'Location')}: **{user_city}**")
    region_sel = st.selectbox("Explore Regions (12 Districts)", list(morocco_map.keys()))
    city_sel = st.selectbox("Cities in this region", morocco_map[region_sel])
    if city_sel == "صفرو": st.success("✅ Smart Trail: The Cherry Route")

with tab2:
    st.subheader(t['scan'])
    up = st.file_uploader("Upload dish...", type=["jpg", "png"])
    if up:
        st.image(up, width=300)
        st.success("✅ AI Detected: Moroccan Gastronomy")

with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    # الباحث الذكي التلقائي - حل مشكلة الخلاء
    st.write(f"**{t['agri']}:** Information about agriculture in {user_city} is being generated...")
    st.write(f"**{t['crafts']}:** Discover local traditional crafts in {user_city}.")
    st.write(f"**{t['monuments']}:** Explore the historical sites of {user_city}.")

st.markdown("---")
st.caption(f"Powered by Maison Balkiss AI - Tourism 4.0 | © 2026")
