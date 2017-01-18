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

@app.route('/validation', methods=['POST','GET'])
def validation():
    openid = request.args.get('openid', '')

    conn = g.db.cursor()
    cmd = "select * from validation"
    conn.execute(cmd)
    user = conn.fetchall()

    return openid

        # cmd = "select * from vote"
        # cursor = conn.execute(cmd)
        # score = cursor.fetchall()
        # user_num = len(user)
        # result = {"user":user_num,"score":score}
        # return json.dumps(result)
   
   


@app.route('/vote',  methods=['POST','GET'])
def vote():
    openid = request.args.get('user', '')
    score = request.args.get('score', '')
    try:
        conn = g.db.cursor()
        cmd = "insert into validation (openid) values (?)"
        conn.execute(cmd, (openid,))

        cmd = "update vote set score= ? where name = ?"
        conn.executemany(cmd, score)
        return 'Succeed to reset'
    except:
        return 'Fail to vote'
   


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