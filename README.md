# Vpr vs Vpx Protein Classification

Machine learning pipeline for **classifying HIV accessory proteins Vpr and Vpx** using **protein sequence k-mers and TF-IDF feature extraction**.

The project parses protein sequences from FASTA files, generates **k-mer representations**, converts them into **TF-IDF vectors**, and trains ensemble machine learning models to classify the proteins.

---

## Overview

Protein sequences are processed through the following pipeline:

```
FASTA Protein Sequences
        │
        ▼
Sequence Filtering (Vpr / Vpx)
        │
        ▼
K-mer Generation (k = 10)
        │
        ▼
TF-IDF Feature Extraction
        │
        ▼
Machine Learning Models
   ├── Random Forest
   └── Extra Trees
        │
        ▼
Protein Classification
```

---

## Dataset

Protein sequences are extracted from FASTA files located in:

```
unreviewed/
```

Sequences are labeled based on their description:

| Protein | Label |
| ------- | ----- |
| Vpr     | 0     |
| Vpx     | 1     |

The dataset is balanced with equal numbers of Vpr and Vpx proteins.

---

## Repository Structure

```
.
├── .idea/                              # IDE configuration files
├── unreviewed/                         # Raw FASTA protein sequences
├── vpR_vpx/                            # Processed datasets / intermediate outputs
│
├── data.pkl                            # Serialized dataset containing protein sequences
├── label.pkl                           # Serialized labels
│
├── kmer_feature_creator.py             # Generates k-mer features from protein sequences
├── split_vpr_vpx_vif.py                # Extracts and splits protein classes
│
└── vpr_vpx_classification_model.ipynb  # Notebook for training and evaluating models
```

---

## Feature Engineering

Protein sequences are transformed into **k-mers** using a sliding window.

Example sequence:

```
MEQAPEDHGPQREPY
```

Generated 10-mers:

```
MEQAPEDHGP
EQAPEDHGPQ
QAPEDHGPQR
APEDHGPQRE
```

These k-mers capture **local sequence patterns** within proteins.

---

## TF-IDF Vectorization

K-mer sequences are converted into **TF-IDF vectors** using Scikit-learn.

This representation captures:

* frequency of k-mers within sequences
* importance of k-mers across the dataset

Typical feature space:

```
~3000+ features per sequence
```

---

## Machine Learning Models

Two ensemble classifiers are used:

### Random Forest

* Ensemble of decision trees
* Works well with high-dimensional sparse data

### Extra Trees

* Extremely randomized tree ensemble
* Faster and less prone to overfitting in some cases

Example training:

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kbrunnerLXG/hmmvml.git
cd hmmvml
```

Install dependencies:

```bash
pip install biopython pandas scikit-learn numpy jupyter
```

---

## Usage

### 1. Extract and label proteins

```bash
python split_vpr_vpx_vif.py
```

### 2. Generate k-mer features

```bash
python kmer_feature_creator.py
```

### 3. Train and evaluate the model

Open the notebook:

```
vpr_vpx_classification_model.ipynb
```

The notebook:

* loads the dataset
* generates TF-IDF features
* trains machine learning models
* evaluates classification accuracy

---

## Dependencies

* Python 3.x
* Biopython
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

Install via:

```bash
pip install biopython pandas scikit-learn numpy jupyter
```

---

## Future Improvements

Possible extensions:

* Cross-validation experiments
* Feature importance analysis
* Confusion matrix and classification metrics
* Deep learning models for protein sequences
* Transformer embeddings (ESM / ProtBERT)

---

## Author

Aditya

GitHub:
[https://github.com/kbrunnerLXG](https://github.com/kbrunnerLXG)


