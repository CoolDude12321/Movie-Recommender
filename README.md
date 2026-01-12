# 🎬 Movie-Recommender

A machine-learning movie recommendation application that suggests similar films using content-based filtering and TMDB metadata, with an interactive Streamlit interface for browsing movie titles and posters.

---

## 📌 Project Overview
This project demonstrates how machine learning and natural language processing (NLP) techniques can be used to build a **content-based movie recommendation system**. By analyzing movie metadata such as genres, keywords, cast, crew, and plot overview, the system identifies similar movies and provides personalized recommendations. The application is lightweight, fast, and ideal for learning, experimentation, and portfolio demonstrations.

---

## ✨ Features

### 🎯 Content-Based Movie Recommendation
- Recommends movies based on similarity of movie metadata such as:
  - Genres
  - Keywords
  - Cast
  - Crew
  - Overview

---

### 🧹 Data Pre-Processing Pipeline
- Merges multiple datasets (movies & credits)
- Removes null values and duplicate records
- Extracts and cleans features such as:
  - Genres
  - Cast
  - Crew
  - Keywords
- Converts unstructured text data into structured **tags**

---

### 🧠 Text Vectorization & Similarity Modelling
- Uses **CountVectorizer** to convert text into numerical values
- Applies **PorterStemmer** to normalize words
- Calculates similarity using **Cosine Similarity**
- Generates **Top-5 similar movie recommendations**

---

### 💾 Model & Data Serialization
- Stores processed movie data using **pickle**
- Saves similarity matrix for fast recommendation lookup
- Eliminates the need for retraining during runtime

---

### 🌐 Interactive Web Application (Streamlit)
- Simple and user-friendly UI
- Movie selection dropdown
- Displays recommended movies with posters
- Fetches posters using **The Movie Database (TMDB) API**

---

### 🔐 Robust API Handling
- Uses `requests.Session()` with a retry mechanism
- Gracefully handles:
  - Network errors
  - API failures
  - Missing posters

---

### ⚡ Fast & Lightweight System
- No deep learning models required
- Efficient for medium-sized datasets
- Suitable for:
  - Learning
  - Experimentation
  - Academic projects
  - Demonstrations

---

### 🧩 Modular & Scalable Codebase
The project is built in clearly separated stages:
1. Data Pre-processing  
2. Feature Engineering  
3. Model Building  
4. Web App Integration & Deployment  

---

## 📁 Project Structure
- `app.py` – Streamlit web application code  
- `train.ipynb` – Data preprocessing and model building  
- `requirements.txt` – Required Python libraries  

---

## 📊 Dataset
- Dataset used: **TMDB Movie Dataset (Kaggle)**
- Due to size limitations:
  - Raw datasets
  - Trained model files (`.pkl`)
  
  are not uploaded to the repository.

---

## 🛠️ Tools & Technologies Used
- **Kaggle** – Dataset source  
- **VS Code** – Model development  
- **PyCharm** – Application development  
- **Python Libraries:**  
  pandas, numpy, scikit-learn, nltk, pickle, streamlit, requests  

---

## ▶️ How to Run the Project
- pip install -r requirements.txt
- python app.py

---  

## 🚀 Future Enhancements
- Add hybrid recommendation (content + collaborative filtering)
- Include user ratings and feedback
- Add advanced filters (genre, year, rating)
- Deploy on Streamlit Cloud or Hugging Face Spaces

---

## 👤 Author
- Prakhar Srivastava
- Aspiring Data Scientist & Business Analyst | Machine Learning, Deep Learning & Generative AI Enthusiast
