import streamlit as st
import pandas as pd

# 1. إعداد الصفحة والستايل
st.set_page_config(page_title="Maison Balkiss AI - Smart Tourism 4.0", layout="wide")

# --- كود PWA للتثبيت ---
st.markdown("""<script>if ('serviceWorker' in navigator) { navigator.serviceWorker.register('https://cdn.ifier.io/gh/michelegera/pwa-streamlit/sw.js'); }</script>""", unsafe_allow_html=True)

# --- 2. الترجمات الشاملة (محفوظة بالكامل) ---
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
        "find_near": "Best places near you in",
        "location": "Location",
        "agri": "Agriculture & Economy",
        "crafts": "Local Crafts",
        "monuments": "Monuments & Heritage"
    },
    "Français": {
        "title": "Maison Balkiss : IA Héritage & Gastronomie",
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
        "find_near": "Meilleurs endroits à",
        "location": "Localisation",
        "agri": "Agriculture & Économie",
        "crafts": "Artisanat Local",
        "monuments": "Monuments & Patrimoine"
    },
    "العربية": {
        "title": "ميزون بلقيس: الذكاء الاصطناعي والتراث الغذائي",
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
        "find_near": "أفضل الأماكن في",
        "location": "الموقع الحالي",
        "agri": "الفلاحة والاقتصاد",
        "crafts": "الصناعة التقليدية",
        "monuments": "المآثر والتراث"
    }
}

# --- 3. محرك البيانات الحقيقية (الذكاء المكاني) ---
# هنا نضع الفوارق الحقيقية بين المدن
city_wiki_data = {
    "صفرو": {
        "agri": "عاصمة حب الملوك (الكرز) عالمياً، تشتهر بإنتاج الزيتون الرفيع بفضل منابع 'عين لالة أمينة'.",
        "craft": "تنفرد بمهارة نساء المدينة في صناعة 'العقد' التقليدية التي تزين القفطان المغربي.",
        "monument": "شلال صفرو العظيم، أسوار المدينة التاريخية، وكهوف 'كاف المومن'.",
        "maps_query": "Sefrou+Monuments+Restaurants"
    },
    "Figuig": {
        "agri": "واحة النخيل العريقة، مشهورة بتمور 'عزيزة' والفقارات (نظام ري تقليدي فريد).",
        "craft": "تتميز بالنسيج 'الفكيكي' التقليدي وصناعة الحايك والجلابة الصوفية الأصيلة.",
        "monument": "الصومعة الحجرية لقصر الوداغير، الواحات السبع، والقصور التاريخية.",
        "maps_query": "Figuig+Oasis+Heritage"
    },
    "Tanger": {
        "agri": "منطقة استراتيجية تعتمد على الصيد البحري ومنتجات جبال الريف المتنوعة.",
        "craft": "تشتهر بالصناعات
