
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def func():
    name = request.args.get('name')
    message = request.args.get('message')
    if name == None or message == None:
        return 'Наберите get запрос (/?name=Rekruto&message=Давай дружить!) и всё заработает <br> Надеюсь я правильно понял задание :)'
    return f"Hello {name}! <br> {message}"



if __name__ == '__main__':
    app.run(debug=True, port=5000)