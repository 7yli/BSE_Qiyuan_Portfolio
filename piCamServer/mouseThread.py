import pymysql
import time


def connect_db():
    return pymysql.connect(host='localhost',
                           user='daniel',
                           password='Lqy41172!',
                           db='web',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

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

if __name__ == "__main__":
    while True:
        x, y = query_mouse_data()
        print(x)
        print(y)
        time.sleep(0.1)
