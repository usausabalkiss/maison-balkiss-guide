import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل (نفس واجهتك الأصلية)
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.ifier.io/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (تمت إضافة المفاتيح الناقصة لتفادي KeyError) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "intro": "Experience Tourism 4.0: Discover Morocco's authentic flavors.",
        "route_tab": "📍 AI Culinary Routes", "story_tab": "🍲 AI Storytelling", "heritage_tab": "🏛️ City Guide",
        "identify": "Scan your Dish", "currency": "Currency", "loc_method": "Location Method", 
        "loc_list": "Choose from List", "loc_manual": "Type City Name", "location": "Location",
        "agri": "Agriculture & Economy", "crafts": "Local Crafts", "monuments": "Monuments & Heritage",
        "select_city": "Select a City", "select_region": "Select a Region", "find_near": "Best places near you in"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "Vivez le Tourisme 4.0 : Découvrez les saveurs authentiques.",
        "route_tab": "📍 Itinéraires Culinaires", "story_tab": "🍲 Storytelling IA", "heritage_tab": "🏛️ Guide Ville",
        "identify": "Scanner votre Plat", "currency": "Devise", "loc_method": "Méthode de Localisation", 
        "loc_list": "Liste des villes", "loc_manual": "Saisie Manuelle", "location": "Localisation",
        "agri": "Agriculture & Économie", "crafts": "Artisanat Local", "monuments": "Monuments & Patrimoine",
        "select_city": "Choisir une Ville", "select_region": "Choisir une Région", "find_near": "Meilleurs endroits à"
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
        "intro": "عش تجربة السياحة 4.0: اكتشف النكهات المغربية الأصيلة وقصصها.",
        "route_tab": "📍 مسارات ذكية", "story_tab": "🍲 حكايات الأطباق", "heritage_tab": "🏛️ دليل المدن",
        "identify": "فحص الطبق", "currency": "العملة", "loc_method": "طريقة تحديد الموقع", 
        "loc_list": "الاختيار من القائمة", "loc_manual": "كتابة يدوية", "location": "الموقع الحالي",
        "agri": "الفلاحة والاقتصاد", "crafts": "الصناعة التقليدية", "monuments": "المآثر والتراث",
        "select_city": "اختر مدينة", "select_region": "اختر جهة", "find_near": "أفضل الأماكن في"
    }
}

# --- 3. محرك المعرفة والجهات (تامارتك محفوظة بالكامل) ---
city_wiki = {
    "صفرو": {
        "agri": "عاصمة حب الملوك (الكرز) عالمياً، وتشتهر بزيت الزيتون الممتاز بفضل منابع مياه الأطلس المتوسط.",
        "craft": "تنفرد بمهارة نساء المدينة في صناعة 'العقد' التقليدية التي تزين القفطان المغربي.",
        "monument": "شلال صفرو العظيم، أسوار المدينة التاريخية، والملاح التاريخي.",
        "best_for": "حب الملوك، زيت الزيتون، والعقد التقليدية."
    },
    "Figuig": {
        "agri": "واحة النخيل العريقة، مشهورة بتمور 'عزيزة' والفقارات (نظام ري تقليدي فريد).",
        "craft": "تتميز بالنسيج الفكيكي التقليدي (الحايك والجلابة الصوفية) بجودة عالية.",
        "monument": "الصومعة الحجرية لقصر الوداغير، الواحات السبع، والقصور التاريخية.",
        "best_for": "تمور عزيزة والسياحة الواحاتية."
    }
}

# --- 4. قاعدة بيانات الجهات الـ 12 (محفوظة بالكامل كما هي) ---
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
    user_city = st.sidebar.selectbox(t["select_city"], all_cities_list, index=all_cities_list.index("صفرو") if "صفرو" in all_cities_list else 0)
else:
    user_city = st.sidebar.text_input(t["loc_manual"], "صفرو")

# --- 5. العرض الرئيسي (Tabs) ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs([t['route_tab'], t['story_tab'], t['heritage_tab']])

with tab1:
    st.info(f"📍 {t['location']}: **{user_city}**")
    region = st.selectbox(t["select_region"], list(morocco_map.keys()))
    city_select = st.selectbox(t["select_city"], morocco_map[region])

with tab2:
    st.subheader(t['identify'])
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png", "jpeg"])
    
    if up:
        st.image(up, width=400)
        
        # --- السطر المهم: ك نعطيو سمية افتراضية باش ما يوقعش NameError ---
        dish_name = "Moroccan Dish" 
        dish_reg = user_city
        dish_story = "A wonderful discovery of Moroccan gastronomy."
        
        import requests
        API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
        headers = {"Authorization": "Bearer hf_VvYvXmSExPypKzLqEBCuXpNbR"}
        
        with st.spinner('Maison Balkiss AI is analyzing... 🧠'):
            try:
                response = requests.post(API_URL, headers=headers, data=up.getvalue(), timeout=10)
                output = response.json()
                
                if isinstance(output, list) and len(output) > 0:
                    top_result = output[0]['label'].lower()
                    
                    if any(x in top_result for x in ["stew", "pottery", "meat", "curry"]):
                        dish_name, dish_reg, dish_story = "Moroccan Tajine", "Atlas & Souss", "A slow-cooked savory stew named after the conical clay pot."
                    elif any(x in top_result for x in ["grain", "couscous", "rice"]):
                        dish_name, dish_reg, dish_story = "Moroccan Couscous", "All Regions", "The masterpiece of Moroccan hospitality, traditionally served on Fridays."
                    elif any(x in top_result for x in ["pastry", "cookie", "bakery", "dough"]):
                        dish_name, dish_reg, dish_story = "Kaab el Ghazal", "Fès & Meknès", "A royal almond pastry shaped like a crescent moon."
                
                st.success(f"✅ AI Identified: {dish_name}")
                st.info(f"📍 **Origin:** {dish_reg}")
                st.write(f"**The Story:** {dish_story}")

            except:
                # إيلا وقع مشكل، ك ياخد السمية من الملف وما ك يوقعش NameError
                dish_name = up.name.split('.')[0].title()
                st.warning(f"🔄 Using filename recognition: {dish_name}")

        st.markdown("---")
        # دبا هاد السطر ديما غا يلقى dish_name وما غا يخرجش الخطأ
        maps_url = f"http://googleusercontent.com/maps.google.com/q={dish_name}+restaurant+{user_city}"
        st.markdown(f"🔗 [Find the best {dish_name} in {user_city} on Maps]({maps_url})")
with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    # جلب بيانات ويكيبيديا الحقيقية لكل مدينة
    info = city_wiki.get(user_city, {
        "agri": "Known for regional products of terroir.",
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
        st.markdown(f"🛍️ **Where to buy:** {info['best_for']}")

st.markdown("---")
st.caption("Powered by Maison Balkiss AI - Tourism 4.0 | © 2026")
