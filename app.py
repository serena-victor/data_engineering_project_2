from flask import Flask, render_template, request
import sys


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def root():
    if request.method == 'GET':
        return render_template('web_app.html')
    if request.method == 'POST':
        data = request.form.get('text_to_send')
        result = data[::-1]

        return render_template('result.html', result = result)


app.run(host='localhost', port=5000)