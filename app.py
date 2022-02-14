from flask import Flask, render_template, request
import sys

from detoxify import Detoxify

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def root():
    if request.method == 'GET':
        return render_template('web_app.html')
    if request.method == 'POST':
        data = request.form.get('text_to_send')

        toxicity = Detoxify('original')
        results = toxicity.predict(data)
        
        text_to_render = f'<br><strong>results for : "</strong>{data}"<br><br>'
        for key in results :
            key_percent = (results[key]*100).round(3)
            text_to_render += f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{key} : {key_percent}%<br>'

        return render_template('result.html', toxicity_results = text_to_render)


app.run(host='localhost', port=5000)