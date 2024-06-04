from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="playlist"
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/playlist", methods=["POST"])
def playlist_post():
    try:
        url_receive = request.form['url_give']
        job_receive = request.form['job_give']
        comment_receive = request.form['comment_give']

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        image = soup.select_one('meta[property="og:image"]')['content']
        title = soup.select_one('meta[property="og:title"]')['content']

        cursor.execute("SELECT COUNT(*) AS count FROM movies")
        result = cursor.fetchone()
        count = result['count'] + 1

        sql = "INSERT INTO movies (num, title, image, url, job, comment) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (count, title, image, url_receive, job_receive, comment_receive)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({'msg': '저장 완료!'})

    except Exception as e:
        return jsonify({'msg': f'저장 실패: {str(e)}'}), 500

@app.route("/playlist", methods=["GET"])
def playlist_get():
    try:
        cursor.execute("SELECT num, title, image, url, job, comment FROM movies")
        play_list = cursor.fetchall()
        return jsonify({'lists': play_list})
    except Exception as e:
        return jsonify({'msg': f'불러오기 실패: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)