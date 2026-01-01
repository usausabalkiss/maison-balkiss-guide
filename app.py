import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Master Code", layout="wide")

# --- كود PWA للتثبيت على الهاتف (محفوظ) ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.jsdelivr.net/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (لغات ثلاث) ---
translations = {
    "English": {
        "title": "Maison Balkiss: AI Heritage & Gastronomy",
        "intro": "Experience Tourism 4.0: Discover Morocco's authentic flavors.",
        "route_tab": "📍 AI Culinary Routes",
        "story_tab": "🍲 AI Storytelling",
        "heritage_tab": "🏛️ City Guide",
        "select_region": "Select a Region",
        "select_city": "Select a City",
        "identify": "Scan your Dish",
        "currency": "Currency",
        "loc_method": "Location Method",
        "loc_list": "Choose from List",
        "loc_manual": "Type City Name",
        "find_near": "Best places near you in"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "Vivez le Tourisme 4.0 : Découvrez les saveurs authentiques.",
        "route_tab": "📍 Itinéraires Culinaires",
        "story_tab": "🍲 Storytelling IA",
        "heritage_tab": "🏛️ Guide Ville",
        "select_region": "Choisir une Région",
        "select_city": "Choisir une Ville",
        "identify": "Scanner votre Plat",
        "currency": "Devise",
        "loc_method": "Méthode de Localisation",
        "loc_list": "Liste des villes",
        "loc_manual": "Saisie Manuelle",
        "find_near": "Meilleurs endroits à"
    },
    "العربية": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
        "intro": "عش تجربة السياحة 4.0: اكتشف النكهات المغربية الأصيلة وقصصها.",
        "route_tab": "📍 مسارات ذكية",
        "story_tab": "🍲 حكايات الأطباق",
        "heritage_tab": "🏛️ دليل المدن",
        "select_region": "اختر جهة",
        "select_city": "اختر مدينة",
        "identify": "فحص الطبق",
        "currency": "العملة",
        "loc_method": "طريقة تحديد الموقع",
        "loc_list": "الاختيار من القائمة",
        "loc_manual": "كتابة يدوية",
        "find_near": "أفضل الأماكن في"
    }
}

# --- 3. قاعدة بيانات الجهات الـ 12 (كاملة ومحفوظة) ---
morocco_map = {
    "Tanger-Tétouan-Al Hoceïma": ["Tanger", "Tétouan", "Chefchaouen", "Al Hoceïma", "Larache", "Ouezzane"],
    "L'Oriental": ["Oujda", "Berkane", "Nador", "Saïdia", "Figuig"],
    "Fès-Meknès": ["صفرو", "فاس", "مكناس", "إفران", "تازة", "زرهون"],
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

# --- 4. القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
t = translations[lang]

curr_type = st.sidebar.selectbox(t["currency"], ["MAD", "USD", "EUR"])
st.sidebar.markdown("---")

# خاصية تحديد الموقع
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
    st.info(f"📍 {t['loc_method']}: **{user_city}**")
    region = st.selectbox(t['select_region'], list(morocco_map.keys()))
    city = st.selectbox(t['select_city'], morocco_map[region])
    if city == "صفرو":
        st.success("✅ Smart Trail Found: The Cherry & Olive Heritage Route")

with tab2:
    st.subheader(t['identify'])
    up = st.file_uploader("Upload dish photo...", type=["jpg", "png"])
    
    if up:
        st.image(up, width=350)
        
        # محرك البحث الذكي (يدوي حالياً لضمان الدقة)
        # تقدري تكتبي هنا أي طبق بغيتي وتزيدي القصص ديالو
        dish_database = {
            "Pastilla": {
                "name": "Bstilla / بسطيلة",
                "story": "تعتبر البسطيلة الفاسية ملكة المائدة المغربية؛ تحفة أندلسية استقرت في فاس وتطورت عبر القرون.",
                "ingredients": "ورقة البسطيلة، دجاج أو حمام، لوز مقلي ومهرمش، بيض، قرفة، سكر صقيل، وماء الزهر.",
                "cities": "فاس (الأصل)، الرباط، تطوان.",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Moroccan_Pastilla.jpg/800px-Moroccan_Pastilla.jpg"
            },
            "Tangia": {
                "name": "Tangia / طنجية",
                "story": "أكلة الحرفيين المراكشيين بامتياز، تُطهى ببطء في رماد الفرن التقليدي 'الفرناشي' ليلة كاملة.",
                "ingredients": "لحم البقر أو الغنم، سمن حار، مصير، ثوم، زعفران حر، كمون، وزيت زيتون.",
                "cities": "مراكش (الأصل).",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Tangia_Marrakchia.jpg/800px-Tangia_Marrakchia.jpg"
            }
        }
        
        # اختيار الطبق (محاكاة للتعرف الذكي)
        selected_dish = st.selectbox("AI Identification Results:", list(dish_database.keys()))
        dish_info = dish_database[selected_dish]
        
        # عرض المعلومات المرتبطة ذكياً
        st.image(dish_info["img"], use_column_width=True)
        st.success(f"✅ {dish_info['name']}")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"📖 **Story / الحكاية:** \n {dish_info['story']}")
            st.markdown(f"📍 **Famous Cities:** {dish_info['cities']}")
        with col_b:
            st.markdown(f"🍳 **Ingredients / المكونات:** \n {dish_info['ingredients']}")

        st.markdown("---")
        # الربط مع المدينة اللي حدد السائح في القائمة الجانبية
        st.subheader(f"🍴 {t['find_near']} {user_city}:")
        st.write(f"Based on AI, here are the top places for {dish_info['name']} in {user_city}:")
        st.info(f"📍 **Restaurant Al-Fassia** - 10 min from your location in {user_city}")
        st.info(f"📍 **Traditional Kitchen** - Highly recommended for authentic {selected_dish}")
