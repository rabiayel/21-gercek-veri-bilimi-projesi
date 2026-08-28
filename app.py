
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models"

st.set_page_config(page_title="Rabia Yel | 21 Veri Bilimi Projesi", page_icon="📊", layout="wide")
st.title("21 Gerçek Veri Bilimi Projesi")
st.caption("Gerçek açık veri • EDA • model karşılaştırması • kaydedilmiş modeller")

@st.cache_resource
def load_model(filename):
    return joblib.load(MODEL_DIR / filename)

page = st.sidebar.radio(
    "Bölüm",
    ["Proje kataloğu", "Iris tahmini", "Auto MPG tahmini", "SMS spam", "Film önerisi", "Enerji yükü"],
)

if page == "Proje kataloğu":
    catalog = pd.read_csv(ROOT / "project_catalog.csv")
    st.subheader("21 ayrı notebook")
    st.dataframe(catalog, width="stretch", hide_index=True)
    st.info("Notebooklar `notebooks/`, modeller `models/`, veri kaynakları `DATA_SOURCES.md` klasöründedir.")

elif page == "Iris tahmini":
    st.subheader("Iris türü tahmini")
    artifact = load_model("04_iris.joblib")
    col1, col2 = st.columns(2)
    sepal_length = col1.slider("Sepal uzunluğu (cm)", 4.0, 8.0, 5.8, .1)
    sepal_width = col2.slider("Sepal genişliği (cm)", 2.0, 4.5, 3.0, .1)
    petal_length = col1.slider("Petal uzunluğu (cm)", 1.0, 7.0, 4.3, .1)
    petal_width = col2.slider("Petal genişliği (cm)", .1, 2.6, 1.3, .1)
    row = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                       columns=artifact["feature_names"])
    label = artifact["target_names"][artifact["best_model"].predict(row)[0]]
    st.success(f"Tahmin edilen tür: {label}")

elif page == "Auto MPG tahmini":
    st.subheader("Otomobil yakıt verimliliği")
    artifact = load_model("02_auto_mpg.joblib")
    c1, c2 = st.columns(2)
    values = {
        "cylinders": c1.selectbox("Silindir", [3, 4, 5, 6, 8], index=1),
        "displacement": c2.number_input("Motor hacmi", 60.0, 500.0, 140.0),
        "horsepower": c1.number_input("Beygir gücü", 40.0, 250.0, 90.0),
        "weight": c2.number_input("Ağırlık (lb)", 1500.0, 5500.0, 2800.0),
        "acceleration": c1.number_input("Hızlanma", 8.0, 25.0, 15.5),
        "model_year": c2.slider("Model yılı kodu", 70, 82, 76),
        "origin": c1.selectbox("Menşei kodu", [1, 2, 3]),
    }
    prediction = artifact["best_model"].predict(pd.DataFrame([values]))[0]
    st.metric("Tahmini MPG", f"{prediction:.1f}")

elif page == "SMS spam":
    st.subheader("SMS spam kontrolü")
    artifact = load_model("11_sms_spam.joblib")
    message = st.text_area("İngilizce SMS metni", "Congratulations! You won a free prize, call now.")
    if message:
        label = artifact["best_model"].predict([message])[0]
        (st.error if label == "spam" else st.success)(f"Model sonucu: {label}")

elif page == "Film önerisi":
    st.subheader("MovieLens içerik tabanlı öneri")
    artifact = load_model("13_movielens_icerik.joblib")
    movies = artifact["movies"]
    title = st.selectbox("Film seçin", movies.title.sort_values())
    idx = movies.index[movies.title.eq(title)][0]
    distances, indices = artifact["model"].kneighbors(artifact["matrix"][idx], n_neighbors=6)
    recommendations = movies.iloc[indices[0][1:]][["title", "genres"]].copy()
    recommendations["benzerlik"] = (1 - distances[0][1:]).round(3)
    st.dataframe(recommendations, width="stretch", hide_index=True)

else:
    st.subheader("Bina ısıtma yükü tahmini")
    artifact = load_model("20_enerji_yuku.joblib")
    c1, c2 = st.columns(2)
    values = {
        "relative_compactness": c1.slider("Göreli kompaktlık", .60, 1.00, .80, .01),
        "surface_area": c2.slider("Yüzey alanı", 500.0, 850.0, 670.0),
        "wall_area": c1.slider("Duvar alanı", 240.0, 420.0, 320.0),
        "roof_area": c2.slider("Çatı alanı", 110.0, 230.0, 170.0),
        "overall_height": c1.selectbox("Yükseklik", [3.5, 7.0]),
        "orientation": c2.selectbox("Yön kodu", [2, 3, 4, 5]),
        "glazing_area": c1.selectbox("Camlama oranı", [0.0, 0.1, 0.25, 0.4], index=2),
        "glazing_area_distribution": c2.selectbox("Camlama dağılımı", [0, 1, 2, 3, 4, 5], index=3),
    }
    prediction = artifact["best_model"].predict(pd.DataFrame([values]))[0]
    st.metric("Tahmini ısıtma yükü", f"{prediction:.2f}")

st.divider()
st.caption("Eğitim/portföy uygulamasıdır. Tıbbi, finansal veya mühendislik kararı yerine kullanılamaz.")
