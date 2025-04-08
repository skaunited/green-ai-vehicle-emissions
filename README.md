# Projet Data Science - Émissions de CO2 des Véhicules

## 🚀 Guide Complet d'Installation et d'Exécution

### Prérequis Système
- **Système d'exploitation** : Windows 10+/macOS 10.15+/Linux Ubuntu 18.04+
- **Disque dur** : 10 GB d'espace libre (pour les datasets volumineux)
- **Mémoire RAM** : 8 GB minimum (16 GB recommandé)

### 1. Installation des Outils de Base

#### 1.1. Installer Git
```bash 
sudo apt-get install git  # Linux
```

```bash 
brew install git         # macOS
```

```bash 
https://git-scm.com/download/win # Windows
```

#### 1.2. Installer Git LFS (pour les gros fichiers)

```bash 
git lfs install
```

#### 1.3. Installer Anaconda

```bash
# Windows
wget "https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe" -outfile "./Downloads/Anaconda3-2024.10-1-Windows-x86_64.exe"  
```

```bash
# MacOS & Linux
curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-aarch64.sh
```
Pour plus d'information merci de consulter la [documentation officiel](https://www.anaconda.com/docs/getting-started/anaconda/install)

### 2. Vérification des installations :

```bash
git --version
conda --version
git lfs --version
```
### 3. Structure Recommandée
```bash
projet-co2-vehicules/
│
├── .gitignore
├── README.md          # Ce fichier
├── environment.yml     # Configuration Anaconda
├── requirements.txt    # Dépendances Python
│
├── data/
│   ├── raw/           # Données brutes
│   ├── processed/     # Données nettoyées
│   └── external/      # Données externes
│
├── notebooks/
│   ├── exploration/    # Notebooks d'analyse exploratoire
│   └── modeling/      # Notebooks de modélisation
│
├── src/
│   ├── data/          # Scripts de preprocessing
│   ├── features/      # Feature engineering
│   ├── models/        # Scripts de modélisation
│   └── visualization/ # Scripts de visualisation
│
└── streamlit_app/     # Application Streamlit
    ├── app.py
    └── assets/
```

### 5. Outils et Bibliothèques, 
Les différents bibliothèques qu'on va trouver dans `environment.yml`

#### Core Data Science Stack
* Python 3.9+ (version stable recommandée)
* Jupyter Lab (pour l'exploration interactive)
* Pandas (manipulation des données)
* NumPy (calculs scientifiques)
* Scikit-learn (modélisation ML)
* Matplotlib/Seaborn (visualisation)
* Plotly (visualisations interactives)

#### Pour Streamlit
* Streamlit (création de dashboard)
* Streamlit-aggrid (tables interactives)
* Plotly Express (visualisations intégrables)

#### Gestion des Données
* Dask ou Polars (pour gros datasets >1GB)
* PyArrow (format Parquet pour efficacité)

#### Qualité de Code
* Pre-commit (validation avant commit)
* Black (formatage automatique)
* Flake8 (linting)
* Pylint (analyse de code)

### 6. Configuration Initiale du Projet
```bash
# 1. Cloner le dépôt avec Git
git clone https://github.com/skaunited/green-ai-vehicle-emissions.git
cd green-ai-vehicle-emissions

# 2. Télécharger les données (2 méthodes)
# Méthode manuelle :
# - Télécharger depuis data.gouv.fr
# - Placer dans data/raw/emissions_2013.csv
# OU
# Méthode script :
python scripts/download_data.py
```

### 7. Création de l'Environnement Conda
```bash
# 1. Créer l'environnement
conda env create -f environment.yml

# 2. Activer l'environnement
conda activate co2-vehicules

# 3. Vérifier l'installation
python -c "import pandas; print(pandas.__version__)"
```

### 8. Premier Lancement du Projet
```bash
streamlit run streamlit_app/app.py
```
Ensuite il faut ouvrir [http://localhost:8501](http://localhost:8501) dans votre navigateur

### 9. Workflow Quotidien de Développement
```bash
# 1. Clone la branche de developpement:
git checkout main
git pull origin main

# 2. Création de branche par feature:
# Attention cette étape est imperatif on ne travaille jamais dans la branche de developpement:
git checkout -b feature/ma-nouvelle-feature

# 3. Vérifier le code
flake8 src/
pylint src/

# 4. Formatter le code
black src/

# 5. Valider les changements
git add .
git commit -m "Message descriptif"
git push origin feature/ma-nouvelle-feature
```