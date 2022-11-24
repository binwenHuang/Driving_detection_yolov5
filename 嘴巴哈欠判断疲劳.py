from threading import Thread

import cv2
import myframe
from pydub import AudioSegment
from pydub.playback import play


# 嘴巴开合判断
MAR_THRESH = 0.65  # 打哈欠长宽比
MOUTH_AR_CONSEC_FRAMES = 3  # 闪烁阈值
mCOUNTER = 0  # 打哈欠帧计数器
mTOTAL = 0  # 打哈欠总数
Roll = 0  # 整个循环内的帧
Rollmouth = 0  # 循环内打哈欠数
ActionCOUNTER = 0           #分心行为计数器器
ALARM_ON = False

# 报警声函数定义
def sound_alarm(path):
    # play an alarm sound
    # music = pyglet.resource.media(path)
    # music.play()
    # pyglet.app.run()
    alarm = AudioSegment.from_wav(path)
    play(alarm)


cap = cv2.VideoCapture(0)

while True:
    _,img= cap.read()


    #检测检测面部信息
    ret, frame = myframe.frametest(img)
    lab, eye, mouth = ret

    #判断是否出现人脸
    if len(ret[0]) > 0:
        # 哈欠判断，根据嘴巴的长宽比
        if mouth > MAR_THRESH:
            mCOUNTER += 1
            Rollmouth += 1
        else:
            # 如果连续3次都小于阈值，则表示打了一次哈欠
            if mCOUNTER >= MOUTH_AR_CONSEC_FRAMES:
                mTOTAL += 1
                # 重置嘴帧计数器
                mCOUNTER = 0

        # 每打3次哈欠，表示有犯困的可能性,就进行提醒
        if mTOTAL != 0 and mTOTAL % 3 == 0:
            path = "sound/tired_sound.wav"
            if not ALARM_ON:
                ALARM_ON = True
                t2 = Thread(target=sound_alarm, args=(path,))
                print('ing....tired_sound')
                t2.setDaemon(True)
                t2.start()
            if ActionCOUNTER > 0:
                ActionCOUNTER -= 1
            mTOTAL += 1
        else:
            ALARM_ON = False

    cv2.imshow("test", frame)
    if cv2.waitKey(1) == ord('q'):
        break