from os import environ as env

BOT_TOKEN = env.get('BOT_TOKEN')

DB_NAME = env.get('POSTGRES_DB')
DB_HOST = env.get('POSTGRES_HOST')
DB_USER = env.get('POSTGRES_USER')
DB_PASSWORD = env.get('POSTGRES_PASSWORD')
DB_PROTOCOL = "postgresql+psycopg2"
DB_URL = f"{DB_PROTOCOL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
