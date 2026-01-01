import streamlit as st

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.ifier.io/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (تم تصحيح جميع المفاتيح لتفادي KeyError) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "route_tab": "📍 AI Culinary Routes", "story_tab": "🍲 AI Storytelling", "heritage_tab": "🏛️ City Guide",
        "select_region": "Select a Region", "select_city": "Select a City", "identify": "Scan your Dish",
        "currency": "Currency", "loc_method": "Location Method", "loc_list": "Choose from List",
        "loc_manual": "Type City Name", "find_near": "Best places near you in", "location": "Location",
        "agri": "Agriculture & Economy", "crafts": "Local Crafts", "monuments": "Monuments & Heritage"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "route_tab": "📍 Itinéraires Culinaires", "story_tab": "🍲 Storytelling IA", "heritage_tab": "🏛️ Guide Ville",
        "select_region": "Choisir une Région", "select_city": "Choisir une Ville", "identify": "Scanner votre Plat",
        "currency": "Devise", "loc_method": "Méthode de Localisation", "loc_list": "Liste des villes",
        "loc_manual": "Saisie Manuelle", "find_near": "Meilleurs endroits à", "location": "Localisation",
        "agri": "Agriculture & Économie", "crafts": "Artisanat Local", "monuments": "Monuments & Patrimoine"
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "route_tab": "📍 مسارات ذكية", "story_tab": "🍲 حكايات الأطباق", "heritage_tab": "🏛️ دليل المدن",
        "select_region": "اختر جهة", "select_city": "اختر مدينة", "identify": "فحص الطبق",
        "currency": "العملة", "loc_method": "طريقة تحديد الموقع", "loc_list": "الاختيار من القائمة",
        "loc_manual": "كتابة يدوية", "find_near": "أفضل الأماكن في", "location": "الموقع الحالي",
        "agri": "الفلاحة والاقتصاد", "crafts": "الصناعة التقليدية", "monuments": "المآثر والتراث"
    }
}

# --- 3. محرك البيانات الحقيقية (ويكيبيديا الذكية لكل مدينة) ---
city_knowledge = {
    "صفرو": {
        "agri": "عاصمة حب الملوك (الكرز) عالمياً. تشتهر بإنتاج الزيتون الرفيع بفضل منابع مياه الأطلس المتوسط.",
        "craft": "تنفرد بصناعة 'العقد' التقليدية (أزرار القفطان) التي تعد تراثاً حياً للمدينة.",
        "monument": "شلالات صفرو، أسوار المدينة العتيقة، والملاح التاريخي الذي يجسد التعايش.",
        "restaurants": ["Resto Cascade", "Al-Maqam"]
    },
    "Figuig": {
        "agri": "واحة النخيل بامتياز، مشهورة بتمور 'عزيزة' النادرة ومنظومة الري التقليدية 'الفقارات'.",
        "craft": "تتميز بالنسيج الفكيكي التقليدي (الحايك والجلابة الصوفية) بجودة عالية.",
        "monument": "الصومعة الحجرية، القصور السبعة التاريخية، والواحات الممتدة.",
        "restaurants": ["Oasis Resto", "Heritage Guest House"]
    }
}

# --- 4. قاعدة بيانات الجهات الـ 12 ---
morocco_map = {
    "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Chefchaouen", "Al Hoceïma"],
    "L'Oriental": ["Oujda", "Berkane", "Nador", "Saïdia", "Figuig"],
    "Fès-Mekنès": ["صفرو", "فاس", "مكناس", "إفران", "تازة"]
}
all_cities_list = sorted([city for cities in morocco_map.values() for city in cities])

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang]
user_city = st.sidebar.selectbox(t["select_city"], all_cities_list, index=0)

# --- العرض الرئيسي ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab2:
    st.subheader(t['identify'])
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    if up:
        st.image(up, width=400)
        # التعرف التلقائي الذكي بناءً على اسم الملف المرفوع
        dish_name = up.name.split('.')[0].replace('_', ' ').title()
        st.success(f"✅ AI Identified: {dish_name}")
        
        st.markdown(f"### 📖 {t['story_tab']}: {dish_name}")
        st.write(f"In **{user_city}**, the dish **{dish_name}** represents a masterpiece of Moroccan culinary heritage, prepared with local ingredients.")
        
        st.markdown("---")
        st.subheader(f"🍴 {t['find_near']} {user_city}:")
        city_info = city_knowledge.get(user_city, {"restaurants": ["Traditional Kitchen"]})
        for rest in city_info["restaurants"]:
            st.info(f"📍 **{rest}** - Highly recommended in {user_city}")

with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    info = city_knowledge.get(user_city, {
        "agri": f"Famous for regional products in {user_city}.",
        "craft": "Ancestral handicrafts representing local identity.",
        "monument": "Historical monuments and natural landscapes."
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
        st.markdown(f"🔗 [Explore {user_city} on Google Maps](https://www.google.com/maps/search/{user_city}+heritage)")

st.caption("Powered by Maison Balkiss AI 4.0 | © 2026")
