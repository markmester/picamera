import yaml
import logging
from utilities import test, camera

logging.basicConfig(level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

with open('config/config.yml', 'r+') as f:
    config = yaml.load(f)


if __name__ == '__main__':
    while True:
        try:
            camera.start_camera_feed()
            test.test()
        except KeyboardInterrupt:
            exit(1)






