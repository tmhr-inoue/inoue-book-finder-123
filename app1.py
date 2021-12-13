from flask import Flask, render_template, request
app = Flask(__name__)
 

@app.route('/', methods=['GET']) #requestの種類 textデータのみを取得　htmlファイルを見るだけ
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])#requestの種類 ユーザーからの情報を送る場合（ログイン情報等）　
def form():
    field = request.form['keyword'] #検索キーワードの取得
    return render_template('webapp.html', message = 'aaaaaa')#結果の表示



@app.route('/predict', methods=['GET','POST'])#アプリとユーザーとのやり取り次第でget postを使い分ける
def myfunc(index,df_comment){
        title = np.array(df_comment)[index,0]
        return title
         }



def predict():
  if request.method == 'GET':
     return render_template('index.html')
  
  if request.method == 'POST':
    keyword = request.form['keyword']
    model = pickle.load(open('./model/model.pkl', 'rb'))#商品説明のワカチ書きデータ
    model_item = pickle.load(open('./model/model_item.pkl', 'rb'))#
    sims = model.wv.most_similar(positive = keyword)#keywordと商品説明の類似度
    for i in sims:
        graph = myfunc(i[0],model_item)
    return render_template('index.html', message = graph)

if __name__ == '__main__':
    app.debag = True
    app.run(host='localhost')

