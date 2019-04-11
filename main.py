from flask import Flask, request, abort, Response
import cv2
import numpy as np

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def root():
    return "Image Process Server"

@app.route('/binarize', methods=['POST'])
def binarize():
    "画像を二値化する"
    if request.method == 'POST':
        data = np.fromstring(request.data, np.uint8)
        img = cv2.imdecode(data, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bin = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,31,15)
        ret, encoded = cv2.imencode('.png',bin)
        str_encoded = encoded.tobytes()
        return Response(response=str_encoded, status=200,
            mimetype="image/png")
    else:
        abort(404)


if __name__ == '__main__':
    # ローカルテスト環境
    app.run(host='127.0.0.1', port=8080, debug=True)
