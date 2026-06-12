# US State Quiz Game

A fun and interactive Python-based quiz game that tests users' knowledge of the 50 states of the United States.

The project uses Python Turtle Graphics for visualization and Pandas for handling state coordinate data.

---

## Features

* Interactive state guessing game
* Displays correctly guessed states on the US map
* Tracks score in real-time
* Uses CSV data for state coordinates
* Built using Python Turtle Graphics

---

## Technologies Used

* Python
* Turtle Graphics
* Pandas

---

## Project Structure

```text
us-state-quiz/
│
├── main.py
├── 50_states.csv
├── img.gif
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

1. The US map is displayed using a GIF image.
2. The user enters the name of a US state.
3. If the answer is correct:

   * The state name appears at its corresponding location on the map.
   * The score is updated.
4. The game continues until all 50 states are guessed.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/us-state-quiz.git
```

Move into the project folder:

```bash
cd us-state-quiz
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Sample Gameplay

```text
Guess The State Game
Enter Any State Name:
```

```text
12/50 Are Correct
Enter another State Name:
```

---

## Future Improvements

* Add a timer
* High score tracking
* Export missed states to CSV
* Difficulty levels

---

## Learning Outcomes

This project demonstrates:

* File handling using Pandas
* CSV data processing
* Turtle Graphics
* Event-driven programming
* GUI development with Python

---

## Author

Yashwanth Lanka

Computer Science Engineering Student
Python | Data Structures | Full Stack Development
