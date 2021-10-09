from flask import Flask, app, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    return render_template('hello.html')


@app.route('/item', methods=['GET', 'POST', 'PUT', 'DELETE'])
def item():
    return render_template('hello.html')


@app.route('/trade', methods=['GET', 'POST', 'PUT', 'DELETE'])
def trade():
    if request.method == "POST":
        return render_template('hello.html')
