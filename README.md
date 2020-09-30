# Digitalbeti

## Translations
In order to make a Django project translatable, you have to add a minimal number of hooks to your Python code and templates.
These hooks are called translation strings. 

### Instructions
1. Add the locale middleware in between the session middleware and the common middleware in the settings.py file.
2. Add a locale path where language.po file will be stored and create a directory for the same.
3. Load the i18n tag in the template file where the translation is required.
4. Place the text under trans tag in the template file.
5. Run python3 manage.py makemessages -l 'language_code'
6. Open the .po file in the directory under locale_paths and place the translation for the message id.
7. Run python3 manage.py compilemessages 
8. Enable the language in language_code in settings.py and it will be done.
