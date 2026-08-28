# Çalıştırma Sonuçları

Tüm notebooklar 26 Ağustos 2026 tarihinde baştan sona çalıştırılmıştır. Aşağıdaki değerler
notebookların kaydettiği test/çapraz doğrulama sonuçlarıdır.

| No | Proje | Seçilen yaklaşım / çıktı | Temel sonuç |
|---:|---|---|---|
| 01 | Öğrenci başarısı | Random Forest | MAE 1.221, R² 0.796 |
| 02 | Auto MPG | Random Forest | MAE 1.514, R² 0.925 |
| 03 | Gayrimenkul değeri | Random Forest | MAE 3.732, R² 0.820 |
| 04 | Iris | Lojistik Regresyon | Accuracy 0.921 |
| 05 | Meme kanseri | Lojistik Regresyon | ROC-AUC 0.995, F1 0.965 |
| 06 | Banka pazarlama | Linear SVM | F1 0.558, Balanced Accuracy 0.832 |
| 07 | Toptan müşteri kümeleme | K-Means, k=2 | Silhouette 0.290 |
| 08 | Şarap kümeleme | K-Means, k=3 | Silhouette 0.285, ARI 0.897 |
| 09 | Rakam tanıma | RBF-SVM | Accuracy 0.981 |
| 10 | Renk sıkıştırma | MiniBatch K-Means, 16 renk | MSE 0.001861 |
| 11 | SMS spam | Lojistik Regresyon | Spam F1 0.936 |
| 12 | Film yorumu konu modelleme | TF-IDF + NMF | 2.000 belge, 6 konu |
| 13 | İçerik tabanlı öneri | TF-IDF + Nearest Neighbors | 9.742 film |
| 14 | İşbirlikçi öneri | Sparse KNN | 100.836 puan, 610 kullanıcı |
| 15 | CO₂ tahmini | Ridge | MAE 0.373 ppm |
| 16 | Güneş lekesi tahmini | Ridge | MAE 14.609 |
| 17 | Penguen görselleştirme | EDA | 344 satır, 3 tür |
| 18 | Titanic görselleştirme | EDA | 1.309 yolcu, hayatta kalma %38,2 |
| 19 | Derin MLP rakam | 128–64–32 MLP | Accuracy 0.972, 37 epoch |
| 20 | Derin MLP enerji | MLP + RF baseline | MLP 195 epoch; en iyi R² 0.998 |
| 21 | Model seçim ajanı | RBF-SVM | 5-fold macro-F1 0.983 |

Metriklerin ham ve makinece okunabilir halleri `results/*.json` dosyalarındadır. Kümeleme,
öneri ve EDA projelerinde klasik supervised test metriği yerine probleme uygun çıktı raporlanmıştır.
