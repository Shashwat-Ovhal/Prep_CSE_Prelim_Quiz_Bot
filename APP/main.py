import pandas as pd
import numpy as np
import time
import os
from utils import load_dataset, inputAns, save_history


name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to your personalized MCQ practicer")

options = {
    1: "History",
    2: "Geography",
    3: "Polity",
    4: "Economy",
    5: "Environment & Ecology",
    6: "Current Affairs"
}

choice = int(input(
    "Select Subject to practice by entering the sequence no. for following options:\n"
    "1. History\n2. Geography\n3. Polity\n4. Economy\n5. Environment & Ecology\n6. Current Affairs\n"
))
subject = options.get(choice, "History")
print(f"Let's start practicing {subject} questions, {name}!")
print("Press 'Exits' to stop the test and see your score at any time.\n")


df = load_dataset(subject)


correct = 0
incorrect = 0
num_questions = 5  # change as needed

print(f"\nStarting quiz with {num_questions} questions...")
start_time = time.time()   # 🕒 start timer

for i in range(num_questions):
    x = np.random.choice(df.index)  # allows repetition
    print(f"\nQ] {df['Question'][x]}")
    print(f"A] {df['Option1'][x]}")
    print(f"B] {df['Option2'][x]}")
    print(f"C] {df['Option3'][x]}")
    print(f"D] {df['Option4'][x]}")
    print("enter 'Quit' to Quit the quiz")

    user_input = input("Enter your answer (A/B/C/D): ").lower().strip()
    if user_input == 'quit':
        break

    user_option = inputAns(user_input, df, x)
    if user_option is None:
        print("Invalid Option! Please enter a, b, c, or d.")
        continue

    correct_option = df["CorrectOption"][x].strip()
    if user_option.strip().lower() == correct_option.lower():
        print("Correct Answer!")
        correct += 1
    else:
        print(f"Incorrect Answer! The correct answer is: {correct_option}")
        incorrect += 1

end_time = time.time()     # 🕒 stop timer
time_taken = round(end_time - start_time, 2)


score = int((correct * 2) - (incorrect * 0.666))
total = correct + incorrect
accuracy = (correct / total) * 100 if total else 0

print("\n📊 QUIZ SUMMARY 📊")
print(f"Subject: {subject}")
print(f"Correct: {correct}, Incorrect: {incorrect}")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Total Time Taken: {time_taken} seconds")
print(f"🏁 Final Score: {score}")


save_history(name, subject, correct, incorrect, accuracy, score, time_taken)
print(f"\n✅ Your performance has been saved successfully.")


history_file = "history/quiz_history.csv"
df_leaderboard = pd.read_csv(history_file)
print("\n🏆 LEADERBOARD (Top 5 by Score) 🏆")
leaderboard = df_leaderboard.sort_values(by="Score", ascending=False).head(5)
print(leaderboard[["Name", "Subject", "Score", "Accuracy (%)", "Time (s)"]].to_string(index=False))
