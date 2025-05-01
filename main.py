# ここからserver.pyのソースコード
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
  # WebAPIを取得しに行く。
  url = "https://weather.tsukumijima.net/api/forecast/"
  #400040は福岡県・久留米だけど、東京都・東京の番号に変更してくださいね。
  city_code = "city/400040"
  # 取得したWebAPIのデータをtenki_dataに代入（格納）
  # requests.get()のデータを、.json()でPythonの辞書型に変換する。
  tenki_data = requests.get(url+city_code).json()
  
  return render_template('index.html',
                        tenki_data=tenki_data)

if __name__ == "__main__":
  app.run(debug=True)
# ここまでserver.pyのソースコード
