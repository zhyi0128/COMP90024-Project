FROM python:3.7.2-stretch

# ENV http_proxy http://wwwproxy.unimelb.edu.au:8000
# ENV https_proxy http://wwwproxy.unimelb.edu.au:8000
ENV PYTHONUNBUFFERED 1
#Set the working directory to /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]