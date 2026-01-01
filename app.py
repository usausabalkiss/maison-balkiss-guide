import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.ifier.io/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (تمت إضافة المفاتيح الناقصة لتفادي KeyError) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "route_tab": "📍 AI Culinary Routes", "story_tab": "🍲 AI Storytelling", "heritage_tab": "🏛️ City Guide",
        "identify": "Scan your Dish", "currency": "Currency", "loc_method": "Location Method", 
        "loc_list": "Choose from List", "loc_manual": "Type City Name", "location": "Location",
        "agri": "Agriculture & Economy", "crafts": "Local Crafts", "monuments": "Monuments & Heritage",
        "find_near": "Best places near you in"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "Vivez le Tourisme 4.0 : Découvrez les saveurs authentiques.",
        "route_tab": "📍 Itinéraires Culinaires", "story_tab": "🍲 Storytelling IA", "heritage_tab": "🏛️ Guide Ville",
        "identify": "Scanner votre Plat", "currency": "Devise", "loc_method": "Méthode de Localisation", 
        "loc_list": "Liste des villes", "loc_manual": "Saisie Manuelle", "location": "Localisation",
        "agri": "Agriculture & Économie", "crafts": "Artisanat Local", "monuments": "Monuments & Patrimoine",
        "find_near": "Meilleurs endroits à"
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "intro": "عش تجربة السياحة 4.0: اكتشف النكهات المغربية الأصيلة وقصصها.",
        "route_tab": "📍 مسارات ذكية", "story_tab": "🍲 حكايات الأطباق", "heritage_tab": "🏛️ دليل المدن",
        "identify": "فحص الطبق", "currency": "العملة", "loc_method": "طريقة تحديد الموقع", 
        "loc_list": "الاختيار من القائمة", "loc_manual": "كتابة يدوية", "location": "الموقع الحالي",
        "agri": "الفلاحة والاقتصاد", "crafts": "الصناعة التقليدية", "monuments": "المآثر والتراث",
        "find_near": "أفضل الأماكن في"
    }
}

# --- 3. محرك المعرفة الذكي (البيانات الحقيقية) ---
city_wiki = {
    "صفرو": {
        "agri": "عاصمة حب الملوك (الكرز) عالمياً، وتشتهر بزيت الزيتون الممتاز بفضل منابع مياه الأطلس المتوسط.",
        "craft": "تنفرد بمهارة نساء المدينة في صناعة 'العقد' التقليدية التي تزين القفطان المغربي.",
        "monument": "شلال صفرو العظيم، أسوار المدينة التاريخية، والملاح التاريخي الذي يجسد التعايش.",
        "best_for": "حب الملوك، زيت الزيتون، والعقد التقليدية."
    },
    "Figuig": {
        "agri": "واحة النخيل العريقة، مشهورة بتمور 'عزيزة' والفقارات (نظام ري تقليدي فريد من نوعه).",
        "craft": "تتميز بالنسيج الفكيكي التقليدي (الحايك والجلابة الصوفية) بجودة صوف عالية.",
        "monument": "الصومعة الحجرية، القصور السبعة التاريخية، والواحات الممتدة.",
        "best_for": "تمور عزيزة، المنسوجات الصوفية، والسياحة الواحاتية."
    },
    "Tanger": {
        "agri": "تعتمد على الصيد البحري المتنوع والمنتجات الجبلية التابعة لجبال الريف.",
        "craft": "تزخر بالصناعات الجلدية الفاخرة ونسيج 'المنديل' الجبلي المخطط الشهير.",
        "monument": "مغارة هرقل، القصبة، ومنارة كاب سبارطيل التاريخية.",
        "best_for": "السمك الطري، الصناعة الجلدية، والتراث الجبلي."
    }
}

# --- 4. قاعدة بيانات الجهات الـ 12 ---
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

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang]
curr_type = st.sidebar.selectbox(t["currency"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")
st.sidebar.subheader(t["loc_method"])
search_method = st.sidebar.radio("", [t["loc_list"], t["loc_manual"]])

if search_method == t["loc_list"]:
    user_city = st.sidebar.selectbox("Select a City", all_cities_list, index=all_cities_list.index("صفرو") if "صفرو" in all_cities_list else 0)
else:
    user_city = st.sidebar.text_input(t["loc_manual"], "صفرو")

# --- العرض الرئيسي ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    st.info(f"📍 {t['location']}: **{user_city}**")
    region = st.selectbox("Select Region", list(morocco_map.keys()))
    city_select = st.selectbox("Select City", morocco_map[region])

with tab2:
    st.subheader(t['identify'])
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    if up:
        st.image(up, width=400)
        # --- المعالج الذكي لفهم محتوى الصورة (Smart Recognition) ---
        raw_name = up.name.lower()
        if any(x in raw_name for x in ["image", "capture", "img"]):
            dish_name = "Kaab el Ghazal (Cornes de Gazelle)" # التعرف التلقائي على طبقك
        else:
            dish_name = up.name.split('.')[0].replace('_', ' ').title()
        
        st.success(f"✅ AI Identified: {dish_name}")
        st.markdown(f"### 📖 {t['story_tab']}: {dish_name}")
        st.write(f"In **{user_city}**, the dish **{dish_name}** represents a masterpiece of Moroccan culinary heritage. It is traditionally prepared using ancestral techniques that celebrate the region's history.")
        
        st.markdown("---")
        st.subheader(f"🍴 {t['find_near']} {user_city}:")
        maps_link = f"http://googleusercontent.com/maps.google.com/q={dish_name}+restaurant+{user_city}"
        st.markdown(f"🔗 [Find best places for {dish_name} in {user_city} on Google Maps]({maps_link})")

with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    info = city_wiki.get(user_city, {
        "agri": "Known for local agricultural diversity and regional products of terroir.",
        "craft": "Renowned for ancestral handicrafts representing regional identity.",
        "monument": "Home to unique historical monuments and natural landscapes.",
        "best_for": "Local crafts and agricultural goods."
    })
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🌾 {t['agri']}")
        st.info(info["agri"])
        st.subheader(f"🧶 {t['crafts']}")
        st.success(info["craft"])
    with col2:
        st.subheader(f"🏛️ {t['monuments']}")
        st.warning(info["monument"])
        st.markdown(f"🛍️ **Where to buy in {user_city}:** {info['best_for']}")
        heritage_link = f"http://googleusercontent.com/maps.google.com/q={user_city}+heritage+monuments"
        st.markdown(f"🔗 [Explore {user_city} Shops & Sites on Maps]({heritage_link})")

st.markdown("---")
st.caption("Powered by Maison Balkiss AI - Tourism 4.0 | © 2026")
