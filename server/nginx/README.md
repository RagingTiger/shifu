## About
NGINX subdirectory for Shifu (师父) website.

## Project Directory Structure
```
.
├── config
│   ├── nginx.conf
│   └── webserver.tmpl
├── Dockerfile
├── README.md
└── static
    ├── assessment.html
    ├── disclaimer.html
    ├── index.html
    ├── privacy_policy.html
    ├── robots.txt
    ├── services.html
    ├── styles
    │   └── main.css
    ├── submitted.html
    └── terms_of_service.html

3 directories, 13 files
```

## Environment
**Warning**: you must set these variables when you run the container (or in your
docker-compose file if you are using `docker-compose`):

```
DYNASERV_ADDR=your.uwsgi.address.local
```

Do not literally set the address to `your.uwsgi.address.local` but rather the
address of the host that the uWSGI server is running on.

If you do not set these, none of the dynamic content will function (e.g. no
email services).
