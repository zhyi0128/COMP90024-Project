def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return f'{engine}+{driver}://{user}:{password}@{host}:{port}/{name}'


class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "heqiwuai11",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "sakila"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5984,
        "NAME": "COMP90024"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5984,
        "NAME": "COMP90024"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductionConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5984,
        "NAME": "COMP90024"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "development": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
    "default": DevelopConfig
}
