from Tools.scripts.pindent import start
from flask import Flask, request
import base64
import zlib
from Waifu2x import main


app = Flask(__name__)

#POST
@app.route('/', methods=['POST'])
def post_echo_call():
    params = request.get_json()
    image_zip = base64.a85encode(params['image'].decode('utf-8'))
    image = zlib.decompress(image_zip).decode('utf-8')

    result_img = main.Start_Waifu(image)

    base85_zip = zlib.compress(result_img)
    base85_string = base64.b85encode(base85_zip).decode('utf-8')
    return base85_string

if __name__ == "__main__":
    app.run()
