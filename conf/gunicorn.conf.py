from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
command = '__INSTALL_DIR__/venv/bin/gunicorn'
bind = '127.0.0.1:__PORT__'
workers = 3
user = '__APP__'
