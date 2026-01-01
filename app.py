import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="Maison Balkiss AI 4.0", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- الترجمات والعملات (كودك القديم) ---
translations = {
    "English": {"title": "Maison Balkiss AI", "location": "Current City", "heritage_tab": "🏛️ City Guide", "agri": "Agriculture", "crafts": "Crafts", "monuments": "Monuments"},
    "Français": {"title": "Maison Balkiss AI", "location": "Ville Actuelle", "heritage_tab": "🏛️ Guide Ville", "agri": "Agriculture", "crafts": "Artisanat", "monuments": "Monuments"},
    "العربية": {"title": "ميزون بلقيس الذكي", "location": "الموقع الحالي", "heritage_tab": "🏛️ دليل المدن", "agri": "الفلاحة والبيئة", "crafts": "الصناعة التقليدية", "monuments": "المآثر والسياحة"}
}
currencies = {"MAD": 1.0, "USD": 0.1, "EUR": 0.09}

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
curr_type = st.sidebar.selectbox("💱 Currency", ["MAD", "USD", "EUR"])
user_city = st.sidebar.text_input(translations[lang]["location"], "صفرو")

t = translations[lang]

# --- الحل الذكي: وظيفة توليد المعلومات أوتوماتيكياً ---
def get_city_info_ai(city_name):
    """
    هنا محاكاة لربط التطبيق بـ AI (مثل Gemini أو ChatGPT)
    لإعطاء معلومات دقيقة عن أي مدينة يكتبها المستخدم
    """
    # قاعدة بيانات محلية ذكية لضمان الدقة في المدن المغربية الكبرى
    smart_db = {
        "الناظور": {
            "agri": "تتميز بإنتاج الزيتون والسمك وبحيرة مارتشيكا.",
            "crafts": "الصناعة التقليدية الريفية، والمنسوجات.",
            "monuments": "مارتشيكا، جبل غوروغو، وكورنيش المدينة.",
            "img": "https://images.unsplash.com/photo-1598111951522-442867828751?q=80&w=800"
        },
        "صفرو": {
            "agri": "عاصمة حب الملوك (الكرز)، وتشتهر بالزيتون والتين.",
            "crafts": "صناعة 'العقد' (أزرار القفطان) المتميزة والنسيج.",
            "monuments": "الشلالات، المدينة القديمة، والملاح التاريخي.",
            "img": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Cascade_Sefrou.jpg"
        }
    }
    
    # إيلا مالقاش المدينة فـ smart_db، السيستيم كينتج معلومة عامة (البحث الذكي)
    if city_name in smart_db:
        return smart_db[city_name]
    else:
        return {
            "agri": f"تشتهر منطقة {city_name} بتنوعها الفلاحي الطبيعي الذي يميز جهتها في المغرب.",
            "crafts": f"تزخر {city_name} بمهارات حرفية تقليدية تتوارثها الأجيال.",
            "monuments": f"توجد بـ {city_name} مآثر تاريخية ومناطق سياحية تستحق الاستكشاف.",
            "img": "https://via.placeholder.com/800x400.png?text=Discover+Morocco"
        }

# --- العرض الرئيسي ---
st.title(f"⚜️ {t['title']}")

# التبويب الثالث: دليل المدن الذكي
tab_routes, tab_food, tab_city = st.tabs([t['title'], "🍲 Gastronomy", t['heritage_tab']])

with tab_city:
    st.header(f"🏛️ Exploring {user_city}")
    info = get_city_info_ai(user_city)
    
    st.image(info["img"], use_column_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🌾 {t['agri']}")
        st.info(info["agri"])
        st.subheader(f"🧶 {t['crafts']}")
        st.success(info["crafts"])
    with col2:
        st.subheader(f"🏛 {t['monuments']}")
        st.warning(info["monuments"])

st.markdown("---")
st.caption("Powered by Maison Balkiss AI - Smart Tourism 4.0 | © 2026")
