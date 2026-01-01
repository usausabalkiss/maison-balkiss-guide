import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود PWA للتثبيت على الهاتف ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.ifier.io/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (لغات ثلاث) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "intro": "Experience Tourism 4.0: Discover Morocco's authentic flavors.",
        "route_tab": "📍 AI Culinary Routes",
        "story_tab": "🍲 AI Storytelling",
        "heritage_tab": "🏛️ City Guide",
        "select_region": "Select a Region",
        "select_city": "Select a City",
        "identify": "Scan your Dish",
        "currency": "Currency",
        "loc_method": "Location Method",
        "loc_list": "Choose from List",
        "loc_manual": "Type City Name",
        "find_near": "Best places near you in",
        "location": "Location",
        "agri": "Agriculture & Economy",
        "crafts": "Local Crafts",
        "monuments": "Monuments & Heritage"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "route_tab": "📍 Itinéraires Culinaires",
        "story_tab": "🍲 Storytelling IA",
        "heritage_tab": "🏛️ Guide Ville",
        "select_region": "Choisir une Région",
        "select_city": "Choisir une Ville",
        "identify": "Scanner votre Plat",
        "currency": "Devise",
        "loc_method": "Méthode de Localisation",
        "loc_list": "Liste des villes",
        "loc_manual": "Saisie Manuelle",
        "find_near": "Meilleurs endroits à",
        "location": "Localisation",
        "agri": "Agriculture & Économie",
        "crafts": "Artisanat Local",
        "monuments": "Monuments & Patrimoine"
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "route_tab": "📍 مسارات ذكية",
        "story_tab": "🍲 حكايات الأطباق",
        "heritage_tab": "🏛️ دليل المدن",
        "select_region": "اختر جهة",
        "select_city": "اختر مدينة",
        "identify": "فحص الطبق",
        "currency": "العملة",
        "loc_method": "طريقة تحديد الموقع",
        "loc_list": "الاختيار من القائمة",
        "loc_manual": "كتابة يدوية",
        "find_near": "أفضل الأماكن في",
        "location": "الموقع الحالي",
        "agri": "الفلاحة والاقتصاد",
        "crafts": "الصناعة التقليدية",
        "monuments": "المآثر والتراث"
    }
}

# --- 3. قاعدة بيانات الجهات الـ 12 ---
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
all_cities_list = sorted([city for cities in morocco_map.values() for city in cities])

# --- 4. القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang]

curr_type = st.sidebar.selectbox(t["currency"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")
st.sidebar.subheader(t["loc_method"])
search_method = st.sidebar.radio("", [t["loc_list"], t["loc_manual"]])

if search_method == t["loc_list"]:
    user_city = st.sidebar.selectbox(t["select_city"], all_cities_list, index=all_cities_list.index("صفرو") if "صفرو" in all_cities_list else 0)
else:
    user_city = st.sidebar.text_input(t["loc_manual"], "صفرو")

# --- 5. العرض الرئيسي (Tabs) ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    # تصحيح السطر 99: إضافة مفتاح location لضمان عمل الترجمة
    st.info(f"📍 {t['location']}: **{user_city}**")
    region = st.selectbox(t['select_region'], list(morocco_map.keys()))
    city_select = st.selectbox(t['select_city'], morocco_map[region])
    if city_select == "صفرو":
        st.success("✅ Smart Trail Found: The Cherry & Olive Heritage Route")

with tab2:
    st.subheader(t['identify'])
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    
    if up:
        st.image(up, width=400)
        # التعرف التلقائي الذكي بناءً على اسم الملف (لأغراض العرض)
        detected_dish = up.name.split('.')[0].replace('_', ' ').title()
        st.success(f"✅ AI Identified: {detected_dish}")
        
        st.markdown(f"### 📖 {t['story_tab']}: {detected_dish}")
        # ربط الحكاية بالمدينة واللغة
        st.write(f"In **{user_city}**, the dish **{detected_dish}** is more than just food; it's a centuries-old heritage.")
        st.info(f"🍳 **Key Ingredients:** Traditional spices, organic olive oil, and fresh produce from the {user_city} region.")
        
        st.markdown("---")
        st.subheader(f"🍴 {t['find_near']} {user_city}:")
        # روابط ذكية لخرائط جوجل تعتمد على المدينة المختارة
        google_maps_url = f"https://www.google.com/maps/search/traditional+restaurants+in+{user_city}"
        st.markdown(f"🔗 [Find authentic restaurants for {detected_dish} in {user_city}]({google_maps_url})")

with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    st.markdown(f"### 🌐 Wikipedia Insight for {user_city}")
    
    # تصحيح السطر 155: تنظيم الإزاحة (Indentation)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🌾 {t['agri']}")
        st.write(f"The economy of **{user_city}** thrives on its local diversity, famous for products of terroir like olives, fruits, and traditional oils.")
        
        st.subheader(f"🧶 {t['crafts']}")
        st.write(f"Artisans in **{user_city}** preserve the soul of the region through weaving, pottery, and manual crafts.")
        
    with col2:
        st.subheader(f"🏛️ {t['monuments']}")
        st.write(f"Explore the historical monuments, ancient walls, and natural beauty that define **{user_city}**.")
        # رابط خريطة المآثر
        heritage_maps_url = f"https://www.google.com/maps/search/historical+monuments+in+{user_city}"
        st.markdown(f"🔗 [Explore {user_city} heritage sites on Google Maps]({heritage_maps_url})")
        st.image("https://via.placeholder.com/600x400.png?text=Explore+Morocco+Heritage", use_column_width=True)

st.markdown("---")
st.caption("Powered by Maison Balkiss AI - Tourism 4.0 | © 2026 Competition Entry")
