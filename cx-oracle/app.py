from gevent.monkey import patch_all
patch_all()

from flask import Flask, request
import requests
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_SERVICE = os.environ['DB_SERVICE']

SQLALCHEMY_ORACLE = 'oracle+cx_oracle://{}:{}@{}:{}/?service_name={}&mode=2'
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_ORACLE.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_SERVICE)
print({SQLALCHEMY_DATABASE_URI})


engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=200)
Session = sessionmaker(bind=engine)


api_port = os.environ['PORT_API']
host_slow = os.environ['HOST_SLOW_API']
api_url = f'http://{host_slow}:{api_port}/'

app = Flask(__name__)

@app.route('/')
def index():
    session = Session()
    result = session.execute('select 1+1 from dual')
    try:
        delay = float(request.args.get('delay') or 1)
        resp = requests.get(f'{api_url}?delay={delay/2}')
    except:
        pass

    rsult = result.fetchall()
    session.close()
    print('bd response for 1+1 ->' + str(rsult[0][0]))

    return 'O resultado da API foi: {}\nA resposta do BD foi:{}!'.format(resp.text, rsult[0][0])


if __name__ == "__main__":
    app.run(
        host='0.0.0.0', 
        port=(os.environ['PORT']), 
        debug=(os.environ.get('DEBUG', False))
    )
