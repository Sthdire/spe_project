from flask import Flask, render_template, request

from init import app
from test import push_comm


@app.route('/', methods=['post', 'get'])
def hello_world():
    if request.method == 'POST':
        push_comm(request.form.get('username'), request.form.get('comment'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

