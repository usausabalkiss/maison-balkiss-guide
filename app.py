import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل المغربي
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود PWA للتثبيت على الهاتف ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 1. قاعدة بيانات الجهات والمدن المغربية (الـ 12 كاملة) ---
morocco_map = {
    "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Chefchaouen", "Al Hoceïma", "Larache", "Ouezzane"],
    "L'Oriental": ["Oujda", "Berkane", "Nador", "Saïdia", "Figuig"],
    "Fès-Meknès": ["صفرو", "فاس", "مكناس", "إفران", "تازة", "مولاي إدريس زرهون"],
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

# --- 2. قاعدة بيانات البحث الذكي (فلاحة، صناعة، مآثر، قصص) ---
city_intel = {
    "صفرو": {
        "agri": "عاصمة حب الملوك (الكرز) عالمياً، وتشتهر بجودة الزيتون والتين المحلي.",
        "craft": "صناعة 'العقد' التقليدية الخاصة بالقفطان، والنسيج اليدوي.",
        "monument": "شلالات صفرو، الملاح القديم، والقناطر التاريخية.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Cascade_Sefrou.jpg"
    },
    "الناظور": {
        "agri": "تتميز بالثروة السمكية وبحيرة مارتشيكا وإنتاج زيت الزيتون.",
        "craft": "المنسوجات الريفية والصناعات المرتبطة بالقصب والدوم.",
        "monument": "كورنيش مارتشيكا وجبل غوروغو.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Nador_Maroc.jpg"
    }
}

food_stories = {
    "Pastilla": {
        "name": "Bstilla / بسطيلة",
        "story": "تحفة أندلسية-فاسية تمزج بين الدجاج واللوز والقرفة في تناغم فريد بين الحلو والمالح.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Moroccan_Pastilla.jpg"
    },
    "Tangia": {
        "name": "Tangia / طنجية",
        "story": "أكلة الحرفيين المراكشيين، تُطبخ ببطء ليلة كاملة في رماد الفرن التقليدي.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Tangia_Marrakchia.jpg"
    }
}

# --- 3. الترجمات الموحدة (للقائمة والتبويبات) ---
translations = {
    "English": {"title": "Maison Balkiss AI", "route_tab": "📍 Routes", "story_tab": "🍲 Storytelling", "heritage_tab": "🏛️ City Guide", "lang": "Language", "curr": "Currency", "loc": "Location", "scan": "Scan Dish"},
    "Français": {"title": "Maison Balkiss AI", "route_tab": "📍 Itinéraires", "story_tab": "🍲 Storytelling", "heritage_tab": "🏛️ Guide Ville", "lang": "Langue", "curr": "Devise", "loc": "Localisation", "scan": "Scanner"},
    "العربية": {"title": "ميزون بلقيس الذكي", "route_tab": "📍 المسارات", "story_tab": "🍲 حكايات الأطباق", "heritage_tab": "🏛️ دليل المدن", "lang": "اللغة", "curr": "العملة", "loc": "الموقع", "scan": "فحص الطبق"}
}

# --- 4. القائمة الجانبية (Sidebar) الشاملة ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 " + translations["English"]["lang"], ["English", "Français", "العربية"])
t = translations[lang]

curr_type = st.sidebar.selectbox("💱 " + t["curr"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")
st.sidebar.subheader(t["loc"])
method = st.sidebar.radio("", ["List", "Manual"])
user_city = st.sidebar.selectbox("Select City", all_cities_list) if method == "List" else st.sidebar.text_input("Type City", "صفرو")

# --- 5. العرض الرئيسي (Tabs) ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    st.info(f"📍 Location: {user_city}")
    region = st.selectbox("Select Region (12 Districts)", list(morocco_map.keys()))
    city_in_reg = st.selectbox("Cities in this region", morocco_map[region])
    if city_in_reg == "صفرو": st.success("✅ Smart Trail Found: The Cherry Route")

with tab2:
    st.subheader(t['scan'])
    up = st.file_uploader("Upload dish...", type=["jpg", "png"])
    if up:
        st.image(up, width=300)
        dish = st.selectbox("Identify:", list(food_stories.keys()))
        st.image(food_stories[dish]["img"], use_column_width=True)
        st.write(f"📖 **{food_stories[dish]['name']}**: {food_stories[dish]['story']}")

with tab3:
    st.header(f"🏛️ Exploring {user_city}")
    data = city_intel.get(user_city, {"agri": "Searching AI...", "craft": "Searching AI...", "monument": "Searching AI...", "img": "https://via.placeholder.com/800x400"})
    st.image(data["img"], use_column_width=True)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🌾 Agriculture")
        st.write(data["agri"])
    with c2:
        st.subheader("🧶 Crafts & Monuments")
        st.write(f"{data['craft']} \n\n {data['monument']}")

st.caption("Powered by Maison Balkiss AI - Tourism 4.0 | © 2026")
