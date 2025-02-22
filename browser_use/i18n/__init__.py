from pathlib import Path
import json
import os

TRANSLATIONS = {}
SUPPORTED_LANGUAGES = ['en', 'de', 'ru', 'tr']
DEFAULT_LANGUAGE = 'en'

def load_translations():
    i18n_dir = Path(__file__).parent
    for lang in SUPPORTED_LANGUAGES:
        translation_file = i18n_dir / f'{lang}.json'
        if translation_file.exists():
            with open(translation_file, 'r', encoding='utf-8') as f:
                TRANSLATIONS[lang] = json.load(f)

def get_text(key, lang=DEFAULT_LANGUAGE):
    if lang not in TRANSLATIONS:
        lang = DEFAULT_LANGUAGE
    return TRANSLATIONS[lang].get(key, TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key))

# Load translations when module is imported
load_translations()
