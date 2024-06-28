from flask import Flask, render_template, Response, request, jsonify, send_file
from camera_pi import Camera  # 确保Camera类已经正确导入
import cv2
from flask_sqlalchemy import SQLAlchemy
import pymysql
import io
from objectDetect import objectDetect

app = Flask(__name__)

# 安全实践：从环境变量中加载敏感信息
import os
HOSTNAME = "localhost"
PORT = 3306
USERNAME = os.getenv("DB_USERNAME", "daniel")
PASSWORD = os.getenv("DB_PASSWORD", "Lqy41172!")
DATABASE = "web"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class JoystickData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joystick_id = db.Column(db.String(10), nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)

class MouseData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mouse_id = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

datas = []

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera_instance):
    """Video streaming generator function."""
    while True:
        frame = camera_instance.get_frame()
        global datas
        if frame is not None:
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame, datas = objectDetect.getObjects(frame, 0.5, 0.2)
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        else:
            # Handle the case where frame is None more gracefully
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + b'Camera is initializing or has been closed.' + b'\r\n')
            break  # Exit the loop if the camera is no longer active

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_objects')
def get_objects():
        # 假设 objectDetect.getObjects() 返回的是列表和对象检测数据
    detected_objects = datas
    x = []
    for i in detected_objects:
        a = []
        for j in i[0]:
            a.append(int(j))
        x.append(a)
    print(x,type(x))
    return jsonify(x)  # 使用 jsonify 来正确返回 JSON 数据


@app.route('/joystick_data', methods=['POST'])
def joystick_data():
    data = request.get_json()
    jd = JoystickData.query.filter_by(joystick_id=data['joystick']).first()
    new_data = JoystickData(
        joystick_id=data['joystick'],
        x=data['data']['vector']['x'],
        y=data['data']['vector']['y']
    )
    if jd is None:
        db.session.add(new_data)
    else:
        jd.x = data['data']['vector']['x']
        jd.y = data['data']['vector']['y']
    #print(f"Received data from {data['joystick']} joystick: {data['data']['vector']['x']}")
    db.session.commit()
    return jsonify(success=True)

@app.route('/mouse_data', methods=['POST'])
def mouse_data():
    data = request.get_json()
    md = MouseData.query.filter_by(mouse_id=0).first()
    new_data = MouseData(
        mouse_id = 0,
        x=data['x'],
        y=data['y']
    )
    if md is None:
        db.session.add(new_data)
    else:
        md.x = data['x']
        md.y = data['y']
    #print(f"Received data from {data['joystick']} joystick: {data['data']['vector']['x']}")
    db.session.commit()
    print("Received mouse data:", data)
    return jsonify(data)


if __name__ == '__main__':
    objectDetect.initialize()
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
