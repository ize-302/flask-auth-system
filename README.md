# Flask-auth-system

A simple auth system built with Python & Flask

#### Project setup

- Clone the repository
- [optional] Copy .flaskenv-example to .flaskenv and add port value for FLASK_RUN_PORT. if not sepecified, port will default to 5000
- Install packages `pip3 install -r requirements.txt`

#### Run app - Great for development

```sh
flask run
```

#### Using docker

```sh
# Build image
docker build -t flask-auth-system .

# Run
docker compose up -d
```
