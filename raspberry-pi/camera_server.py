from flask import Flask, Response
import cv2

app = Flask(__name__)

# 카메라 열기 (USB 카메라)
camera = cv2.VideoCapture(0)

# 해상도 설정 (선택)
camera.set(3, 640)  # width
camera.set(4, 480)  # height

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # JPEG로 인코딩
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # 스트리밍 형식
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "Camera Server Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)