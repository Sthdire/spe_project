from flask import Flask, render_template, request

from init import app
import test


@app.route('/', methods=['post', 'get'])
def hello_world():
    if request.method == 'POST':
        test.push_comm(request.form.get('username'), request.form.get('comment'))
    i = 0
    username = ['', '', '', '', '', '', '', '', '', '']
    com_value = ['', '', '', '', '', '', '', '', '', '']
    while i < 10:
        username[i] = test.get_comm_username(i + 1)
        com_value[i] = test.get_comm_value(i + 1)
        i += 1
    return render_template('index.html', username=username, com_value=com_value)  # , username = username, comment= comment


if __name__ == '__main__':
    app.run(debug=True)
