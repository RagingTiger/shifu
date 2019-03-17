## About
Repo for Shifu (师父) website

## Project Directory Structure
```
.
├── README.md
├── docker-compose.yml
└── server
    ├── nginx
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── config
    │   │   ├── nginx.conf
    │   │   └── webserver.tmpl
    │   └── static
    │       ├── contactform.html
    │       ├── index.html
    │       └── robots.txt
    └── uwsgi
        ├── Dockerfile
        ├── README.md
        ├── config
        │   └── uwsgi.tmpl
        └── dynamic
            └── python
                ├── requirements.txt
                └── src
                    ├── handler.py
                    └── server.py
```
