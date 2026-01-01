import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل المغربي
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود تحويل الموقع لتطبيق (PWA) للتثبيت على الهاتف ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- قاعدة بيانات الجهات والمدن المغربية الشاملة (12 جهة) ---
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

# تجميع كل المدن في قائمة واحدة للبحث الذكي
all_cities_list = sorted([city for cities in morocco_map.values() for city in cities])

# --- قاعدة بيانات المعارف المغربية (فلاحة، صناعة، مآثر، وصور) ---
city_knowledge_base = {
    "صفرو": {
        "agri": "تُعرف بـ 'حديقة المغرب'، وهي العاصمة العالمية لـ 'حب الملوك' (الكرز)، وتشتهر بجودة الزيتون والتين المحلي.",
        "crafts": "تنفرد بصناعة 'العقد' التقليدية (أزرار القفطان)، وتشتهر بالنسيج والنجارة الفنية.",
        "monuments": "شلالات صفرو الخلابة، المدينة القديمة، ملاح صفرو التاريخي، وقنطرة لالة أمينة.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Cascade_Sefrou.jpg/800px-Cascade_Sefrou.jpg"
    },
    "فاس": {
        "agri": "تعتمد ضواحيها (سهل سايس) على إنتاج زيت الزيتون، الحبوب، والفواكه الموسمية.",
        "crafts": "عاصمة الصناعة التقليدية: دباغة الجلود، الزليج الفاسي، النحاسيات، والنسيج المطرز.",
        "monuments": "جامعة القرويين، مدرسة العطارين، دار الدباغ (شوارة)، وباب بوجلود الشهير.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Fes_Morocco_Gate.jpg/800px-Fes_Morocco_Gate.jpg"
    }
}

# --- قاعدة بيانات الحكايات الطويلة للأطباق ---
food_stories = {
    "Pastilla": {
        "name": "Bstilla / بسطيلة",
        "story": "البسطيلة الفاسية هي ذروة فن الطبخ المغربي؛ تحفة أندلسية استقرت في فاس وتطورت عبر القرون. تتميز بتناغم مذهل بين الملوحة والحلاوة، حيث تُحشى رقائق العجين الرقيقة جداً (الورقة) بالدجاج المحمر أو الحمام، واللوز المقلي والمهرمش مع القرفة وماء الزهر، وتُزين بالسكر الصقيل والقرفة.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Moroccan_Pastilla.jpg/800px-Moroccan_Pastilla.jpg"
    },
    "Tangia": {
        "name": "Tangia / طنجية",
        "story": "الطنجية المراكشية هي أكلة الرجال بامتياز. ترتبط تاريخياً بأسواق مراكش وحرفييها؛ حيث يوضع اللحم مع الثوم والكامون والزعفران الحر والسمن في 'قلوشة' فخارية، وتُدفن في رماد 'الفرناشي' ليلة كاملة لتنضج ببطء شديد وتكتسب نكهة لا تُقاوم.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Tangia_Marrakchia.jpg/800px-Tangia_Marrakchia.jpg"
    }
}

# --- الترجمات والعملات ---
translations = {
    "English": {"title": "Maison Balkiss AI", "route_tab": "📍 Routes", "story_tab": "🍲 AI Storytelling", "heritage_tab": "🏛️ City Guide", "location": "Current Location", "select_city": "Select or Type City"},
    "Français": {"title": "Maison Balkiss AI", "route_tab": "📍 Itinéraires", "story_tab": "🍲 Storytelling", "heritage_tab": "🏛️ Guide Ville", "location": "Ville Actuelle", "select_city": "Choisir/Saisir Ville"},
    "العربية": {"title": "ميزون بلقيس الذكي", "route_tab": "📍 المسارات", "story_tab": "🍲 حكايات الأطباق", "heritage_tab": "🏛️ دليل المدن", "location": "الموقع الحالي", "select_city": "اختر أو اكتب المدينة"}
}
currencies = {"MAD": 1.0, "USD": 0.1, "EUR": 0.09}

# --- القائمة الجانبية (Sidebar) الشاملة ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
curr_type = st.sidebar.selectbox("💱 Currency", ["MAD", "USD", "EUR"])

t = translations[lang]

st.sidebar.markdown("---")
st.sidebar.subheader(t["location"])
# خاصية تحديد الموقع: اختيار من القائمة أو كتابة يدوية
search_method = st.sidebar.radio("", ["Select from List", "Type City Name"])
if search_method == "Select from List":
    user_city = st.sidebar.selectbox(t["select_city"], all_cities_list, index=all_cities_list.index("صفرو"))
else:
    user_city = st.sidebar.text_input(t["select_city"], "صفرو")

# --- العنوان الرئيسي ---
st.title(f"⚜️ {t['title']}")

tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    st.info(f"📍 {t['location']}: **{user_city}**")
    region_of_city = next((r for r, cities in morocco_map.items() if user_city in cities), "Unknown Region")
    st.subheader(f"Region: {region_of_city}")
    # (هنا يظهر منطق المسارات الذكية)
    if user_city == "صفرو":
        st.success("✅ Smart Trail Found: **The Cherry & Olive Heritage Route**")

with tab2:
    st.subheader("🍲 AI Gastronomy Storytelling")
    dish = st.selectbox("Select Dish:", list(food_stories.keys()))
    data = food_stories[dish]
    st.image(data["img"], use_column_width=True)
    st.markdown(f"### {data['name']}")
    st.write(f"📖 {data['story']}")

with tab3:
    st.header(f"🏛️ Discover {user_city}")
    # البحث الذكي في قاعدة البيانات
    info = city_knowledge_base.get(user_city, {
        "agri": "المعلومات الفلاحية قيد التحديث عبر Google لهذه المنطقة...",
        "crafts": "الصناعة التقليدية مشهورة تاريخياً في هذا الإقليم، جاري تحميل التفاصيل...",
        "monuments": "نحن نبحث في السجلات الأثرية عن معالم هذه المدينة...",
        "img": "https://via.placeholder.com/800x400.png?text=Discover+Morocco"
    })
    
    st.image(info["img"], use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌾 Agriculture & Nature")
        st.write(info["agri"])
        st.subheader("🧶 Local Crafts")
        st.write(info["crafts"])
    with col2:
        st.subheader("🏛️ Monuments & Places")
        st.write(info["monuments"])

st.markdown("---")
st.caption("Powered by Maison Balkiss AI - Tourism 4.0 | © 2026 Competition Entry")
