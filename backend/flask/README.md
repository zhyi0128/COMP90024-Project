# How to use without docker

```bash
pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=manage
flask run
```
```
├── App
│   ├── __init__.py
│   ├── analysis.py
│   ├── ext.py
│   ├── settings.py
│   ├── views
│   └── views.py
├── Dockerfile
├── README.md
├── app.ini
├── manage.py
└── requirements.txt
```

In the analysis.py file, adding flask-restful api class.

In the views.py file, adding url to these api.