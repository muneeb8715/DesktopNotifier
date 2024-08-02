from plyer import notification
import time

if __name__=="__main__":
    while True:
         notification.notify(
            title = "*** Take Rest ***",
            message = ''' In the office brief respite,
            keyboards hush, and coffee mugs clink,
            a symphony of a moments peace in the corporate hum.''',
            app_icon = "F:\Python-course/vk.ico",
            timeout = 5)
         time.sleep(20)

## background m Run k lea  (pythonw file.py)