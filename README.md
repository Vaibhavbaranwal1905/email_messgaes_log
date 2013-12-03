In your settings.py file put these lines of code.

Add email_messages_log in your INSTALLED_APP

# For email_messages_log app starts
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'  #only for stagging and local
EMAIL_FILE_PATH = 'email_messages_log/temp_messages'  #only for stagging and local
KEEP_FILES_COUNT = 50
LIST_EMAIL_MESSAGES_PER_PAGE = 20
# For email_messages_log app ends
