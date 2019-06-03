## About
uWSGI subdirectory for Shifu (师父) website.

## Project Directory Structure
```
.
├── Dockerfile
├── README.md
├── config
│   └── uwsgi.tmpl
└── dynamic
    └── python
        ├── requirements.txt
        └── src
            ├── gmail.py
            ├── handler.py
            └── server.py

4 directories, 7 files
```

## Environment
**Warning**: you must set these variables when you run the container (or in your
docker-compose file if you are using `docker-compose`):

```
GMAIL_ACCOUNT=username@gmail.com
GMAIL_APP_PSSWD=secret_password
```

If you do not set these, none of the dynamic content will function (e.g. no
email services).
