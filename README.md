# Movie-Recommender
A machine-learning movie recommendation app that suggests similar films using feature similarity and TMDB data, with an interactive Streamlit interface for browsing titles and posters

## Features 
Content Based Movie Recommendation
- Recommends movies based on similarity of movie metadata such as genres, keywords, cast & overview.

Data Pre-Processing Pipeline
- Merges multiple datasets(movies & credits)
- Removes null values & duplicate records
- Extracts & cleans features like genres, cast, crew & keywords
- Converts text data into structured tags

Text vectoriztion & Similarity Modelling
- Uses CountVectorizer to convert text into numerical values
- Applies stemming using PorterStemmer to normalize words
- Calculates similarity using Cosine Similarity
- Generates top-5 similar movie recommendations

Model & Data Serialization
- Stores processed movie data using pickle
- Saves similarity matrix for fast recommendation lookup

Interactive Web Application(Streamlit)
- Simple and user-friendly UI
- Movie selection dropdown
- Displays recommended movies with posters
- Fetches posters from The Movie Database (TMDB) API

Robust API Handling
- Uses requests.Session() with retry mechanism
- Handles network errors and missing posters gracefully

Fast & Lightweight System
- No deep learning required
- Efficient for medium-sized datasets
- Suitable for learning, experimentation, and demonstrations

Modular & Scalable Codebase Made in Seperate Stages
- Data pre-processing
- Feature Engineering
- Model Building
- Web App Integration & Deployment

## Files
- app.py : Web Application Code
- train.ipynb : Data preprocessing and model building
- requirements.txt : Required Python libraries

## Dataset
The dataset used is the TMDB movie dataset from kaggle. Due to size limitations, datasets & trained model files(.pkl) are not uploaded.

## Tools & Technologies Used
- Kaggle : Getting the sample datasets
- VS Code : Building the training model
- Pycharm : Building the app
- Various python libraries like pickle, sklearn, nlk, streamlit, etc.

## How to Run the project
pip install -r
requirements.txt
python app.py
