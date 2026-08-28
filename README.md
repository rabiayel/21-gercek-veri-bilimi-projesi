

# 21 Gerçek Veri Bilimi Projesi

Bu depo, ödev geri bildirimi doğrultusunda baştan hazırlanmış 21 ayrı Jupyter Notebook içerir.
Sentetik/rastgele üretilmiş gözlem yoktur. Her proje gerçek ve kaynaklandırılmış bir veri setiyle;
veri kalitesi kontrolü, EDA, görselleştirme, modelleme/değerlendirme ve sonuç yorumu sunar.

## Teslim yapısı

- `notebooks/`: 21 ayrı, çalıştırılmış `.ipynb`
- `data/`: notebookların çevrimdışı da çalışması için gerçek veri kopyaları
- `models/`: notebooklarda eğitilip `joblib` ile kaydedilmiş model artifact'leri
- `results/`: model metrikleri ve EDA özetleri
- `MODEL_RESULTS.md`: çalıştırılmış notebooklardan toplu sonuç özeti
- `app.py`: Streamlit uygulaması
- `DATA_SOURCES.md`: veri kaynağı ve kullanım notları
- `OGRETMEN_GERI_BILDIRIMI_KONTROL_LISTESI.md`: geri bildirim–düzeltme eşlemesi

## Yerelde çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Notebookları proje kökünden Jupyter/VS Code ile açın. Her notebook, `data/`, `models/` ve `results/`
yollarını otomatik bulur.

## GitHub'a yükleme

```bash
git init
git add .
git commit -m "21 real-data science projects"
git branch -M main
git remote add origin GITHUB_REPO_ADRESINIZ
git push -u origin main
```

## Hugging Face Spaces

1. Hugging Face üzerinde **New Space** seçin.
2. SDK olarak **Streamlit** kullanın.
3. Bu deponun tamamını Space'e yükleyin.
4. `README.md` başındaki Space metadata ve `app.py` otomatik algılanır.

Çalışmada kullanılan açık veri setlerinin telif/lisans koşulları kendi sahiplerine aittir;
ayrıntılı bağlantılar `DATA_SOURCES.md` dosyasındadır.
