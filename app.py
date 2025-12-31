import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل المغربي
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism", layout="wide")

# --- الترجمات (عربي، فرنسي، إنجليزي) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "intro": "Experience Tourism 4.0: Discover Morocco's authentic flavors and stories.",
        "route_tab": "📍 AI Culinary Routes",
        "story_tab": "🍲 Dish Storytelling",
        "select_region": "Select a Region",
        "identify": "Identify your Dish",
        "currency": "Currency"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "Vivez le Tourisme 4.0 : Découvrez les saveurs et histoires authentiques du Maroc.",
        "route_tab": "📍 Itinéraires Culinaires IA",
        "story_tab": "🍲 Storytelling des Plats",
        "select_region": "Choisir une Région",
        "identify": "Identifier votre Plat",
        "currency": "Devise"
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "intro": "عش تجربة السياحة 4.0: اكتشف النكهات والقصص المغربية الأصيلة.",
        "route_tab": "📍 مسارات تذوق ذكية",
        "story_tab": "🍲 حكايات الأطباق",
        "select_region": "اختر جهة",
        "identify": "تعرف على طبقك",
        "currency": "العملة"
    }
}

# --- العملات ---
currencies = {"MAD": 1.0, "USD": 0.1, "EUR": 0.09}

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
curr_type = st.sidebar.selectbox("💱 Currency", ["MAD", "USD", "EUR"])

t = translations[lang]

# --- العنوان الرئيسي ---
st.title(f"⚜️ {t['title']}")
st.markdown(f"**{t['intro']}**")

# --- التبويبات الرئيسية ---
tab1, tab2 = st.tabs([t['route_tab'], t['story_tab']])

with tab1:
    st.subheader(t['select_region'])
    region = st.selectbox("", ["Fès-Meknès", "Marrakech-Safi", "Souss-Massa", "Tanger-Tétouan", "Sahara Regions"])
    
    # مثال حي لجهة فاس-مكناس (سيفرو)
    if region == "Fès-Meknès":
        st.info("📍 **Route: The Cherry & Olive Trail (Sefrou)**")
        st.write("Explore the ancient watermills and traditional cherry orchards.")
        st.write("🍴 **Must-try:** Sefrou Tagine with local olives.")

with tab2:
    st.subheader(t['identify'])
    uploaded_file = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, width=400)
        st.success("✅ AI Detection: **Traditional Moroccan Couscous**")
        
        # قصة الطبق (Storytelling)
        st.write("📖 **The Story:** Couscous is a symbol of generosity in Morocco. Traditionally served on Fridays, it represents family unity.")
        
        # تحويل السعر ذكياً
        base_price = 100 # MAD
        converted_price = base_price * currencies[curr_type]
        st.metric(label=f"Average Price in {curr_type}", value=f"{converted_price:.2f} {curr_type}")

st.markdown("---")
st.caption("Powered by Maison Balkiss AI Business - Tourism 4.0")
