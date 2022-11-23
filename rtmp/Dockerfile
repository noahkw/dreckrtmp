FROM tiangolo/nginx-rtmp:latest-2022-11-09

COPY nginx.conf.template /etc/nginx/nginx.conf.template
# Install dependencies
RUN apt-get update && apt-get install -y gettext-base
