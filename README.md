# Python Utility & Interactive Applications
<img width="499" height="330" alt="WhatsApp Image 2026-07-22 at 3 29 27 PM" src="https://github.com/user-attachments/assets/352c0329-30d6-4b99-8656-b5ee3c398ba5" />
<img width="551" height="420" alt="WhatsApp Image 2026-07-22 at 3 32 21 PM" src="https://github.com/user-attachments/assets/c7708767-4110-4d7b-a57d-b58fa87dcb2d" />

A collection of lightweight Python applications including a GUI-based **Strong Password Generator** and a CLI-based **Terminal Quiz System**.

---

## 🛠️ Applications Included

### 1. 🔑 Strong Password Generator (`password_generator.py`)
A Tkinter GUI application that creates personalized, highly secure 16-character passwords based on the user's username.

#### **Features**
- **Personalized Complexity**: Integrates sanitized portions of the username while ensuring random uppercase, lowercase, numbers, and special symbols (`!@#$%^&*()-_=+?`).
- **One-Click Clipboard Copy**: Instantly copy the generated password to your clipboard.
- **Clean UI**: Minimalist visual layout built with native Python Tkinter styling[cite: 2, 4].

---

### 2. 📝 Terminal Quiz System (`quiz_system.py`)
A command-line interface (CLI) quiz application that dynamically loads multiple-choice questions from an external JSON file and provides a detailed post-game report card.

#### **Features**
- **Dynamic Question Loading**: Fetches questions, options, and correct answers directly from `questions.json`.
- **Input Validation**: Ensures valid choice inputs (`A`, `B`, `C`, or `D`).
- **Comprehensive Scorecard**: Outputs a tabular summary detailing selected answers, correct answers, total scores, percentages, and performance ratings[cite: 3, 4].

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your system.
* **Tkinter** (included by default with standard Python installations on Windows/macOS; Linux users may install it via `sudo apt-get install python3-tk`)[cite: 4].

---

## 📁 Project Setup

Organize your script files in your project workspace as follows[cite: 4]:

```text
├── password_generator.py
├── quiz_system.py
└── questions.json
