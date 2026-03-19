📌 AI-Based Student Feedback ERP System

An intelligent web-based ERP system that collects, analyzes, and visualizes student feedback using Machine Learning (LSTM-based sentiment analysis).
This project helps academic institutions gain actionable insights from qualitative student feedback instead of manually reviewing raw responses.

🚀 Project Overview

Traditional student feedback systems collect data but fail to extract meaningful insights.
This project solves that problem by integrating Natural Language Processing (NLP) with a Flask-based web application to automatically analyze student feedback and present results through an admin dashboard.

🎯 Key Features

👨‍🎓 Student Interface

--Simple and user-friendly feedback submission form

--Open-ended feedback text input

--Seamless navigation with home and resubmission options

🧑‍💼 Management / Admin Interface

--Dashboard to view all collected feedback

--Sentiment analysis using trained LSTM model

--Bar-graph visualization of feedback distribution

--Identification of sector/department with maximum feedback

--CSV-based feedback storage for simplicity

🧠 Machine Learning Details

Model Used: LSTM (Long Short-Term Memory)

Task: Text Sentiment Analysis

Preprocessing:

Tokenization

Padding

Model Files:

--best_lstm_model.keras

--tokenizer.pkl

Output:

Classified sentiment used for analytical insights

🛠️ Tech Stack
Layer	Technology
Frontend	HTML, CSS, Bootstrap
Backend	Python, Flask
Machine Learning	TensorFlow, Keras (LSTM)
Data Storage	CSV
Visualization	Matplotlib / Chart.js
Deployment	Render
📂 Project Structure
AI-student-feedback-system/
│
├── app.py
├── best_lstm_model.keras
├── tokenizer.pkl
├── feedbacks.csv
├── requirements.txt
├── templates/
├── static/
└── README.md

▶️ How to Run Locally

Clone the repository

git clone https://github.com/Deepika0506/AI-student-feedback-system-.git


Navigate to the project directory

cd AI-student-feedback-system-


Install dependencies

pip install -r requirements.txt


Run the application

python app.py


Open in browser

http://127.0.0.1:5000/

🌐 Live Deployment

🔗 Live App:
https://ai-student-feedback-system.onrender.com/

📈 Future Enhancements

Role-based authentication (Student / Admin)

Database integration (MySQL / PostgreSQL)

Advanced NLP models (BERT / Transformers)

Downloadable reports (PDF / Excel)

UI/UX improvements with animations

⭐ If you find this project useful, feel free to star the repository

README.md

