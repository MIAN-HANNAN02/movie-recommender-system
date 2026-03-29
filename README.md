# 🎬 Movie Recommender System

A simple Movie Recommender System built using Python, Pandas, and Streamlit. This project suggests movies similar to the one selected by the user using content-based filtering.

---
### 🔴 Live Demo
Check out the live web app here: https://movie-recommender-system-ewpwg7vrtduqykrvyd8ein.streamlit.app/
---
## 🚀 Features

* Recommend movies based on similarity
* Fetch movie posters using TMDB API
* Clean and interactive UI with Streamlit
* Fast recommendations using precomputed similarity matrix

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* TMDB API

---

## 📁 Project Structure

```
movies-recommender-system/
│
├── app.py                # Streamlit app
├── setup.sh              # Shell script for automated environment setup
├── movies.pkl            # Movie dataset
├── similarity.pkl        # Similarity matrix
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```
## 🧠 How It Works

* Movies are converted into feature vectors
* Cosine similarity is calculated between movies
* When a user selects a movie, the system finds the most similar ones
* Posters are fetched dynamically using TMDB API

---



⭐ If you like this project, give it a star!
