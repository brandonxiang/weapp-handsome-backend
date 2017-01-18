from __future__ import print_function
from flask import Flask, request, g
import json
import MySQLdb
app = Flask(__name__)
from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
    MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
)

@app.before_request
def before_request():
    g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
                           MYSQL_DB, port=int(MYSQL_PORT))


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/validation', methods=['POST'])
def validation():
    openid = json.loads(request.data).get("openid")

    conn = g.db.cursor()
    cmd = "select * from validation where openid = %s"
    conn.execute(cmd,(openid))
    user = conn.fetchall()

    cmd = "select * from vote"
    conn.execute(cmd)
    score = conn.fetchall()
    user_num = len(user)
    result = {"user":user_num,"score":score}
    return json.dumps(result)


@app.route('/vote',  methods=['POST'])
def vote():
    res = json.loads(request.data)

    openid = res.get('user')
    score = res.get('score')

    conn = g.db.cursor()
    cmd = "insert into validation (openid) values (%s)"
    conn.execute(cmd, (openid))

    cmd = "update vote set score= %s where name = %s"
    conn.executemany(cmd, score)
    return 'Succeed to reset'

   


@app.route('/reset',methods=['get'])
def reset():
    try:
        if request.args.get('id') == "19910525":
            conn = g.db.cursor()
            cmd = "delete from validation"
            conn.execute(cmd)
            cmd = "update vote set score = 0"
            conn.execute(cmd)
            return 'Succeed to reset'
    except:
        return 'Fail to reset'
    
    

if __name__ == '__main__':
    app.debug = True
    app.run()