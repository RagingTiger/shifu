/bin/sh -c \
  "envsubst < \
  /etc/nginx/webserver.tmpl > \
  /etc/nginx/conf.d/webserver.conf && \
  nginx -g 'daemon off;' || \
  printf '\n---> CONFIG ERROR: Check settings printed below\n\n' && \
  cat /etc/nginx/conf.d/webserver.conf"
