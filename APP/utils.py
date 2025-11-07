import pandas as pd
import os

def load_dataset(subject):
    """Loads the dataset based on subject name."""
    mapping = {
        "History": "data/UPSC_History_MCQ_Dataset.csv",
        "Geography": "data/UPSC_Geography_MCQ_Dataset.csv",
        "Polity": "data/UPSC_Polity_MCQ_Dataset.csv",
        "Economy": "data/UPSC_Economy_MCQ_Dataset.csv",
        "Environment & Ecology": "data/UPSC_Environment_Ecology_MCQ_Dataset.csv",
        "Current Affairs": "data/UPSC_Current_Affairs_MCQ_Dataset.csv"
    }

    file_path = mapping.get(subject, "data/UPSC_History_MCQ_Dataset.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found for {subject}. Expected: {file_path}")

    return pd.read_csv(file_path)

def inputAns(user_input, df, x):
    """Maps user input (A/B/C/D) to actual text option."""
    if user_input == 'a':
        return df["Option1"][x]
    elif user_input == 'b':
        return df["Option2"][x]
    elif user_input == 'c':
        return df["Option3"][x]
    elif user_input == 'd':
        return df["Option4"][x]
    else:
        return None

def save_history(name, subject, correct, incorrect, accuracy, score, time_taken, history_file="history/quiz_history.csv"):
    """Saves quiz performance to CSV."""
    os.makedirs(os.path.dirname(history_file), exist_ok=True)

    player_data = {
        "Name": [name],
        "Subject": [subject],
        "Correct": [correct],
        "Incorrect": [incorrect],
        "Accuracy (%)": [round(accuracy, 2)],
        "Score": [score],
        "Time (s)": [time_taken]
    }

    df_player = pd.DataFrame(player_data)

    if os.path.exists(history_file):
        df_existing = pd.read_csv(history_file)
        df_combined = pd.concat([df_existing, df_player], ignore_index=True)
        df_combined.to_csv(history_file, index=False)
    else:
        df_player.to_csv(history_file, index=False)
