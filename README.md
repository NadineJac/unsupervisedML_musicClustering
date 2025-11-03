![Python](https://img.shields.io/badge/Python-3.13.7-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)

# Clustering Songs into Playlists Based on Audio Features

## 🎯 Project Overview
This project explores how **k-means clustering** can be used to automatically group songs into playlists based on their **audio features**, reducing manual workload for music experts in a fictional music company.  

The goal is to identify meaningful clusters that capture distinct moods or styles, providing a foundation for automated playlist generation.


## 📊 Dataset & Sources
- **Data source:** Spotify song dataset provided by *WBS Coding School* – [get data here](https://drive.google.com/uc?export=download&id=1oYQSNxfvw6kFr6-N9rKLRAnLXlp0osEt)  
- **Dataset size:** 5,000 records  
- **Key features:** Audio features such as *danceability, energy, loudness, mode, tempo*, etc.  
- **Preprocessing:**  
  - Selected features with high variance and low-to-moderate correlation to ensure diverse representation.  
  - Standard scaling was applied to remove unit bias before clustering.  
  - Optimal number of clusters (52) determined using **inertia** and **silhouette** scores across 20–100 clusters.  



## 🚀 Key Findings & Results
- **52 playlists** were created, each containing on average **100 songs** (range: 21–258).  
- Most playlists represented distinct moods or energy levels (e.g., “calm acoustic,” “energetic dance”), though a few contained outlier songs.  
- Visualizations confirmed well-separated clusters in feature space and strong internal consistency for most groups.  


## 🛠️ Technologies Used
- **Programming Language:** Python  
- **Key Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`  
- **Tools:** Jupyter Notebook  

---

## 📁 Project Structure
```
data/
├── songs_data.csv
images/ # Generated plots and figures
notebooks/ # Jupyter notebooks
│ ├── 1_exploreMusic.ipynb
│ ├── 2_preprocessFeatures.ipynb
│ └── 3_cluster_send2spotify.ipynb
requirements.txt
LICENSE
README.md
```

- `data/`: Contains the raw and preprocessed songs data.  
- `images/`: Stores visualizations created during analysis.  
- `notebooks/`: Jupyter notebooks documenting each project step.  
- `requirements.txt`: Python dependencies.  



## 📈 Visualizations
- Inertia (Elbow method) for 20–100 clusters  
- Silhouette scores for 20–100 clusters  
- Correlation matrix of chosen features  
- Feature distributions per cluster  
- Number of songs per playlist  
- PCA projection of clustered songs  



## 🔗 How to Use This Project
**Setup:**
1. Clone this repository  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies
    ```
    pip install -r requirements.txt
    ```


3. Run the analysis notebooks in order:

    - Start with [1_exploreMusic.ipynb](notebooks\1_exploreMusic.ipynb)

    - Continue with [2_optimizeClustering_5000songs.ipynb](notebooks\2_optimizeClustering_5000songs.ipynb)

    - Reproduce clustering and export results via [3_cluster_send2spotify.ipynb](notebooks\3_cluster_send2spotify.ipynb)

All generated plots and results will be saved in the images/ folder.

## 🚀 Future Work

* Integrate **personalized recommendations** using user listening histories.

* Add **AI-generated playlist titles, descriptions, and cover art**.

* Develop an **interactive dashboard** to adjust features and visualize cluster outcomes in real time.


## 📜 License

This project is released under the [MIT License](LICENSE).

