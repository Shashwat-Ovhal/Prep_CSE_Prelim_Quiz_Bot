# 🧠 QuizBot – AI-Powered UPSC GS Paper 1 MCQ Practice App

Welcome to **QuizBot**, a personalized quiz practice tool designed for **CSE Prelims (General Studies Paper 1)** aspirants.  
This open-source Python + Streamlit app allows users to select subjects, answer timed MCQs, and track their performance — all from a simple, command-line or web interface.
---
# Keywords : education, quiz-app, python, streamlit, ai, learning, UPSC, CSE Prelims, hands-on python, open-source.
---

## 📘 Features

✅ **6 Subject Categories**  
- History  
- Geography  
- Polity  
- Economy  
- Environment & Ecology  
- Current Affairs  

✅ **Smart Quiz System**
- Randomized question selection  
- User can quit anytime  
- Real-time scoring and feedback  

✅ **Performance Tracking**
- Saves user history (`quiz_history.csv`)  
- Accuracy, time, and score tracking  
- Displays Top 5 Leaderboard  

✅ **Ready for Streamlit Deployment**
- Deploy free on [Streamlit Cloud](https://streamlit.io/)  
- No database setup required  
- Uses simple CSV files for data storage  

---

## 📂 Project Structure

├── 📂 APP/
│ ├── main.py
│ ├── utils.py
│
├── 📂 Dataset_Generating/
│ ├── UPSC_Current_Affairs_MCQ_Dataset.ipynb
│ ├── UPSC_Economy_MCQ_Dataset.ipynb
│ ├── UPSC_Environment_Ecology_MCQ_Dataset.ipynb
│ ├── UPSC_Geography_MCQ_Dataset.ipynb
│ ├── UPSC_History_MCQ_Dataset.ipynb
│ ├── UPSC_Polity_MCQ_Dataset.ipynb
│
├── 📂 Question_bank_Datasets/
│ ├── UPSC_Current_Affairs_MCQ_Dataset.csv
│ ├── UPSC_Economy_MCQ_Dataset.csv
│ ├── UPSC_Environment_Ecology_MCQ_Dataset.csv
│ ├── UPSC_Geography_MCQ_Dataset.csv
│ ├── UPSC_History_MCQ_Dataset.csv
│ ├── UPSC_Polity_MCQ_Dataset.csv
│
├── 📂 Quiz_history&performance_logs/
│ ├── quiz_history.csv 
│
├── .gitignore
├── CONTRIBUTING.md
├── LICENCE
├── QuizBot.ipynb 
├── README.md 
├── Requirements.txt 


---

### 🧠 Folder Overview

| Folder | Description |
|---------|--------------|
| **APP/** | Contains main application scripts (`main.py`, `utils.py`) |
| **Dataset_Generating/** | Jupyter notebooks for creating and preparing UPSC subject datasets |
| **Question_bank_Datasets/** | Final structured CSV files used during quiz sessions |
| **Quiz_history&performance_logs/** | Stores quiz attempt logs and leaderboard data |
| **Root Files** | `QuizBot.ipynb` (prototype), `README.md` (docs), `Requirements.txt` (dependencies) |

---

✅ **Tip:**  
When deploying to Streamlit or running locally, make sure all dataset paths in `main.py` match this structure.


## 🧩 How It Works

1. User enters their name.  
2. Chooses one of six subjects.  
3. App loads the corresponding CSV dataset.  
4. Displays questions one by one (A/B/C/D options).  
5. User can type the answer or “Quit” anytime.  
6. Calculates score, accuracy, and displays leaderboard.  
7. Saves attempt in `quiz_history.csv`.

---

## 🧮 Scoring Logic

| Type | Points |
|------|---------|
| Correct | +2 |
| Incorrect | -0.666 |
| Unanswered | 0 |

**Accuracy (%) = (Correct / Total Attempted) × 100**

---

## 🧠 Example Output

Enter your name: Shashwat
Hello, Shashwat! Welcome to your personalized MCQ practicer.
Select Subject: 3 (Polity)
Let's start practicing Polity questions!

Q] Who is the head of the Union Executive of India?
A] Prime Minister
B] President
C] Chief Justice
D] Speaker

Enter your answer (A/B/C/D): b
✅ Correct Answer!

📊 QUIZ SUMMARY 📊
Subject: Polity
Correct: 4, Incorrect: 1
Accuracy: 80.00%
Time Taken: 58.24 seconds
🏁 Final Score: 6.67

---

## 🏆 Leaderboard Example

| Name | Subject | Score | Accuracy (%) | Time (s) |
|------|----------|--------|---------------|-----------|
| Shashwat | History | 8.00 | 90.00 | 72 |
| Aditi | Economy | 7.33 | 85.00 | 95 |
| Raj | Polity | 6.67 | 80.00 | 89 |

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to improve the datasets, UI, or add analytics:

1. Fork this repo  
2. Create a new branch (`feature/new-subject`)  
3. Submit a Pull Request  

---

## 🧾 License

This project is open-source and available under the **MIT License**.

---

## 💡 Credits

Developed by **Shashwat S Ovhal**  
B.Tech ECE (AI & ML), MIT-WPU, Pune  
Part of the initiative to build **Made-in-India educational and tech solutions 🇮🇳**

---

⭐ **If you found this helpful, give the repo a star!**


