import base64
import zlib

with open('E:/Users/tmfql/OneDrive/문서/GitHub/hanul-ai-waifu/Waifu2x/input.png', 'rb') as img:
    base85_zip = zlib.compress(img.read())
    base85_string = base64.b64encode(base85_zip).decode('utf-8')
    print(base85_string)
    # print(len(base85_string))