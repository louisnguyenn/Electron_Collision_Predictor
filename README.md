# ⚛️ Electron Collision Invariant Mass Prediction

## 🔍 Project Overview  
This project uses linear regression to predict the **invariant mass** resulting from **CERN electron collision data**. By leveraging the energies of two colliding electrons (`E1` and `E2`), the model estimates the mass produced from the event. The project includes data cleaning, exploratory visualization, model training, and performance evaluation, all conducted in an interactive Jupyter Notebook environment.

---

## 🛠️ Technologies Used  
- **Python** – Core programming language  
- **Jupyter Notebook** – Interactive data science and development environment  
- **NumPy** – Numerical operations and array handling  
- **Pandas** – Data loading, preprocessing, and manipulation  
- **Scikit-learn** – Linear regression modeling and train-test splitting  
- **Matplotlib** – Data visualization and plotting  
- **Seaborn** – Statistical visualizations  

---

## 📋 Features  
- **Data Cleaning**: Removal of missing values from the CERN dataset  
- **Feature Engineering**: Use of electron energy values as predictors  
- **Regression Modeling**: Training a linear regression model to estimate invariant mass  
- **Prediction Visualization**: Scatter plot comparing predicted vs actual mass values  
- **Model Evaluation**: Visual feedback to assess accuracy of regression results  

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.7+  
- pip (Python package manager)  
- Git  

### Installation  
Clone the repository:

```bash
git clone https://github.com/your-username/electron-collision-prediction.git
cd electron-collision-prediction
```

Download Jupyter Notebook:
```bash
pip install notebook
```

Launch the notebook:
```bash
python -m notebook
```

## 📊 Analysis Highlights
Key Insights
- Energy → Mass Relationship: Strong correlation observed between combined electron energy and resulting mass  
- Prediction Performance: Linear regression offers a baseline method for invariant mass estimation  
- Visual Verification: Scatter plot aligns predictions closely with actual test values

## 📁 Dataset
Source: [Kaggle](https://www.kaggle.com/datasets/fedesoriano/cern-electron-collision-data?resource=download)

## 👨‍🔬 Credits
Created by Louis Nguyen
