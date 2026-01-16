\# Mini-projet MLOps - ML



\## 1. Description

Ce projet illustre un pipeline simple d'entraînement et d'évaluation d'un modèle ML sur le dataset Iris.



\- Dataset utilisé : Iris (inclus dans le script)

\- Modèle : Logistic Regression

\- Pipeline : train -> evaluate -> artefacts générés dans `artifacts/`



---



\## 2. Structure du projet



mlops-ml-project/

│

├── artifacts/ # Résultats et rapports

├── config/ # Fichiers YAML de configuration

│ └── train.yaml

├── data/ # Données (si nécessaire)

├── notebooks/ # Jupyter notebooks (optionnel)

├── scripts/ # Scripts Python pour entraîner et évaluer

│ ├── train.py

│ └── evaluate.py

├── src/ # Code source (data, features, model)

│ ├── init.py

│ ├── data.py

│ ├── features.py

│ └── model.py

├── tests/ # Tests unitaires

│ └── test\_config.py

├── requirements.txt # Dépendances Python

└── README.md



---



\## 3. Prérequis



\- Python >= 3.12

\- Virtualenv (optionnel mais recommandé)

\- Pip



---



\## 4. Installation



1\. Cloner le projet :



```bash

git clone https://github.com/Masaafkhaoula/Atelier-MLOps---Mini-projet-ML-Git.git

cd mlops-ml-project




\#Auteur: Masaaf Khaoula (Kham)


