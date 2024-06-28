import pymysql
import serial
import time
import requests
from objectDetect import objectDetect
from camera_pi import Camera
import numpy as np
import cv2
import math

ser = serial.Serial('/dev/ttyUSB0')  

ser.baudrate = 9600

ser.timeout = 1 

def connect_db():
    return pymysql.connect(host='localhost',
                           user='daniel',
                           password='Lqy41172!',
                           db='web',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def format_value(value):
    return str(- int(value * 512) + 512).zfill(4)

def format_valu(value):
    return str(value).zfill(4)

def calcAng(x, y, resx, resy):
    angx = math.atan((x-160)/160*math.tan(math.radians(27)))
    angy = math.atan((y-120)/120*math.tan(math.radians(20.5)))
    return math.degrees(angx), math.degrees(angy)

def query_joystick_data(joystick_id):
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            sql = "SELECT x, y FROM joystick_data WHERE joystick_id = %s"
            cursor.execute(sql, (joystick_id,))
            result = cursor.fetchone()
            if result:
                return format_value(result['x']), format_value(result['y'])
            else:
                return "0512", "0512"
    except Exception as e:
        print(f"Database error: {e}")
        return "0512", "0512" 
    finally:
        connection.close()

def send_data(lx,ly,rx,ry):
    output_string = f"{lx}{ly}{rx}{ry}"
    ser.write(output_string.encode())

def query_mouse_data():
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            sql = "SELECT x, y FROM mouse_data WHERE mouse_id = 0"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result['x'], result['y']
            else:
                return -1, -1 
    except Exception as e:
        print(f"Database error: {e}")
        return -1, -1 
    finally:
        connection.close()

def get_object():
    response = requests.get("http://localhost/get_objects")
    if response.status_code == 200:
        return response.json()
    return None

hori = 0
vert = 0

def image_move(x, y):
    dx, dy =calcAng(x,y,160,120)
    nx=0
    ny=0
    if dx>=0:nx = 200
    else: nx = 850
    print(dx)
    dx = math.fabs(dx)
    time.sleep(0.02)
    send_data(format_valu(int(512)), format_valu(nx), format_valu(512), format_valu(512))
    while dx > 1:
        #print(dx)
        dx-= 1
        time.sleep(0.02)
    if dy>=0:ny = 200
    else: ny = 850
    print(dy)
    dy = math.fabs(dy)
    time.sleep(0.015)
    send_data(format_valu(ny), format_valu(int(512)), format_valu(512), format_valu(512))
    while dy > 1:
    #print(dy)
        dy-= 2
        time.sleep(0.02)
    time.sleep(0.1)
    send_data(format_valu(512), format_valu(512), format_valu(512), format_valu(512))

if __name__ == "__main__":
    objectDetect.initialize()
    while True:
        print(ser.readline())
        ly, lx = query_joystick_data("left")
        ry, rx = query_joystick_data("right")
        send_data(lx,ly,rx,ry)
        data = get_object()
        x, y = query_mouse_data()
        a=0
        #print(data)
        if data != None:
            for i in data:
                a = a+1
                pos = i
                #print(str(pos)+" "+str(x)+" "+str(y))
                if x<=pos[0]+pos[2] and x>=pos[0] and y>=pos[1] and y<=pos[1]+pos[3]:
                    print(1)
                    image_move((pos[0]*2+pos[2])/2,(pos[1]*2+pos[3])/2)
                    time.sleep(0.1)
                    break
        #if x!=-1 and y!=-1:
        #    image_move(x,y)
        #print(data)
        time.sleep(0.02)
