# 🚀 SolveX AI: Intelligent Math & Reasoning Agent

SolveX AI is an AI-powered multi-tool reasoning agent that can solve mathematical problems, logical reasoning questions, and fetch factual information using integrated tools. It leverages the ReAct (Reasoning + Acting) framework to dynamically decide which tool to use and provides step-by-step explanations.

---

## 🧠 Features

- 🧮 Solve mathematical expressions using a custom calculator tool
- 🤔 Handle logical and reasoning-based questions
- 🌐 Fetch real-time information using Wikipedia
- 🔁 Uses ReAct Agent (Reason + Action loop)
- 💬 Step-by-step explanation for every solution
- ⚡ Powered by Groq LLM (fast inference)
- 🎯 Streamlit-based interactive UI

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq API (LLM)**
- **Streamlit**
- **numexpr (for math evaluation)**
- **Wikipedia API**

---

## ⚙️ How It Works

1. User inputs a question
2. Agent analyzes the problem
3. Chooses the appropriate tool:
   - Calculator → for math problems
   - Chain Tool → for reasoning
   - Wikipedia Tool → for factual queries
4. Executes tool
5. Returns step-by-step final answer

---

## 🧩 Tools Used

### 🔢 Calculator Tool
- Evaluates mathematical expressions using `numexpr`
- Ensures accurate and deterministic results

### 🧠 Reasoning Tool (LLM Chain)
- Handles logic-based and descriptive problems

### 🌍 Wikipedia Tool
- Fetches factual and general knowledge data

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/solvex-ai.git
cd solvex-ai

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Add Groq API Key
Get API key from: https://console.groq.com/
Enter it in the Streamlit sidebar

### 4️⃣ Run the App
streamlit run app.py

💡 Example Use Cases
Solve equations: x + 5 = 15
Arithmetic: 37593 * 67
Logical problems: puzzles, reasoning
General knowledge queries

🖥️ UI Preview
Chat-based interface
Real-time response generation
Step-by-step reasoning display
