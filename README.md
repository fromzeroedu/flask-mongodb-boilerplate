# Flask MongoDB Boilerplate

![Code Check](https://github.com/fromzeroedu/flask-mongodb-boilerplate/workflows/Code%20Checks/badge.svg)

This is a boilerplate for a MongoDB Flask app that can run as a local poetry-based or Docker application. Requires `python 3.7` or higher.

## Using Docker

- Make sure your folder is being shared within Docker client (Preferences > Resources > File Sharing)
- Run `docker-compose up --build`. If there's a timeout error, you can restart the Flask container.
- Head over to `http://localhost:5000` on your browser
- Run tests by doing `docker-compose run --rm web poetry run pytest -s`

## Production

- Use Hypercorn `hypercorn --bind 0.0.0.0:$PORT --reload wsgi:app`

## Codespaces

- TODO
