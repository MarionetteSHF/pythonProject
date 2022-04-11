
from flask import Flask
from flask import render_template



app = Flask(__name__)
import sql
"""
这是一个展示Flask如何读取服务器本地图片, 并返回图片流给前端显示的例子
"""

def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """

    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        # print(img_stream)
        # params=psycopg2.Binary(img_stream)
        # img_stream = Image.open(params)
        # img_stream = Image.open(io.BytesIO(params))

        db = sql.get_db()
        cur = db.cursor()
        img_stream = base64.b64encode(img_stream).decode()
        # command = "INSERT INTO Photos (photo_id, item_id, image_source) VALUES (default,%s,%s)"  # create table cataract
        # params = ("7", img_stream)
        # cur.execute(command, params)

        cur.execute(
            "SELECT image_source FROM Photos WHERE item_id = %s",
            ("7",),
        )
        data = cur.fetchone()
        # print("hhhhh")
        # print(data[0])
        # print("hhhhh")

        db.commit()
        db.close()
        img_stream = data[0]
        # img_stream = base64.b64encode(img_stream).decode()
        # print(img_stream)



    return img_stream



@app.route('/')
def hello_world():
    # img_path = 'D:\MME73.jpeg'
    # img_stream = return_img_stream(img_path)
    # return render_template('index.html',
    #                        img_stream=img_stream)
    return render_template("upload.html")

@app.route('/upload', methods=['get', 'post'])
def upload():

    # if request.method == 'POST':
    #     img = request.files['photo']
    #     # print(img.read())
    #     # print(img)
    #     img_stream =img.read()
    #     img_stream = base64.b64encode(img_stream).decode()
    #     print(img_stream)





    return render_template("upload.html")

if __name__ == '__main__':
    app.run(debug=True,port=8111)
