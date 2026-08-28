# 21 Gerçek Veri Bilimi Projesi

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.62-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Bu depo; regresyon, sınıflandırma, kümeleme, bilgisayarlı görü, doğal dil işleme, öneri sistemleri, zaman serileri, veri görselleştirme, derin öğrenme ve AI Agents alanlarında hazırlanmış **21 ayrı veri bilimi projesini** içerir.

Çalışmaların tamamında gerçek ve kaynaklandırılmış veri setleri kullanılmıştır. Her notebook; veri kalite kontrolleri, keşifsel veri analizi (EDA), görselleştirme, veri ön işleme, modelleme veya probleme uygun analiz, değerlendirme ve sonuç yorumlama adımlarını içerir.

## Projenin amacı

Bu çalışmanın temel amaçları şunlardır:

- Farklı veri bilimi problemlerinde uçtan uca proje geliştirmek
- Gerçek veri setlerinde veri temizleme ve EDA uygulamak
- Uygun projelerde birden fazla yaklaşımı karşılaştırmak
- Başarıyı probleme uygun metriklerle değerlendirmek
- Eğitilen modelleri yeniden kullanılabilir biçimde kaydetmek
- Sonuçları Streamlit arayüzünde erişilebilir hâle getirmek
- Çalışmaları ayrı ve çalıştırılmış Jupyter Notebook dosyalarıyla sunmak

## Projeler ve sonuçlar

| No | Alan | Proje | Veri seti | Yaklaşım / temel sonuç |
|---:|---|---|---|---|
| 01 | Regresyon | [Öğrenci başarı notu tahmini](notebooks/01_regresyon_ogrenci_basari.ipynb) | UCI Student Performance | Random Forest — MAE: 1.221, R²: 0.796 |
| 02 | Regresyon | [Otomobil yakıt verimliliği](notebooks/02_regresyon_otomobil_yakit.ipynb) | UCI Auto MPG | Random Forest — MAE: 1.514, R²: 0.925 |
| 03 | Regresyon | [Gayrimenkul birim fiyat tahmini](notebooks/03_regresyon_gayrimenkul_deger.ipynb) | UCI Real Estate Valuation | Random Forest — MAE: 3.732, R²: 0.820 |
| 04 | Sınıflandırma | [Iris çiçek türü sınıflandırması](notebooks/04_siniflandirma_iris.ipynb) | Fisher Iris | Lojistik Regresyon — Accuracy: 0.921 |
| 05 | Sınıflandırma | [Meme kanseri tanı sınıflandırması](notebooks/05_siniflandirma_meme_kanseri.ipynb) | Wisconsin Diagnostic Breast Cancer | Lojistik Regresyon — ROC-AUC: 0.995, F1: 0.965 |
| 06 | Sınıflandırma | [Banka kampanyası yanıt tahmini](notebooks/06_siniflandirma_banka_pazarlama.ipynb) | UCI Bank Marketing | Linear SVM — F1: 0.558, Balanced Accuracy: 0.832 |
| 07 | Kümeleme | [Toptan müşteri segmentasyonu](notebooks/07_kumeleme_toptan_musteri.ipynb) | UCI Wholesale Customers | K-Means, k=2 — Silhouette: 0.290 |
| 08 | Kümeleme | [Şarap kimyasıyla kümeleme](notebooks/08_kumeleme_sarap_kimyasi.ipynb) | UCI Wine | K-Means, k=3 — Silhouette: 0.285, ARI: 0.897 |
| 09 | Bilgisayarlı Görü | [El yazısı rakam tanıma](notebooks/09_bilgisayarli_goru_rakam_tanima.ipynb) | scikit-learn Digits | RBF-SVM — Accuracy: 0.981 |
| 10 | Bilgisayarlı Görü | [Fotoğrafta renk sıkıştırma](notebooks/10_bilgisayarli_goru_renk_sikistirma.ipynb) | scikit-learn China photograph | MiniBatch K-Means, 16 renk — MSE: 0.001861 |
| 11 | NLP | [SMS spam sınıflandırması](notebooks/11_nlp_sms_spam.ipynb) | UCI SMS Spam Collection | TF-IDF + Lojistik Regresyon — Spam F1: 0.936 |
| 12 | NLP | [Film yorumlarında konu modelleme](notebooks/12_nlp_film_yorumlari_konu_modelleme.ipynb) | NLTK Movie Reviews | TF-IDF + NMF — 2.000 belge, 6 konu |
| 13 | Öneri Sistemleri | [İçerik tabanlı film önerisi](notebooks/13_oneri_movielens_icerik.ipynb) | MovieLens latest-small | TF-IDF + Nearest Neighbors — 9.742 film |
| 14 | Öneri Sistemleri | [İşbirlikçi film önerisi](notebooks/14_oneri_movielens_isbirlikci.ipynb) | MovieLens latest-small | Sparse KNN — 100.836 puan, 610 kullanıcı |
| 15 | Zaman Serisi | [Atmosferik CO₂ tahmini](notebooks/15_zaman_serisi_co2_tahmin.ipynb) | Mauna Loa Weekly CO₂ | Ridge — MAE: 0.373 ppm |
| 16 | Zaman Serisi | [Güneş lekesi aktivitesi tahmini](notebooks/16_zaman_serisi_gunes_lekesi.ipynb) | Annual Sunspots | Ridge — MAE: 14.609 |
| 17 | Veri Görselleştirme | [Palmer Penguenleri EDA](notebooks/17_veri_gorsellestirme_penguen.ipynb) | Palmer Penguins | 344 gözlem ve 3 tür üzerinde görsel analiz |
| 18 | Veri Görselleştirme | [Titanic yolcu verisi EDA](notebooks/18_veri_gorsellestirme_titanic.ipynb) | OpenML Titanic 40945 | 1.309 yolcu; genel hayatta kalma oranı: %38,2 |
| 19 | Derin Öğrenme | [Derin MLP ile rakam sınıflandırma](notebooks/19_derin_ogrenme_mlp_rakam.ipynb) | scikit-learn Digits | 128–64–32 MLP — Accuracy: 0.972 |
| 20 | Derin Öğrenme | [Derin MLP ile bina ısıtma yükü](notebooks/20_derin_ogrenme_enerji_yuku.ipynb) | UCI Energy Efficiency | MLP + Random Forest karşılaştırması — en iyi R²: 0.998 |
| 21 | AI Agents | [Otomatik model seçim ajanı](notebooks/21_ai_agent_otomatik_model_secimi.ipynb) | UCI Wine | RBF-SVM — 5-fold Macro-F1: 0.983 |

