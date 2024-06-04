from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://ecec1023:Ljx10jeUZF0dGHIW@movies.aivdll0.mongodb.net/movies?retryWrites=true&w=majority&appName=movies')
db = client.movies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/playlist", methods=["POST"])
def playlist_post():
    
        url_receive = request.form['url_give']
        job_receive = request.form['job_give']
        comment_receive = request.form['comment_give']
    
    # URL을 읽어서 HTML를 받아오고,
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다. 크롤링 기본코드
        image = soup.select_one('meta[property="og:image"]')['content']
        title = soup.select_one('meta[property="og:title"]')['content']

        play_list = list(db.movies.find({}, {'_id': False}))
        count = len(play_list) + 1

        doc = {
            'num':count, # 저장된 숫자를 기록하게 만듦
            'title':title,
            'image':image,
            
            'url':url_receive,
            'job':job_receive,
            'comment':comment_receive,
        }
    
        db.movies.insert_one(doc)

        return jsonify({'msg': '저장 완료!'})

@app.route("/playlist", methods=["GET"])
def playlist_get():
    play_list = list(db.movies.find({},{'_id':False}))

    return jsonify({'lists': play_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)