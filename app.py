from flask import Flask, request

app = Flask(__name__)

#POST
@app.route('/', methods=['POST'])
def post_echo_call():
    params = request.get_json()

    return 'ok'

if __name__ == "__main__":
    app.run()
