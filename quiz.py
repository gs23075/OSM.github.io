import requests
import csv
import random

# GitHub Pages의 CSV URL
CSV_URL = "https://github.com/gs23075/osm.github.io/blob/main/vocab1.csv"

def fetch_csv_data(url):
    """
    Fetch the CSV data from the given URL.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    lines = response.text.splitlines()
    reader = csv.DictReader(lines)
    return list(reader)

def word_quiz(words):
    """
    Conduct a word quiz where the user guesses the word based on its meaning.
    """
    print("Welcome to the Word Quiz!")
    print("You will see a meaning, and you need to type the corresponding word.\n")
    
    score = 0
    random.shuffle(words)  # Shuffle the word list for randomness

    for entry in words:
        meaning = entry['meaning']
        word = entry['word']
        
        print(f"Meaning: {meaning}")
        user_input = input("Your answer: ").strip().lower()

        if user_input == word.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct word was: {word}\n")
    
    print(f"Quiz Over! You scored {score} out of {len(words)}.")

if __name__ == "__main__":
    try:
        words_data = fetch_csv_data(CSV_URL)
        word_quiz(words_data)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
