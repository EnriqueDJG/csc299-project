# AI-Powered Personal Knowledge & Task Management System (PKMS)

## 📌 Overview

This project is a terminal-based **AI-powered Personal Knowledge Management System (PKMS)** that allows users to create, manage, and interact with notes and tasks using both traditional commands and an integrated OpenAI agent.

The system was built in Python and designed to run portably on Windows, macOS, and Linux. It uses JSON for persistent storage and integrates the OpenAI API to provide intelligent features such as note summarization and task generation.

---

## ✨ Features

### 🧠 Personal Knowledge Management

* Create, list, search, and delete notes
* Tag-based organization
* Persistent JSON storage

### ✅ Task Management

* Add, list, complete, and delete tasks
* Due date tracking
* Completion status management

### 🤖 AI Agent Integration

Powered by OpenAI API:

* Summarize notes into concise explanations
* Generate actionable tasks from note content

### 💬 Terminal Chat Interface

Interact entirely through a command-line interface using intuitive commands.

---

## 🛠️ Technologies Used

* Python 3.10+
* OpenAI API
* JSON file storage
* Git & GitHub
* python-dotenv for secure API handling

---

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd pkms_Project
```

### 2. Install dependencies

```bash
python -m pip install openai python-dotenv
```

### 3. Create .env file

In the project root, create a file named `.env`:

```
OPENAI_API_KEY=sk-your-api-key-here
```

### 4. Run the application

```bash
python main.py
```

---

## 💻 Available Commands

### NOTES

```
note create
note list
note search <keyword>
note delete <id>
```

### TASKS

```
task add
task list
task done <id>
task delete <id>
```

### AI

```
ai summarize <note_id>
ai suggest <note_id>
```

### SYSTEM

```
help
exit
```

---

## 📸 Example Usage

```
>> note create
Title: Study Plan
Content: Review chapters 1-4 and prepare for final exam.
Tags: school,study

>> ai summarize <note_id>
🤖 AI Summary:
Review chapters 1-4 and prepare effectively for the final exam.
```

---

## 📂 Project Structure

```
pkms_Project/
│ main.py
│ .gitignore
├── ai/
├── chat/
├── notes/
├── tasks/
├── storage/
```

---

## 🎓 Academic Compliance

This project fulfills all assignment requirements:

* ✔ Personal Knowledge Management System
* ✔ Task Management System
* ✔ Terminal Chat Interface
* ✔ AI Agents (via OpenAI API)
* ✔ Python Cross-platform Support
* ✔ JSON State Storage

---

## 🏁 Final Notes

This system was developed as a final prototype demonstrating the practical use of AI-coding assistants in software development workflows. It reflects real-world practices in security, modular design, and AI integration.

Feel free to expand the system with additional features such as reminders, analytics, or GUI interfaces.

---

### 👨‍💻 Author

Enrique Garcia

### 📅 Version

v1.0 - Final Prototype

---

⭐ If you find this project useful, feel free to star the repository!
