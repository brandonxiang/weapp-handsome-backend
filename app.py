from __future__ import print_function
from flask import Flask, request
import sqlite3
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/validation', methods=['post'])
def validation():
    openid = request.get_json().get("openid")
    try:
         with sqlite3.connect('./handsome.db') as conn:
            cmd = "select openid from validation where openid = ?"
            cursor = conn.execute(cmd,(openid,))
            user = cursor.fetchall()

            cmd = "select * from vote"
            cursor = conn.execute(cmd)
            score = cursor.fetchall()
            user_num = len(user)
            result = {"user":user_num,"score":score}
            return json.dumps(result)
    except:
        return 'Fail to validation'
   


@app.route('/vote', methods=['post'])
def vote():
    try:
        newScore = request.get_json()
        with sqlite3.connect('handsome.db') as conn:
            openid = newScore.get("user")
            cmd = "insert into validation (openid) values (?)"
            conn.execute(cmd, (openid,))

            print(newScore.get("score"))
            score = newScore.get("score")
            cmd = "update vote set score = score+1 where name = ?"
            conn.execute(cmd, (score,))
        return 'Succeed to reset'
    except Exception as e:
        return 'Fail to vote'+ e.args
   


@app.route('/reset',methods=['get'])
def reset():
    try:
        if request.args.get('id') == "19910525":
            with sqlite3.connect('handsome.db') as conn:
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