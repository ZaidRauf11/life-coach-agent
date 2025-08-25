# 🧘 AI Life Coach Agent

The **AI Life Coach Agent** is a supportive system that listens to the user’s mood and responds with **uplifting, motivational, and practical suggestions**.
It’s built using **Agno**, **Groq LLMs**, and **Streamlit** to provide a smooth conversational interface.

---

## 🚀 Features

* 💭 Accepts user input about their **mood** (tired, stressed, happy, sad, etc.).
* 🤝 Provides **empathetic, warm, and supportive advice**.
* 🎯 Encourages positive actions like self-care, reflection, or celebration.
* 🖥️ Clean and interactive **Streamlit UI**.
* 🔑 Secure API key management with `.env`.

---

## 🛠 Requirements

Create a `requirements.txt` file with:

```txt
streamlit
agno
python-dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📂 Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/ZaidRauf/ai-life-coach-agent.git
   cd ai-life-coach-agent
   ```

2. Create a `.env` file and add your **GROQ API Key**:

   ```
   GROQ_API_KEY=your_api_key_here
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 🎯 How It Works

1. User types how they are **feeling today**.
   Example:

   * *"I feel tired"*
   * *"I am stressed"*
   * *"I’m really happy today"*
   * *"Feeling a bit sad"*

2. The **AI Life Coach Agent** understands the mood.

3. It responds with **short, motivational, and practical suggestions** in a warm tone.

---

## 💻 Interface

The app is built with **Streamlit**, providing:

* 💭 Input box for user mood.
* ⚡ "Get Suggestion" button to generate advice.
* 📄 Results section that displays motivational guidance.

Example output:

**Input:**

```txt
I feel stressed
```

**Output:**

```txt
Take a deep breath 🌿. Try a quick 5-minute break away from your screen—it can refresh your mind and lower stress levels. You’ve got this! 💪
```

---

## 📸 App Preview

<img width="961" height="741" alt="2" src="https://github.com/user-attachments/assets/60fefb8d-388d-4f54-8592-f3e573530427" />

---

✨ With **AI Life Coach Agent**, it’s like having a personal motivational coach by your side every day!
