FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl/selfsigned.crt /etc/ssl/certs/selfsigned.crt
COPY ssl/selfsigned.key /etc/ssl/private/selfsigned.key
COPY ./frontend /usr/share/nginx/html