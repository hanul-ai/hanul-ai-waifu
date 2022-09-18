import base64
import zlib

with open('E:/Users/tmfql/PycharmProjects/Flask_API_AI/Waifu2x-master/input_image.png', 'rb') as img:
    base85_zip = zlib.compress(img.read())
    base85_string = base64.b85encode(base85_zip).decode('utf-8')
    print(base85_string)
    # print(len(base85_string))

