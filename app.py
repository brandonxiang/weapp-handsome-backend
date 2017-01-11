from __future__ import print_function
from flask import Flask
import sqlite3
import json
app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route('/validation/<openid>')
def validation(openid):
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
    return 'validation'

@app.route('/vote')
def vote():
    newScore = {"user":"robin","score":[(104,"bluebutterfly"),(105, "me")]}
    with sqlite3.connect('handsome.db') as conn:
        openid = newScore.get("user")
        cmd = "insert into validation (openid) values (?)"
        conn.execute(cmd, (openid,))

        print(newScore.get("score"))
        score = newScore.get("score")
        cmd = "update vote set score= ? where name = ?"
        conn.executemany(cmd, score)

        pass
    return 'vote'

if __name__ == '__main__':
    app.debug = True
    app.run()