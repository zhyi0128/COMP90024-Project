FROM nginx

ENV http_proxy http://wwwproxy.unimelb.edu.au:8000
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000

RUN rm /etc/nginx/conf.d/default.conf

COPY dist/ /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/