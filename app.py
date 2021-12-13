from flask import Flask, render_template, request
import pickle, os
import numpy as np
import random
import pandas as pd
app = Flask(__name__)
 

@app.route('/', methods=['GET']) #requestの種類 textデータのみを取得　htmlファイルを見るだけ
def index():
    filepath1 = os.path.dirname(os.path.abspath(__file__)) + "/flask_app/model/model.pkl"
    filepath2 = os.path.dirname(os.path.abspath(__file__)) + "/flask_app/model/model_item.pkl"

    model = pickle.load(open(filepath1, 'rb'))#商品説明のワカチ書きデータ
    model_item = pickle.load(open(filepath2, 'rb'))#
    item_list = myfunc([random.randint(0, 2969) for i in range(10)],model_item)
    
    return render_template('index.html', message1 = item_list[0][0], message2 = item_list[0][1], message3 = item_list[0][2], message4 = item_list[0][3], message5 = item_list[0][4], message6 = item_list[0][5], message7 = item_list[0][6], message8 = item_list[0][7], message9 = item_list[0][8])


#アプリとユーザーとのやり取り次第でget postを使い分ける
def myfunc(index,df_comment):
    title = np.array(df_comment)[index,1]#Index　配列のエラー
    setsumei = np.array(df_comment)[index,2]
    return title, setsumei
    
@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'GET':
    return render_template('index.html')
  
  if request.method == 'POST':
    title = request.form["you"]
    filepath1 = os.path.dirname(os.path.abspath(__file__)) + "/flask_app/model/model.pkl"
    model = pickle.load(open(filepath1, 'rb'))#作品説明のワカチ書きデータ
    filepath2 = os.path.dirname(os.path.abspath(__file__)) + "/flask_app/model/model_item.pkl"
    model_item = pickle.load(open(filepath2, 'rb'))#作品名と作品説明

    item_number = model_item.query(f"作品名 == \"{title}\"")["id"]
    sims = model.dv.most_similar(item_number)#　作品のindex　類似度
    graph = myfunc(sims[0][0],model_item)
    return render_template('webappa.html', message1 = graph[0], message2 = graph[1])

# if __name__ == '__main__':
if __name__ == "__main__":
  port = int(os.environ.get('PORT', 8080))
  app.run(host ='0.0.0.0',port = port)
    # app.debug = True
    # app.run(host='localhost')




