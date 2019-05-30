## About
Repo for Shifu (师父) website

## Project Directory Structure
```
.
├── docker-compose.yml
├── README.md
├── server
│   ├── nginx
│   │   ├── config
│   │   │   ├── nginx.conf
│   │   │   └── webserver.tmpl
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── static
│   │       ├── assessment.html
│   │       ├── disclaimer.html
│   │       ├── index.html
│   │       ├── privacy_policy.html
│   │       ├── robots.txt
│   │       ├── services.html
│   │       ├── styles
│   │       │   └── main.css
│   │       ├── submitted.html
│   │       └── terms_of_service.html
│   └── uwsgi
│       ├── config
│       │   └── uwsgi.tmpl
│       ├── Dockerfile
│       ├── dynamic
│       │   └── python
│       │       ├── requirements.txt
│       │       └── src
│       │           ├── gmail.py
│       │           ├── handler.py
│       │           └── server.py
│       └── README.md
└── test
    └── test_request.sh

11 directories, 23 files
```
