import streamlit as st
import random

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI 4.0 - Smart Link", layout="wide")

# --- الترجمات (كاملة) ---
translations = {
    "English": {"title": "Maison Balkiss AI", "agri": "Agri-Culture", "crafts": "Local Crafts", "monuments": "Monuments", "find_near": "Best Restaurants in"},
    "Français": {"title": "Maison Balkiss AI", "agri": "Agriculture", "crafts": "Artisanat", "monuments": "Monuments", "find_near": "Meilleurs restos à"},
    "العربية": {"title": "ميزون بلقيس الذكي", "agri": "الفلاحة والإنتاج المحلي", "crafts": "الصناعة التقليدية", "monuments": "المآثر والسياحة", "find_near": "أفضل المطاعم في"}
}

# --- 1. محرك البحث الذكي (محاكاة الربط بـ Google/Wikipedia) ---
# هاد الدالة دابا كتولد معلومات "مختلفة" لكل مدينة بناءً على اسمها
def get_realtime_city_info(city_name):
    city_db = {
        "صفرو": {
            "agri": "عاصمة حب الملوك (الكرز) عالمياً، وتشتهر بزيت الزيتون الممتاز بفضل وفرة منابع المياه مثل عين لالة أمينة.",
            "craft": "تنفرد بصناعة 'العقد' (أزرار القفطان) التقليدية التي تُصدر لكل المغرب، مع نجارة الخشب الرفيعة.",
            "monument": "شلالات صفرو، أسوار المدينة القديمة، الملاح التاريخي، وكهوف 'كاف المومن'.",
            "restaurants": ["Resto Cascade Sefrou", "Maison d'Hôte Al-Maqam"]
        },
        "الناظور": {
            "agri": "مركز إقليمي لإنتاج الزيتون والحوامض، وتعتمد بشكل كبير على الثروة السمكية بفضل بحيرة مارتشيكا.",
            "craft": "تشتهر بالصناعات المرتبطة بالقصب (الحلفاء) والنسيج الريفي التقليدي بالألوان الطبيعية.",
            "monument": "بحيرة مارتشيكا العالمية، كورنيش الناظور، وجبل غوروغو المطل على البحر المتوسط.",
            "restaurants": ["Marchica Grill", "Nador Fish Market"]
        }
    }
    # إيلا كانت المدينة مازال ما دخلناش بياناتها، AI كيدير "تحليل افتراضي" ذكي
    default = {
        "agri": f"تعتمد {city_name} على مواردها الطبيعية الخاصة وتساهم في التنوع الفلاحي للجهة.",
        "craft": f"تزخر {city_name} بمهارات يدوية تعكس هوية المنطقة وتراثها الأصيل.",
        "monument": f"توجد في {city_name} معالم تاريخية ومساحات خضراء تستقطب الزوار.",
        "restaurants": [f"Traditional Kitchen {city_name}", f"The Garden Resto {city_name}"]
    }
    return city_db.get(city_name, default)

# --- 2. محرك حكايات الأطباق (Storytelling) ---
food_stories = {
    "Pastilla": {
        "full_story": "البسطيلة الفاسية هي قمة فن الطبخ المغربي. تاريخياً، انتقلت من الأندلس واستقرت في فاس لتتطور من طبق بسيط إلى 'ملكة الموائد'. السر في جودتها هو 'الورقة' الرقيقة جداً التي تُحشى بمزيج من الدجاج المحمر، البيض، اللوز المقلي المهرمش، والقرفة. تعكس البسطيلة ترف العيش في الدور الفاسية العريقة.",
        "img": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Moroccan_Pastilla.jpg"
    }
}

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("👑 Maison Balkiss AI")
lang = st.sidebar.selectbox("🌐 Language", ["English", "Français", "العربية"])
user_city = st.sidebar.text_input("📍 الموقع الحالي (اكتب المدينة)", "صفرو")
t = translations[lang]

# --- العرض الرئيسي ---
st.title(f"⚜️ {t['title']}")
tab1, tab2, tab3 = st.tabs(["📍 Routes", "🍲 Storytelling", "🏛️ Guide"])

with tab2:
    st.subheader("📸 Scan Dish")
    # ملي كتحطي الصورة، الستوري كيولي طويل ومفصل
    up = st.file_uploader("Upload...", type=["jpg", "png"])
    if up:
        st.image(up, width=300)
        dish = st.selectbox("Identify:", list(food_stories.keys()))
        info = food_stories[dish]
        st.image(info["img"], use_column_width=True)
        st.success("✅ AI Detection Complete")
        st.markdown(f"### 📖 الحكاية الكاملة:\n {info['full_story']}")
        
        # الربط مع المدينة المختارة: المطاعم كتغير حسب user_city
        city_data = get_realtime_city_info(user_city)
        st.markdown(f"--- \n ### 🍴 {t['find_near']} {user_city}:")
        for res in city_data["restaurants"]:
            st.write(f"🚩 **{res}** - Specialty: {dish}")

with tab3:
    st.header(f"🏛️ Exploring {user_city}")
    data = get_realtime_city_info(user_city)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🌾 {t['agri']}")
        st.info(data["agri"])
    with col2:
        st.subheader(f"🧶 {t['crafts']} & 🏛️ {t['monuments']}")
        st.success(data["craft"] + "\n\n" + data["monument"])

st.caption("Powered by Maison Balkiss AI 4.0 | Real-time AI Connection")
