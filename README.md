# Flask-auth-system

A simple auth system built with Python & Flask

#### Project setup

- Clone the repository
- [optional] Copy .flaskenv-example to .flaskenv and add port value for FLASK_RUN_PORT. if not sepecified, port will default to 5000
- Install packages `pip3 install -r requirements.txt`

#### Run app - Great for development

```sh
flask run --debug
```

#### Using docker compose

```sh
# Build image
docker compose build

# Run
docker compose up -d
```

Features

- Registration
- Login support
- Change password
- User information

To fix

- Docker compose not starting up, somehow app attribute isn't found
