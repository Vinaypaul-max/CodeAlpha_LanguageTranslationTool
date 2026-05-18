# 🌐 Lingua — Language Translation Tool

> **CodeAlpha AI Internship | Task 1**

A clean, fast language translation web app built with Streamlit and deep-translator. Supports 100+ languages with auto-detection, character counting, and easy copy functionality.

---

## ✨ Features

- 🔍 **Auto language detection** — no need to manually specify source language
- 🌍 **100+ languages** supported via Google Translate (free, no API key)
- 📋 **Copy-ready output** — translated text shown in a selectable text area
- 🔢 **Character counter** — live count with 5000 char limit
- ⚡ **Instant UI** — built with Streamlit for zero-config deployment

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Streamlit` | Web UI framework |
| `deep-translator` | Google Translate wrapper (free, no API key) |
| `Python 3.8+` | Core language |

---

## 🚀 Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
CodeAlpha_LanguageTranslationTool/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 📸 Usage

1. Select **source language** (or leave as Auto Detect)
2. Select **target language**
3. Enter your text in the input box
4. Click **Translate →**
5. Copy the result from the output box

---

## 📌 Notes

- Requires an active internet connection (uses Google Translate via deep-translator)
- Free to use, no API key required
- Handles up to 5000 characters per translation

---

## 👤 Author

Built as part of the **CodeAlpha AI Internship** program.

---

## 🌐 Live Demo
👉 [Try it here](https://languagetranslationtool.streamlit.app/)
