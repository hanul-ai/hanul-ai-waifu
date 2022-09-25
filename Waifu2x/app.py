from Tools.scripts.pindent import start
from flask import Flask, request
import base64
import zlib
from main import *


app = Flask(__name__)

#POST
@app.route('/', methods=['POST'])
def post():
    print("start")
    # request.get_json()
    params = request.get_json()
    print("get data")
    z = base64.b64decode(params['image'].encode('utf-8'))
    print("base pass")
    image = zlib.decompress(z)
    print("zip pass")

    result_img = Start_Waifu(image)

    base = zlib.compress(result_img)
    z_base = base64.b64encode(base).decode('utf-8')
    return z_base

@app.route('/test', methods=['GET'])
def hello_world():
   return 'Hello World'

if __name__ == "__main__":
    app.run()