import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل المغربي
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود تحويل الموقع لتطبيق (PWA) ليتثبت على الهاتف ---
st.markdown(
    """
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js');
      }
    </script>
    """,
    unsafe_allow_html=True,
)

# --- قاعدة بيانات الأطباق الذكية (القصص والأصول) ---
food_db = {
    "Pastilla": {
        "name_ar": "بسطيلة",
        "origin": "Fès / فاس",
        "story_en": "A masterpiece of Andalusian-Moroccan fusion, traditionally served at weddings. It balances sweet and savory flavors.",
        "story_fr": "Un chef-d'œuvre de la fusion andalou-marocaine, traditionnellement servie lors des mariages.",
        "story_ar": "تحفة فنية من الاندماج الأندلسي المغربي، تُقدم تقليدياً في الأعراس وتوازن بين المذاق الحلو والمالح."
    },
    "Tangia": {
        "name_ar": "طنجية",
        "origin": "Marrakech / مراكش",
        "story_en": "The famous slow-cooked clay pot dish, traditionally prepared by men in the communal oven (Fernatchi).",
        "story_fr": "Le célèbre plat cuit lentement dans un pot en terre, traditionnellement préparé par les hommes.",
        "story_ar": "طبق القدر الفخاري الشهير المطبوخ ببطء، كان يُحضره الرجال تقليدياً ويُطهى في الفرن الجماعي (الفرناشي)."
    },
    "Couscous": {
        "name_ar": "كسكس",
        "origin": "All Morocco / كل المغرب",
        "story_en": "The symbol of Friday and family gathering. Each region has its own version.",
        "story_fr": "Le symbole du vendredi et du rassemblement familial. Chaque région a sa propre version.",
        "story_ar": "رمز يوم الجمعة واللمة العائلية. كل منطقة في المغرب لها لمستها الخاصة في تحضيره."
    }
}

# --- قاعدة بيانات المطاعم الافتراضية (للبحث حسب الموقع) ---
restaurants_data = [
    {"name": "Authentic Flavors Tanger", "city": "Tanger", "dish": "Tangia", "price": 120},
    {"name": "Palais de Fès", "city": "Fès", "dish": "Pastilla", "price": 180},
    {"name": "Sefrou Traditional Garden", "city": "Sefrou", "dish": "Tagine", "price": 95},
    {"name": "Marrakech Delight (Tanger Branch)", "city": "Tanger", "dish": "Tangia", "price": 130}
]

# --- الترجمات ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "intro": "Experience Tourism 4.0: Discover Morocco's authentic flavors.",
        "route_tab": "📍 AI Culinary Routes",
        "story_tab": "🍲 AI Storytelling",
        "select_region": "Select a Region",
        "select_city": "Select a City",
        "identify": "Scan your Dish",
        "currency": "Currency",
        "find_near": "Find it near you in",
        "no_res": "No restaurants serving this dish in this city yet."
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "Vivez le Tourisme 4.0 : Découvrez les saveurs authentiques.",
        "route_tab": "📍 Itinéraires Culinaires",
        "story_tab": "🍲 Storytelling IA",
        "select_region": "Choisir une Région",
        "select_city": "Choisir une Ville",
        "identify": "Scanner votre Plat",
        "currency": "Devise",
        "find_near": "Trouvez-le près de vous à",
        "no_res": "Aucun restaurant ne sert ce plat dans cette ville pour le moment."
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "intro": "عش تجربة السياحة 4.0: اكتشف النكهات المغربية الأصيلة وقصصها.",
        "route_tab": "📍 مسارات ذكية",
        "story_tab": "🍲 حكايات الذكاء الاصطناعي",
        "select_region": "اختر جهة",
        "select_city": "اختر مدينة",
        "identify": "فحص الطبق",
        "currency": "العملة",
        "find_near": "أين تجد هذا الطبق في مدينة",
        "no_res": "لا توجد مطاعم تقدم هذا الطبق في هذه المدينة حالياً."
    }
}

# --- العملات ---
currencies = {"MAD": 1.0, "USD": 0.1, "EUR": 0.09}

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
curr_type = st.sidebar.selectbox("💱 Currency", ["MAD", "USD", "EUR"])
user_location = st.sidebar.selectbox("📍 Current Location (City)", ["Tanger", "Fès", "Marrakech", "Casablanca", "Sefrou"])

t = translations[lang]

# --- العنوان الرئيسي ---
st.title(f"⚜️ {t['title']}")
st.markdown(f"**{t['intro']}**")

tab1, tab2 = st.tabs([t['route_tab'], t['story_tab']])

with tab1:
    # قاعدة بيانات الجهات الـ 12
    morocco_map = {
        "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Chefchaouen"],
        "Fès-Meknès": ["Sefrou", "Fès", "Meknès", "Ifrane"],
        "Marrakech-Safi": ["Marrakech", "Safi", "Essaouira"],
        # ... باقي الجهات تضاف هنا
    }
    region = st.selectbox(t['select_region'], list(morocco_map.keys()) if region in morocco_map else ["Fès-Meknès"])
    city = st.selectbox(t['select_city'], morocco_map.get(region, ["Fès"]))
    
    if city == "Sefrou":
        st.info("🍒 **Route: The Cherry & Olive Trail**")
        st.write("Specialty: Tajine with Sefrou Olives.")
    else:
        st.warning("🚧 Smart route generation...")

with tab2:
    st.subheader(t['identify'])
    uploaded_file = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, width=400)
        
        # اختيار الطبق (محاكاة للتعرف الذكي)
        dish_selected = st.selectbox("AI Identification Results:", list(food_db.keys()))
        info = food_db[dish_selected]
        
        st.success(f"✅ {info['name_ar']} / {dish_selected}")
        st.info(f"📍 **Origin:** {info['origin']}")
        
        # عرض القصة حسب اللغة المختارة
        if lang == "English": st.write(f"📖 **Story:** {info['story_en']}")
        elif lang == "Français": st.write(f"📖 **Histoire:** {info['story_fr']}")
        else: st.write(f"📖 **القصة:** {info['story_ar']}")
        
        st.markdown("---")
        st.subheader(f"🍴 {t['find_near']} {user_location}:")
        
        # البحث في المطاعم حسب الطبق والمدينة الحالية للسائح
        nearby = [r for r in restaurants_data if r['dish'] == dish_selected and r['city'] == user_location]
        
        if nearby:
            for res in nearby:
                col1, col2 = st.columns([2,1])
                with col1:
                    st.write(f"🏠 **{res['name']}**")
                with col2:
                    price = res['price'] * currencies[curr_type]
                    st.write(f"💰 {round(price, 2)} {curr_type}")
                st.button(f"Go to {res['name']} 🚩", key=res['name'])
        else:
            st.warning(t['no_res'])

st.markdown("---")
st.caption("Maison Balkiss AI Business - Tourism 4.0")
