import os

PROJECT_NAME = "fastapi sqlalchemy pytest example"
VERSION = "0.0.1"
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_PREFIX = "/api"
SQLALCHEMY_DATABASE_URL: str = os.getenv('DATABASE_URI', f"sqlite:///{BASE_DIR}/foo.db")
DEBUG=True