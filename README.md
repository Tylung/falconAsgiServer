# Server Asgi hecho en Falcon

## Setup virtual enviroment

```sh
source .venv/bin/activate
```

## Install dependencies

```
pip install -r requirements.txt
```

## Setup server

```
$ uvicorn asgilook.asgi:app
```

## Setup server with reload

```
uvicorn --reload asgilook.asgi:app
```