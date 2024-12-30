from db import migrate
from app import app


if __name__ == "__main__":
    migrate()
    app.run(host="localhost", port=8080)
