import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

def getMongoClient(exchange, db_name):
    if exchange == "local":
        db_host = '127.0.0.1'
        db_user = ''
        db_pass = ''
        db_params = 'retryWrites=true&w=majority'
        db_is_srv = False
        db_port = 27017
    elif exchange == "target":
        db_host = os.environ.get("TARGET_DB_HOST")
        db_port = os.environ.get("TARGET_DB_PORT")
        db_user = os.environ.get("TARGET_DB_USER")
        db_pass = os.environ.get("TARGET_DB_PASS")
        db_params = os.environ.get("TARGET_DB_PARAMS")
        db_is_srv = False
    elif exchange == "Binance":
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_user = os.environ.get("DB_USER")
        db_pass = os.environ.get("DB_PASS")
        db_params = os.environ.get("DB_PARAMS")
        db_is_srv = False
    else:
        db_host = os.environ.get("BB_DB_HOST")
        db_port = os.environ.get("BB_DB_PORT")
        db_user = os.environ.get("BB_DB_USER")
        db_pass = os.environ.get("BB_DB_PASS")
        db_params = os.environ.get("BB_DB_PARAMS")
        db_is_srv = False

    print("CONNECTING TO {}".format("mongodb{db_is_srv}://{db_auth}{db_host}{db_port}/{db_name}?{db_params}".format(
        db_auth='{db_user}:{db_pass}@'.format(db_user=db_user, db_pass=db_pass) if db_user and db_pass else '',
        db_host=db_host,
        db_port=':{}'.format(db_port) if db_port else '',
        db_name=db_name,
        db_params=db_params,
        db_is_srv='+srv' if db_is_srv else ''
    )))

    return pymongo.MongoClient(
        "mongodb{db_is_srv}://{db_auth}{db_host}{db_port}/{db_name}?{db_params}".format(
            db_auth='{db_user}:{db_pass}@'.format(db_user=db_user, db_pass=db_pass) if db_user and db_pass else '',
            db_host=db_host,
            db_port=':{}'.format(db_port) if db_port else '',
            db_name=db_name,
            db_params=db_params,
            db_is_srv='+srv' if db_is_srv else ''
        ))