Sonuçların ayrıntılı özeti [`MODEL_RESULTS.md`](MODEL_RESULTS.md), makinece okunabilir metrikler ise [`results/`](results/) klasöründe yer alır.

## Proje yapısı

```text
Rabia_Yel_21_Gercek_Veri_Projesi/
├── notebooks/          # 21 ayrı ve çalıştırılmış Jupyter Notebook
├── data/               # Gerçek veri setlerinin çevrimdışı kopyaları
├── models/             # Eğitilmiş model dosyaları (.joblib)
├── results/            # Metrik ve EDA sonuçları (.json)
├── app.py              # Streamlit uygulaması
├── project_catalog.csv # Proje kataloğu
├── MODEL_RESULTS.md     # Toplu model sonuçları
├── DATA_SOURCES.md      # Veri kaynakları ve bağlantılar
├── DEPLOYMENT.md        # Yayınlama notları
├── requirements.txt    # Python bağımlılıkları
└── LICENSE              # MIT Lisansı
```


## Veri ve modeller

- Kullanılan veri setlerinin tamamı gerçek verilerden oluşur; sentetik veya rastgele üretilmiş gözlem kullanılmamıştır.
- Veri setleri, çalışmanın çevrimdışı ve yeniden üretilebilir olması amacıyla `data/` klasöründe tutulur.
- Kaynak bağlantıları ve kullanım notları [`DATA_SOURCES.md`](DATA_SOURCES.md) dosyasında yer alır.
- Modelleme içeren 19 çalışma için eğitilmiş `.joblib` dosyaları `models/` klasörüne kaydedilmiştir.
- Yalnızca görsel analiz içeren 17 ve 18 numaralı projelerde model dosyası bulunmaz.


## Referans proje listeleri

Proje seçimi ve alternatif çözüm incelemelerinde aşağıdaki çalışma listelerinden yararlanılmıştır:

- [75 Data Science Projects](https://python.plainenglish.io/85-data-science-projects-c03c8750599e)
- [230 Machine Learning Projects with Python](https://medium.com/coders-camp/230-machine-learning-projects-with-python-5d0c7abf8265)

## Lisans

Proje kodları [`MIT Lisansı`](LICENSE) ile sunulmaktadır. Veri setlerinin lisans ve kullanım koşulları kendi sağlayıcılarına aittir.