with tab3:
    st.header(f"🏛️ {t['heritage_tab']}: {user_city}")
    
    # قاعدة بيانات ذكية وشاملة (تقدري تعمريها يدوياً لكل مدينة)
    city_wiki = {
        "صفرو": {
            "intro": "تُلقب بـ 'حديقة المغرب'، وهي مدينة عريقة تقع في سفح الأطلس المتوسط، تتميز بتاريخها التعايشي وتراثها المائي الغني.",
            "economy": "يعتمد اقتصادها بشكل أساسي على الفلاحة المسقية والسياحة الجبلية والصناعة التقليدية المرتبطة بالنسيج والعقد.",
            "monuments": [
                {"name": "شلال صفرو", "loc": "وسط المدينة", "desc": "متنفس طبيعي خلاب يجسد غنى المدينة بالمنابع المائية."},
                {"name": "المدينة القديمة والملاح", "loc": "المركز التاريخي", "desc": "شاهد على التعايش التاريخي وتضم أزقة ضيقة تعبق بالتاريخ."},
                {"name": "باب المقام", "loc": "مدخل المدينة", "desc": "أحد الأبواب التاريخية التي تحرس ذاكرة صفرو."}
            ],
            "crafts": "تشتهر عالمياً بصناعة 'العقد' التقليدية (أزرار القفطان) التي تعد مورد رزق لمئات النساء بالمنطقة.",
            "agri": "عاصمة حب الملوك (الكرز) عالمياً، بالإضافة إلى إنتاج الزيتون الرفيع والتين واللوز."
        },
        "فاس": {
            "intro": "العاصمة الروحية والعلمية للمملكة، أقدم مدينة إمبراطورية في المغرب ومصنفة تراثاً عالمياً من طرف اليونسكو.",
            "economy": "قطب سياحي وصناعي وتجاري ضخم، يعتمد على الصناعة التقليدية والتعليم والخدمات.",
            "monuments": [
                {"name": "جامعة القرويين", "loc": "فاس البالي", "desc": "أقدم جامعة في العالم لا تزال تدرس حتى الآن."},
                {"name": "دار الدباغ (شوارة)", "loc": "قرب واد فاس", "desc": "أكبر وأقدم مدبغة للجلود في العالم."},
                {"name": "باب بوجلود", "loc": "مدخل المدينة القديمة", "desc": "البوابة الزرقاء الشهيرة التي تفصل بين فاس الجديد وفاس البالي."}
            ],
            "crafts": "الزليج الفاسي، النحاسيات، الدباغة، والطرز الفاسي الأصيل.",
            "agri": "تعتمد ضواحيها (سهل سايس) على زيت الزيتون، الحبوب، والفواكه الموسمية."
        }
    }

    # جلب البيانات بناءً على المدينة المختارة
    city_info = city_wiki.get(user_city, {
        "intro": f"معلومات تعريفية عن {user_city} قيد التحديث...",
        "economy": "يتم الآن جمع البيانات الاقتصادية لهذه المنطقة...",
        "monuments": [{"name": "معالم المنطقة", "loc": "جاري التحديد", "desc": "ابحث عن المآثر التاريخية في مركز المدينة."}],
        "crafts": "صناعات يدوية محلية تعكس هوية المنطقة.",
        "agri": "إنتاجات فلاحية محلية متميزة."
    })

    # --- الجزء الأول: التعريف الشامل ---
    st.subheader("🌐 Overview & Economy / تعريف عام واقتصاد")
    st.write(f"**{user_city}:** {city_info['intro']}")
    st.info(f"💰 **Economy:** {city_info['economy']}")

    st.markdown("---")

    # --- الجزء الثاني: المآثر والمعالم بالترتيب ---
    st.subheader("🏛️ Monuments & Landmarks / المآثر والمعالم")
    for mon in city_info['monuments']:
        with st.expander(f"📍 {mon['name']}"):
            st.write(f"**Location:** {mon['loc']}")
            st.write(f"**Description:** {mon['desc']}")

    st.markdown("---")

    # --- الجزء الثالث: الصناعة التقليدية والفلاحة المجالية ---
    st.subheader("🧶 Crafts & Agriculture / الصناعة والفلاحة")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.success(f"**Handicrafts:** {city_info['crafts']}")
        st.caption("🛍️ يمكنكم زيارة الورشات المحلية في المدينة القديمة للتقدي.")
    with col_c2:
        st.warning(f"**Local Agriculture:** {city_info['agri']}")
        st.caption("🚜 تتوفر هذه المنتجات في الأسواق الأسبوعية والمحلات المختصة.")
st.markdown("---")
st.caption("Powered by Maison Balkiss AI - Tourism 4.0 | © 2026")
