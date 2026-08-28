# GitHub ve Hugging Face Yayınlama

## GitHub

Bu klasörü yeni bir GitHub reposunun kökü olarak yükleyin. Modeller ve veri dosyaları toplam boyut
sınırını aşarsa Git LFS kullanın: `git lfs track "*.joblib"`.

## Hugging Face Space

- Space SDK: Streamlit
- Python: 3.12
- Ana dosya: `app.py`
- Kurulum: `requirements.txt`

Uygulama yerelde `streamlit run app.py` komutuyla doğrulanabilir. Yayın sırasında model artifact'leri
`models/` klasörüyle birlikte bulunmalıdır. Hugging Face hesabında yeni Space oluşturma ve son push
işlemi hesap erişimi gerektirir.
