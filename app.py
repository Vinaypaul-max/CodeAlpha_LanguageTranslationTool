import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }
            
    header[data-testid="stHeader"] {
    background: none;
    }
    [data-testid="stDecoration"] {
        display: none;
    }

    .main-title {
        font-family: 'DM Serif Display', serif;
        font-size: 2.8rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 1rem;
        margin-bottom: 2.5rem;
        font-weight: 300;
    }

    .lang-badge {
        display: inline-block;
        background: #ecfdf5;
        color: #0d9488;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    .result-box {
        border-left: 4px solid #0d9488;
        background: #ecfdf5;
        border-radius: 0 12px 12px 0;
        padding: 1.2rem 1.5rem;
        font-size: 1.1rem;
        color: #1a1a2e;
        line-height: 1.7;
        margin-top: 1rem;
    }

    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1.5px solid #e2e8f0 !important;
        font-size: 1rem !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    .stTextArea textarea:focus {
        border-color: #0d9488 !important;
        box-shadow: 0 0 0 3px rgba(59, 79, 216, 0.1) !important;
    }

    .stSelectbox > div > div {
        border-radius: 10px !important;
        border: 1.5px solid #e2e8f0 !important;
    }

    .stButton > button {
        background: #064e3b !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        width: 100% !important;
        transition: background 0.2s ease !important;
    }

    .stButton > button:hover {
        background: #0d9488 !important;
        color: #0d9488
    }

    .char-count {
        font-size: 0.78rem;
        color: #9ca3af;
        text-align: right;
        margin-top: -0.8rem;
        margin-bottom: 1rem;
    }

    .section-label {
        font-size: 0.82rem;
        font-weight: 500;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.4rem;
    }

    .divider {
        border: none;
        border-top: 1px solid #f0f0f0;
        margin: 2rem 0;
    }

    .copy-note {
        font-size: 0.78rem;
        color: #9ca3af;
        margin-top: 0.5rem;
        text-align: right;
    }
            
    .stApp {
    background-color:  #228B22;
    }
</style>
""", unsafe_allow_html=True)

LANGUAGES = {
    "Auto Detect": "auto",
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am",
    "Arabic": "ar", "Armenian": "hy", "Azerbaijani": "az",
    "Basque": "eu", "Belarusian": "be", "Bengali": "bn",
    "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
    "Cebuano": "ceb", "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW", "Corsican": "co",
    "Croatian": "hr", "Czech": "cs", "Danish": "da",
    "Dutch": "nl", "English": "en", "Esperanto": "eo",
    "Estonian": "et", "Finnish": "fi", "French": "fr",
    "Frisian": "fy", "Galician": "gl", "Georgian": "ka",
    "German": "de", "Greek": "el", "Gujarati": "gu",
    "Haitian Creole": "ht", "Hausa": "ha", "Hawaiian": "haw",
    "Hebrew": "he", "Hindi": "hi", "Hmong": "hmn",
    "Hungarian": "hu", "Icelandic": "is", "Igbo": "ig",
    "Indonesian": "id", "Irish": "ga", "Italian": "it",
    "Japanese": "ja", "Javanese": "jv", "Kannada": "kn",
    "Kazakh": "kk", "Khmer": "km", "Korean": "ko",
    "Kurdish": "ku", "Kyrgyz": "ky", "Lao": "lo",
    "Latin": "la", "Latvian": "lv", "Lithuanian": "lt",
    "Luxembourgish": "lb", "Macedonian": "mk", "Malagasy": "mg",
    "Malay": "ms", "Malayalam": "ml", "Maltese": "mt",
    "Maori": "mi", "Marathi": "mr", "Mongolian": "mn",
    "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no",
    "Nyanja (Chichewa)": "ny", "Odia (Oriya)": "or",
    "Pashto": "ps", "Persian": "fa", "Polish": "pl",
    "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro",
    "Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd",
    "Serbian": "sr", "Sesotho": "st", "Shona": "sn",
    "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk",
    "Slovenian": "sl", "Somali": "so", "Spanish": "es",
    "Sundanese": "su", "Swahili": "sw", "Swedish": "sv",
    "Tagalog (Filipino)": "tl", "Tajik": "tg", "Tamil": "ta",
    "Tatar": "tt", "Telugu": "te", "Thai": "th",
    "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk",
    "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz",
    "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh",
    "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu",
}

SOURCE_LANGS = list(LANGUAGES.keys())
TARGET_LANGS = [k for k in LANGUAGES.keys() if k != "Auto Detect"]

st.markdown('<div class="main-title">🌍 Lingua</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate instantly across 100+ languages</div>', unsafe_allow_html=True)

col1, col_arrow, col2 = st.columns([5, 1, 5])

with col1:
    st.markdown('<div class="section-label">From</div>', unsafe_allow_html=True)
    source_lang_name = st.selectbox(
        "Source Language",
        SOURCE_LANGS,
        index=SOURCE_LANGS.index("Auto Detect"),
        label_visibility="collapsed"
    )

with col_arrow:
    st.markdown("<div style='text-align:center; padding-top: 2.1rem; font-size: 1.4rem; color: #9ca3af;'>→</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-label">To</div>', unsafe_allow_html=True)
    default_target = "Hindi" if "Hindi" in TARGET_LANGS else TARGET_LANGS[0]
    target_lang_name = st.selectbox(
        "Target Language",
        TARGET_LANGS,
        index=TARGET_LANGS.index(default_target),
        label_visibility="collapsed"
    )

st.markdown('<div class="section-label" style="margin-top:1.2rem;">Text to translate</div>', unsafe_allow_html=True)
input_text = st.text_area(
    "Enter text",
    placeholder="Type or paste your text here...",
    height=160,
    max_chars=5000,
    label_visibility="collapsed"
)

char_count = len(input_text) if input_text else 0
st.markdown(f'<div class="char-count">{char_count} / 5000 characters</div>', unsafe_allow_html=True)

translate_btn = st.button("Translate →", use_container_width=True)

if translate_btn:
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        source_code = LANGUAGES[source_lang_name]
        target_code = LANGUAGES[target_lang_name]

        if source_code == target_code and source_code != "auto":
            st.info("Source and target languages are the same.")
        else:
            with st.spinner("Translating..."):
                try:
                    translator = GoogleTranslator(source=source_code, target=target_code)
                    translated = translator.translate(input_text.strip())

                    st.markdown('<hr class="divider">', unsafe_allow_html=True)
                    st.markdown(
                        f'<span class="lang-badge">→ {target_lang_name}</span>',
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f'<div class="result-box">{translated}</div>',
                        unsafe_allow_html=True
                    )

                    st.text_area(
                        "Copy translated text",
                        value=translated,
                        height=100,
                        key="copy_area",
                        help="Select all and copy (Ctrl+A, Ctrl+C)"
                    )
                    st.markdown(
                        '<div class="copy-note">↑ Select all text above to copy</div>',
                        unsafe_allow_html=True
                    )

                except LanguageNotSupportedException:
                    st.error("This language pair is not supported. Try a different combination.")
                except Exception as e:
                    st.error(f"Translation failed: {str(e)}\n\nCheck your internet connection and try again.")

st.markdown("""
<hr class="divider">
<div style="text-align:center; color:#d1d5db; font-size:0.78rem; padding-bottom: 1rem;">
    Lingua — Built with deep-translator & Streamlit &nbsp;·&nbsp; CodeAlpha AI Internship
</div>
""", unsafe_allow_html=True)
