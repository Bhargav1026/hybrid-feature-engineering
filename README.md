# Hybrid Feature Engineering

🚀 **Hybrid Feature Engineering for Image and Audio Classification using Deep Embeddings**

This repository presents an academic-to-industry grade **machine learning project** that explores how **hybrid deep feature representations** can improve performance on vision and audio classification tasks.

Instead of training large models end-to-end, this project treats **state-of-the-art pre-trained networks as feature extractors**, combines their embeddings, and evaluates the effectiveness of different fusion strategies using lightweight classifiers.

---

## 📌 Key Highlights

- 🔹 Hybrid feature banks built from **multiple pre-trained models**
- 🔹 Image experiments on **CIFAR-10**
- 🔹 Audio experiments on **ESC-50**
- 🔹 Mutual Information–based feature selection
- 🔹 Attention-style feature fusion
- 🔹 UMAP visualizations for feature space analysis
- 🔹 Ethical perspective emphasizing **transparency and responsible AI**

---

## 🧠 Models Used

### 🖼 Image Feature Extractors
- **CLIP** – semantic visual embeddings
- **DINOv2** – self-supervised visual representations
- **MAE (Masked Autoencoder)** – global structural features

### 🔊 Audio Feature Extractors
- **MFCCs** – classical handcrafted audio features
- **AST (Audio Spectrogram Transformer)** – transformer-based audio embeddings

---

## 📁 Project Structure

hybrid-feature-engineering/
│
├── hybrid_feature_bank/
│ ├── hybrid_feature_bank.ipynb # Image feature experiments
│ ├── hybrid_feature_bank_audio.ipynb # Audio feature experiments
│
├── scripts/
│ ├── download_cifar10.py
│ ├── download_esc50.py
│
├── .gitignore
├── README.md
└── LICENSE

yaml


> 📌 **Note:** Datasets and generated artifacts are intentionally excluded from version control.

---

## 🧪 Methodology Overview

### Image Pipeline
1. Extract embeddings from CLIP, DINOv2, and MAE
2. Evaluate single-model baselines
3. Create hybrid embeddings via concatenation
4. Apply:
   - Mutual Information feature selection
   - Attention-based feature fusion
5. Train a **linear classifier (Logistic Regression)**

### Audio Pipeline
1. Extract MFCC features
2. Extract AST embeddings
3. Evaluate:
   - MFCC-only
   - AST-only
   - MFCC + AST hybrid features

---

## 📊 Results Snapshot

### CIFAR-10 (Image Classification)

| Feature Set | Accuracy |
|------------|----------|
| CLIP | ~94.0% |
| DINOv2 | ~96.4% |
| CLIP + DINOv2 | **~96.8%** |
| CLIP + DINOv2 + MAE | **~96.9%** |

### ESC-50 (Audio Classification)

| Feature Set | Accuracy |
|------------|----------|
| MFCC | ~30% |
| AST | **~94.3%** |
| MFCC + AST | ~93.8% |

---

## 📈 Visualization

- **UMAP** is used to visualize high-dimensional feature spaces
- Helps interpret:
  - Class separability
  - Feature redundancy
  - Effects of fusion and selection

---

## ⚖️ Ethical Considerations

This project adopts a **beneficence-based ethical framework**, focusing on:
- Transparency of representations
- Auditable feature pipelines
- Avoiding black-box decision making
- Responsible reuse of pre-trained models

---

## 🛠 Setup & Usage

```bash
git clone https://github.com/Bhargav1026/hybrid-feature-engineering.git
cd hybrid-feature-engineering
Install dependencies (example):

bash

pip install numpy scikit-learn matplotlib librosa torch
Run notebooks:

hybrid_feature_bank.ipynb

hybrid_feature_bank_audio.ipynb

📚 Academic Context
This project was developed as part of a graduate-level Feature Engineering / Machine Learning coursework and structured to be reusable as a research prototype or ML portfolio project.

🔮 Future Work
Extend to multimodal (image + audio + text) fusion

Evaluate on larger, real-world datasets

Add fairness and bias analysis

Persist feature banks for downstream inference

👤 Author
Bhargava Sai Vardhan Gunapu
M.S. in Computer Science
University of North Texas

⭐ If you find this useful
Give the repo a ⭐ — it really helps!



---


