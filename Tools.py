import datetime
import logging
import sys
import time
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageTk

WARN = 0
INFO = 1
MESSAGE = 2
logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def logFormat(l, info):
    """
    将运行日志输出到控制台。
    1：INFO
    2：WARN
    3：MESSAGE
    :param l: 输出信息的等级
    :param info: 输出信息的语句
    :return: None
    """
    if l == 1:
        level = 'INFO'
    elif l == 2:
        level = 'WARN'
    else:
        level = 'MESSAGE'

    t = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    val = '[{}] {} {}'.format(level, t, info)
    logging.info(val)


def getTimeStamp() -> int:
    """
    获取时间戳，精确到毫秒。
    :return:返回时间戳
    """
    return int(time.time() * 1000)


def pic2TKpic(img, img_size, code=-1):
    """
    用cv2的方法读取图像，转为array类型，再转为tk类型。
    普通的tk方法不能显示gif以外的图片。
    :param code: 图片的读取方式
    :param img: 图片路径。
    :param img_size: 图片大小（长*宽）。
    :return:
    """
    img_ = cv2.imread(img, code)
    img__ = cv2.resize(img_, img_size)
    img__ = cv2.cvtColor(img__, cv2.COLOR_BGR2RGB)
    img___ = Image.fromarray(img__)
    img____ = ImageTk.PhotoImage(image=img___)
    return img____
