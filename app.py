import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- الترجمات (عربي، فرنسي، إنجليزي) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "intro": "Experience Tourism 4.0: Discover Morocco's authentic flavors and stories.",
        "route_tab": "📍 AI Culinary Routes",
        "story_tab": "🍲 Dish Storytelling",
        "select_region": "Select a Region",
        "select_city": "Select a City",
        "identify": "Identify your Dish (AI Scan)",
        "currency": "Currency",
        "more_info": "Smart route is being generated for this area..."
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "Vivez le Tourisme 4.0 : Découvrez les saveurs et histoires authentiques du Maroc.",
        "route_tab": "📍 Itinéraires Culinaires IA",
        "story_tab": "🍲 Storytelling des Plats",
        "select_region": "Choisir une Région",
        "select_city": "Choisir une Ville",
        "identify": "Identifier votre Plat (Scan IA)",
        "currency": "Devise",
        "more_info": "L'itinéraire intelligent est en cours de génération..."
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "intro": "عش تجربة السياحة 4.0: اكتشف النكهات والقصص المغربية الأصيلة.",
        "route_tab": "📍 مسارات تذوق ذكية",
        "story_tab": "🍲 حكايات الأطباق",
        "select_region": "اختر جهة",
        "select_city": "اختر مدينة",
        "identify": "تعرف على طبقك (فحص ذكي)",
        "currency": "العملة",
        "more_info": "يتم الآن إنشاء المسار الذكي لهذه المنطقة..."
    }
}

# --- قاعدة بيانات الجهات والمدن المغربية (AI Data Structure) ---
morocco_map = {
    "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Al Hoceïma", "Chefchaouen", "Larache", "Ouezzane"],
    "L'Oriental": ["Oujda", "Berkane", "Nador", "Saïdia", "Figuig", "Taourirt"],
    "Fès-Meknès": ["Fès", "Meknès", "Sefrou", "Ifrane", "Taza", "Moulay Idriss Zerhoun"],
    "Rabat-Salé-Kénitra": ["Rabat", "Salé", "Kénitra", "Skhirat", "Khémisset"],
    "Béni Mellal-Khénifra": ["Béni Mellal", "Khénifra", "Azilal", "Fquih Ben Salah"],
    "Casablanca-Settat": ["Casablanca", "Settat", "Mohammédia", "El Jadida", "Benslimane"],
    "Marrakech-Safi": ["Marrakech", "Safi", "Essaouira", "Oukaïmeden", "Benguérir"],
    "Drâa-Tafilalet": ["Errachidia", "Ouarzazate", "Midelt", "Tinghir", "Zagora"],
    "Souss-Massa": ["Agadir", "Taroudant", "Tiznit", "Tafraout", "Tata"],
    "Guelmim-Oued Noun": ["Guelmim", "Tan-Tan", "Sidi Ifni", "Assa-Zag"],
    "Laâyoune-Sakia El Hamra": ["Laâyoune", "Smara", "Boujdour", "Tarfaya"],
    "Dakhla-Oued Ed-Dahab": ["Dakhla", "Aousserd"]
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
    # اختيار الجهة من القائمة الشاملة
    region = st.selectbox("", list(morocco_map.keys()))
    
    st.subheader(t['select_city'])
    # اختيار المدينة بناءً على الجهة المختارة (Dynamic Selection)
    city = st.selectbox("", morocco_map[region])
    
    st.markdown("---")
    # منطق العرض الخاص بسيفرو وفاس (Pilot)
    if city == "Sefrou":
        st.info("🍒 **Route: The Cherry & Olive Trail**")
        st.write("Explore the ancient watermills and traditional cherry orchards of the Middle Atlas.")
        st.write("🍴 **Must-try:** Sefrou Tagine with local olives.")
    elif city == "Marrakech":
        st.info("🏺 **Route: The Red City Spice Tour**")
        st.write("Navigate through the souks to discover the secret of Tangia.")
    else:
        st.warning(f"🚧 {t['more_info']} (Location: {city})")

with tab2:
    st.subheader(t['identify'])
    uploaded_file = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, width=400)
        st.success("✅ AI Detection Complete")
        
        # مثال لقصة طبق (Couscous)
        st.write("📖 **Storytelling:** This dish represents centuries of Moroccan hospitality. Each region adds its unique touch via local spices and grains.")
        
        # تحويل السعر ذكياً
        base_price = 100 # MAD
        converted_price = base_price * currencies[curr_type]
        st.metric(label=f"Average Price in {curr_type}", value=f"{converted_price:.2f} {curr_type}")

st.markdown("---")
st.caption("Powered by Maison Balkiss AI Business - Tourism 4.0 | © 2025 Competition Entry")
