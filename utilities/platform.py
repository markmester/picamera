from threading import Thread


def get_current_position(pantilt):
    return (pantilt.get_servo_one(),
            pantilt.get_servo_two())


def move(azimuth, elevation, pantilt):

    current_azimuth, current_elevation = (pantilt.get_servo_one(), pantilt.get_servo_two())

    def pan(x):
        if current_azimuth + x > 90:
            pantilt.servo_one(90)
        else:
            pantilt.servo_one(current_azimuth + x)

    def tilt(y):
        if elevation + y > 90:
            pantilt.servo_two(90)
        else:
            pantilt.servo_two(current_elevation + y)

    t1 = Thread(target=pan, args=(azimuth,))
    t2 = Thread(target=tilt, args=(elevation,))

    t1.start()
    t2.start()
