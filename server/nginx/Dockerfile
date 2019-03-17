# Base NGINX image (with alpine 3.9)
FROM nginx:1.15.8-alpine

# Remove default.conf
RUN rm /etc/nginx/conf.d/default.conf

# Get static content
COPY static/ /usr/share/nginx/html/
COPY config/ /etc/nginx/

# setup ENV
ENV LISTEN_ADDR='80' \
    DOMAIN_NAME='_' \
    STATSERV_ROUTE='/' \
    DYNASERV_METHOD='uwsgi_pass' \
    DYNASERV_PARAMS='uwsgi_params' \
    DYNASERV_ROUTE='/dynamic/' \
    DYNASERV_ADDR='uwsgi' \
    DYNASERV_PORT='9090'

# entry command
CMD /bin/sh -c \
    "envsubst < \
     /etc/nginx/webserver.tmpl > \
     /etc/nginx/conf.d/webserver.conf && \
     nginx -g 'daemon off;' || \
     printf '\n---> CONFIG ERROR: Check settings printed below\n\n' && \
     cat /etc/nginx/conf.d/webserver.conf"
