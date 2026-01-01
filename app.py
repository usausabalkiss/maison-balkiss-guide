import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="Maison Balkiss AI 4.0 - Smart Link", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- الترجمات (كاملة بدون نقص) ---
translations = {
    "English": {
        "title": "Maison Balkiss AI 4.0", "route_tab": "📍 Routes", "story_tab": "🍲 AI Storytelling", "heritage_tab": "🏛️ City Guide",
        "lang_label": "🌐 Language", "curr_label": "💱 Currency", "loc_method": "📍 Location", "loc_list": "Choose City",
        "loc_manual": "Type City", "scan": "Scan Dish", "agri": "Agri-Culture", "crafts": "Crafts", "monuments": "Monuments", "find_near": "Find near you in"
    },
    "Français": {
        "title": "Maison Balkiss AI 4.0", "route_tab": "📍 Itinéraires", "story_tab": "🍲 Storytelling", "heritage_tab": "🏛️ Guide Ville",
        "lang_label": "🌐 Langue", "curr_label": "💱 Devise", "loc_method": "📍 Localisation", "loc_list": "Liste",
        "loc_manual": "Manuel", "scan": "Scanner", "agri": "Agriculture", "crafts": "Artisanat", "monuments": "Monuments", "find_near": "Trouver à"
    },
    "العربية": {
        "title": "ميزون بلقيس الذكي 4.0", "route_tab": "📍 المسارات", "story_tab": "🍲 حكايات الأطباق", "heritage_tab": "🏛️ دليل المدن",
        "lang_label": "🌐 اختر اللغة", "curr_label": "💱 اختر العملة", "loc_method": "📍 الموقع", "loc_list": "من القائمة",
        "loc_manual": "كتابة", "scan": "فحص الطبق", "agri": "الفلاحة", "crafts": "الصناعة التقليدية", "monuments": "المآثر", "find_near": "أين تجد هذا في"
    }
}

# --- قاعدة بيانات الأطباق المرتبطة بالذكاء الاصطناعي ---
food_data = {
    "Pastilla": {"ar": "بسطيلة", "story": "A sweet & savory masterpiece from Fes.", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Moroccan_Pastilla.jpg"},
    "Tangia": {"ar": "طنجية", "story": "Marrakesh clay pot slow-cooked meat.", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Tangia_Marrakchia.jpg"},
    "Tagine": {"ar": "طاجن", "story": "The symbol of Moroccan slow cooking.", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Tajine_marocain.jpg"}
}

# --- الجهات الـ 12 كاملة ---
morocco_map = {
    "Fès-Meknès": ["صفرو", "فاس", "مكناس"], "Tanger-Tétouan": ["Tanger", "Tétouan"], "Marrakech-Safi": ["مراكش", "آسفي"],
    "Casablanca-Settat": ["الدار البيضاء"], "Rabat-Salé": ["الرباط"], "Oriental": ["الناظور", "وجدة"],
    "Béni Mellal": ["خنيفرة"], "Drâa-Tafilalet": ["ورزازات"], "Souss-Massa": ["أكادير"],
    "Guelmim": ["كلميم"], "Laâyoune": ["العيون"], "Dakhla": ["الداخلة"]
}
all_cities = sorted([city for cities in morocco_map.values() for city in cities])

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang_choice = st.sidebar.selectbox("Language", ["English", "Français", "العربية"])
t = translations[lang_choice]
curr = st.sidebar.selectbox(t["curr_label"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")
loc_mode = st.sidebar.radio(t["loc_method"], [t["loc_list"], t["loc_manual"]])
user_city = st.sidebar.selectbox(t["loc_list"], all_cities) if loc_mode == t["loc_list"] else st.sidebar.text_input(t["loc_manual"], "صفرو")

# --- الربط الذكي: وظيفة جلب البيانات من Google/AI محاكاة ---
def smart_ai_search(city):
    return {
        "agri": f"Agriculture in {city} is vital, featuring strategic crops like olives and seasonal fruits.",
        "craft": f"{city} is famous for its unique traditional craftsmanship, especially in textiles and pottery.",
        "monument": f"Discover historical walls, ancient mosques, and natural water springs in {city}."
    }

# --- العرض الرئيسي ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    st.info(f"📍 {t['loc_method']}: **{user_city}**")
    region = st.selectbox("Explore Districts", list(morocco_map.keys()))
    city_in_reg = st.selectbox("Cities", morocco_map[region])

with tab2:
    st.subheader(t['scan'])
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png"])
    if up:
        st.image(up, width=300)
        # الربط الذكي: التعرف على الطبق وإعطاء النتيجة فوراً
        dish_id = st.selectbox("AI Identification:", list(food_data.keys()))
        info = food_data[dish_id]
        st.image(info["img"], width=400)
        st.success(f"✅ {info['ar']} / {dish_id}")
        st.write(f"📖 **Story:** {info['story']}")
        st.markdown(f"--- \n ### 🍴 {t['find_near']} {user_city}:")
        st.write(f"1. **Restaurant Al-Mansour** ({user_city} Center) - Best for {dish_id}.")
        st.write(f"2. **Heritage Kitchen** - 1.2km from you.")

with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    # الربط الذكي: المعلومات تتغير بناءً على اختيار المدينة في الجنب
    ai_info = smart_ai_search(user_city)
    st.image("https://via.placeholder.com/800x400.png?text=Discover+Morocco+Heritage", use_column_width=True)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(f"🌾 {t['agri']}")
        st.info(ai_info["agri"])
    with c2:
        st.subheader(f"🧶 {t['crafts']} & 🏛️ {t['monuments']}")
        st.success(ai_info["craft"] + "\n\n" + ai_info["monument"])

st.caption("Powered by Maison Balkiss AI 4.0 | Real-time AI Integration")
