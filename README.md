# Flask MongoDB Boilerplate

![Code Check](https://github.com/fromzeroedu/flask-mongodb-boilerplate/workflows/Code%20Checks/badge.svg)

This is a boilerplate for a MongoDB Flask app that can run as a local poetry-based or Docker application. Requires `python 3.7` or higher.

## Local Development

### Install MongoDB on Mac (TODO)

- Install using HomeBrew: `brew install postgresql`
  - If you want Postgres to launch automatically whenever you power on your Mac, you can do: `brew services start postgresql`. Preferably, you can start it manually when you need it by doing `pg_ctl -D /usr/local/var/postgres start` and stopping with `pg_ctl -D /usr/local/var/postgres stop`.
  - To login to Postgres using: `psql postgres`

### Install MongoDB on Windows (TODO)

- Install using Chocolatey: `choco install postgresql --params '/Password:rootpass'`
- To login to Postgres use: `psql postgres postgres`

### Install Poetry

- Install Poetry if you don't have it using `pip install poetry`
    - On WSL install using the get-poetry route. For example, on Ubuntu, do `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -`. 
- Install the packages: `poetry install`
- To open a Quart shell, just do `poetry run quart shell`

### Running the application

- To run the application do: `poetry run quart run`
- Open `http://localhost:5000` on your browser

### Run Tests

- Run tests by doing `poetry run pytest`

## Using Docker

- Make sure your folder is being shared within Docker client (Preferences > Resources > File Sharing)
- Run `docker-compose up --build`. If there's a timeout error, you can restart the Flask container.
- Head over to `http://localhost:5000` on your browser
- Run tests by doing `docker-compose run --rm web poetry run pytest -s`

## Production

- Use Hypercorn `hypercorn --bind 0.0.0.0:$PORT --reload wsgi:app`

## Codespaces

- Start the Codespace
- First time:
  - Run `poetry install`
  - Restart VSCode for changes to be applied
  - After restart:
    - Make sure to select the poetry Python interpreter for VSCode
- To run the application: `poetry run quart run`
  - The codespace will give you a private URL for your application
- To connect to Postgres Database: `psql -h localhost -Uapp_user postgres`
