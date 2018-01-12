import requests
import json
# from threading import Timer
import threading
import pygame
import time
import sys
from pygame.locals import *

TIme_out = 600

url = r'http://api.map.baidu.com/telematics/v3/weather?location=%E5%A5%8E%E6%96%87&output=json&ak=你申请的ak'
jsonStr = requests.get(url).text
data = json.loads(jsonStr)

error = data["error"]
status = def strTimetoSec(time):

    time_list = time.split(':')

    return (float(time_list.pop()) + int(time_list.pop()) * 60 + int(time_list.pop()) * 3600)



trades = {'B': [], 'D': [], 'J': [], 'K': [], 'P': [], 'Q': [], 'V': [], 'X': [], 'Y': [], 'Z': [], 'All': []}

max = {'B': 0, 'D': 0, 'J': 0, 'K': 0, 'P': 0, 'Q': 0, 'V': 0, 'X': 0, 'Y': 0, 'Z': 0, 'All': 0}

times = {'B': 0, 'D': 0, 'J': 0, 'K': 0, 'P': 0, 'Q': 0, 'V': 0, 'X': 0, 'Y': 0, 'Z': 0, 'All': 0}



def cell(line_table):

    list_line=line_table.split(',')

    time=strTimetoSec(list_line[0])

    ex = list_line[3][0]

    append_trade(time,ex)



def append_trade(time, ex):

    trades[ex].append(time)

    while time - trades[ex][0] >= 1:

        trades[ex].pop(0)

    if len(trades[ex]) > max[ex]:

        max[ex] = len(trades[ex])

        times[ex] = trades[ex][0]

    if ex != 'All':

        ex = 'All'

        append_trade(time, ex)

def secondToStrTime(time):

    o_min = ''

    o_hours = ''

    o_sec = ''

    hour = int(time // 3600)

    time -= hour * 3600

    min = int(time // 60)

    sec = int((time - min * 60) * 1000) / 1000

    if hour < 10: o_hours = '0'

    if min< 10: o_min = '0'

    if sec < 10: o_sec = '0'

    return o_hours + str(hour) + ':' + o_min + str(min) + ':' + o_sec + str(sec)

with open("TRD2.csv") as f:

    f.readline()

    for line in f.readlines():

        cell(line)

print('Exchange:  '+'Max:  '+'Time:')

for a in max:

    p='        '

    if a == 'All':

        p = '      '

    print(a + ':', p + str(max[a]), ' ' * (5 - len(str(max[a]))) + secondToStrTime(times[a])) data["status"]
date = data["date"]
currentCity = data["results"][0]["currentCity"]
pm25 = data["results"][0]["pm25"]


class Index:
    title = "title"
    zs = "zs"
    tipt = "tipt"
    des = "des"


class Weather_data:
    date = "date"
    dayPictureUrl = "0"
    nightPictureUrl = "0"
    weather = "0"
    wind = "0"
    temperature = "0"


chuan_yi = Index()
xi_che = Index()
gan_mao = Index()
yun_dong = Index()
zi_wai = Index()

day = Weather_data()
day1 = Weather_data()
day2 = Weather_data()
day3 = Weather_data()

Thread1_flg = 1
Time_Data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def Tian_Qi_undate():
    Thread1_Update_flg = 700
    global Time_Data
    global pm25
    global currentCity
    global date
    global status
    global error

    while Thread1_flg:

        if (Thread1_Update_flg >= 300):
            print("Update ok")
            Thread1_Update_flg = 0
            jsonStr = requests.get(url).text
            data = json.loads(jsonStr)

            Time_Data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            error = data["error"]
            status = data["status"]
            date = data["date"]
            currentCity = data["results"][0]["currentCity"]
            pm25 = data["results"][0]["pm25"]

            chuan_yi.title = data["results"][0]["index"][0]["title"]
            chuan_yi.zs = data["results"][0]["index"][0]["zs"]
            chuan_yi.tipt = data["results"][0]["index"][0]["tipt"]
            chuan_yi.des = data["results"][0]["index"][0]["des"]

            xi_che.title = data["results"][0]["index"][1]["title"]
            xi_che.zs = data["results"][0]["index"][1]["zs"]
            xi_che.tipt = data["results"][0]["index"][1]["tipt"]
            xi_che.des = data["results"][0]["index"][1]["des"]

            gan_mao.title = data["results"][0]["index"][2]["title"]
            gan_mao.zs = data["results"][0]["index"][2]["zs"]
            gan_mao.tipt = data["results"][0]["index"][2]["tipt"]
            gan_mao.des = data["results"][0]["index"][2]["des"]

            yun_dong.title = data["results"][0]["index"][3]["title"]
            yun_dong.zs = data["results"][0]["index"][3]["zs"]
            yun_dong.tipt = data["results"][0]["index"][3]["tipt"]
            yun_dong.des = data["results"][0]["index"][3]["des"]

            zi_wai.title = data["results"][0]["index"][4]["title"]
            zi_wai.zs = data["results"][0]["index"][4]["zs"]
            zi_wai.tipt = data["results"][0]["index"][4]["tipt"]
            zi_wai.des = data["results"][0]["index"][4]["des"]

            day.date = data["results"][0]["weather_data"][0]["date"]
            day.dayPictureUrl = data["results"][0]["weather_data"][0]["dayPictureUrl"]
            day.nightPictureUrl = data["results"][0]["weather_data"][0]["nightPictureUrl"]
            day.weather = data["results"][0]["weather_data"][0]["weather"]
            day.wind = data["results"][0]["weather_data"][0]["wind"]
            day.temperature = data["results"][0]["weather_data"][0]["temperature"]

            day1.date = data["results"][0]["weather_data"][1]["date"]
            day1.dayPictureUrl = data["results"][0]["weather_data"][1]["dayPictureUrl"]
            day1.nightPictureUrl = data["results"][0]["weather_data"][1]["nightPictureUrl"]
            day1.weather = data["results"][0]["weather_data"][1]["weather"]
            day1.wind = data["results"][0]["weather_data"][1]["wind"]
            day1.temperature = data["results"][0]["weather_data"][1]["temperature"]

            day2.date = data["results"][0]["weather_data"][2]["date"]
            day2.dayPictureUrl = data["results"][0]["weather_data"][2]["dayPictureUrl"]
            day2.nightPictureUrl = data["results"][0]["weather_data"][2]["nightPictureUrl"]
            day2.weather = data["results"][0]["weather_data"][2]["weather"]
            day2.wind = data["results"][0]["weather_data"][2]["wind"]
            day2.temperature = data["results"][0]["weather_data"][2]["temperature"]

            day3.date = data["results"][0]["weather_data"][3]["date"]
            day3.dayPictureUrl = data["results"][0]["weather_data"][3]["dayPictureUrl"]
            day3.nightPictureUrl = data["results"][0]["weather_data"][3]["nightPictureUrl"]
            day3.weather = data["results"][0]["weather_data"][3]["weather"]
            day3.wind = data["results"][0]["weather_data"][3]["wind"]
            day3.temperature = data["results"][0]["weather_data"][3]["temperature"]

            print("错误", error)
            print("statue", status)
            print("时间", date)
            print("城市", currentCity)
            print("PM2.5 : ", pm25)

            print(chuan_yi.title)
            print(chuan_yi.zs)
            print(chuan_yi.tipt)
            print(chuan_yi.des)

            print(xi_che.title)
            print(xi_che.zs)
            print(xi_che.tipt)
            print(xi_che.des)

            print(gan_mao.title)
            print(gan_mao.zs)
            print(gan_mao.tipt)
            print(gan_mao.des)

            print(yun_dong.title)
            print(yun_dong.zs)
            print(yun_dong.tipt)
            print(yun_dong.des)

            print(zi_wai.title)
            print(zi_wai.zs)
            print(zi_wai.tipt)
            print(zi_wai.des)

            print(day.date)
            print(day.dayPictureUrl)
            print(day.nightPictureUrl)
            print(day.weather)
            print(day.wind)
            print(day.temperature)

            print(day1.date)
            print(day1.dayPictureUrl)
            print(day1.nightPictureUrl)
            print(day1.weather)
            print(day1.wind)
            print(day1.temperature)

            print(day2.dayPictureUrl)
            print(day2.nightPictureUrl)
            print(day2.weather)
            print(day2.wind)
            print(day2.temperature)

            print(day3.date)
            print(day3.dayPictureUrl)
            print(day3.nightPictureUrl)
            print(day3.weather)
            print(day3.wind)
            print(day3.temperature)

            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("-------------------------------------")

        Thread1_Update_flg += 1
        time.sleep(1)
    # t1 = threading.Timer(2, Tian_Qi_undate)


# t1.start()

# Tian_Qi_undate()

t1 = threading.Thread(target=Tian_Qi_undate)
t1.start()
# --------------------------------------------------------------------
full_screen = False
Time_num = 0
pygame.init()

ScreenSize = (1300, 900)
GameScreen = pygame.display.set_mode(ScreenSize, pygame.RESIZABLE, 32)

X_1 = 20  # X坐标首个显示位置
X_2 = 400
X_3 = 800

Y_1 = 30  # Y坐标第一行位置
Y_2 = 130
Y_3 = 180
Y_4 = 230
Y_5 = 280
Y_6 = 330
Y_7 = 380
Y_8 = 430
Y_9 = 480
Y_10 = 530
Y_11 = 580
Y_12 = 630
Y_13 = 680
Y_14 = 720
Y_15 = 750
Y_16 = 780
Y_17 = 810

black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255
red = 255, 0, 0
green = 0, 255, 0

# DefaultFont = "/opt/Fonts/simkai.ttf"
# DefaultFont = "/like/Fonts/simkai.ttf"
DefaultFont = "C:\Windows\Fonts\simkai.ttf"


class GameText:
    Font = DefaultFont
    Size = 40
    Text = "123abc中文"
    Rgb = red
    Coords = 100, 50

    def Display_Update(self):
        GameScreen.blit(pygame.font.Font(self.Font, self.Size).render(self.Text, True, self.Rgb), (self.Coords))


GameScreen.fill(black)  # 背景颜色
Text1 = GameText()
Text1.Text = "天气预报"
Text1.Size = 80
Text1.Rgb = white
Text1.Coords = 300, 50
# Text1.display()

while True:
    GameScreen.fill(black)  # 背景颜色

    Time_display = GameText()
    Time_display.Text = (time.strftime('%Y-%m-%d %H:%M:%S %A', time.localtime(time.time())))
    Time_display.Size = 60
    Time_display.Rgb = white
    Time_display.Coords = 180, Y_1
    Time_display.Display_Update()

    Cheng_shi = GameText()
    Cheng_shi.Text = currentCity
    Cheng_shi.Size = 40
    Cheng_shi.Rgb = white
    Cheng_shi.Coords = X_1, Y_2
    Cheng_shi.Display_Update()

    day_date = GameText()
    day_date.Text = day.date
    day_date.Size = 40
    day_date.Rgb = white
    day_date.Coords = 200, Y_2
    day_date.Display_Update()

    day_temperature = GameText()
    day_temperature.Text = day.temperature
    day_temperature.Size = 40
    day_temperature.Rgb = white
    day_temperature.Coords = 800, Y_2
    day_temperature.Display_Update()

    day_weather = GameText()
    day_weather.Text = day.weather
    day_weather.Size = 40
    day_weather.Rgb = white
    day_weather.Coords = X_1, Y_3
    day_weather.Display_Update()

    day_wind = GameText()
    day_wind.Text = day.wind
    day_wind.Size = 40
    day_wind.Rgb = white
    day_wind.Coords = 500, Y_3
    day_wind.Display_Update()

    Pm25_display = GameText()
    Pm25_display.Text = "PM2.5：" + pm25
    Pm25_display.Size = 40
    Pm25_display.Rgb = white
    Pm25_display.Coords = 800, Y_3
    Pm25_display.Display_Update()

    chuan_yi_tipt = GameText()
    chuan_yi_tipt.Text = chuan_yi.tipt
    chuan_yi_tipt.Size = 40
    chuan_yi_tipt.Rgb = white
    chuan_yi_tipt.Coords = X_1, Y_4
    chuan_yi_tipt.Display_Update()

    chuan_yi_zs = GameText()
    chuan_yi_zs.Text = chuan_yi.zs
    chuan_yi_zs.Size = 40
    chuan_yi_zs.Rgb = white
    chuan_yi_zs.Coords = 250, Y_4
    chuan_yi_zs.Display_Update()

    chuan_yi_des = GameText()
    chuan_yi_des.Text = chuan_yi.des
    chuan_yi_des.Size = 30
    chuan_yi_des.Rgb = white
    chuan_yi_des.Coords = X_1, Y_5
    chuan_yi_des.Display_Update()

    xi_che_tipt = GameText()
    xi_che_tipt.Text = xi_che.tipt
    xi_che_tipt.Size = 40
    xi_che_tipt.Rgb = white
    xi_che_tipt.Coords = X_1, Y_6
    xi_che_tipt.Display_Update()

    xi_che_zs = GameText()
    xi_che_zs.Text = xi_che.zs
    xi_che_zs.Size = 40
    xi_che_zs.Rgb = white
    xi_che_zs.Coords = 250, Y_6
    xi_che_zs.Display_Update()

    xi_che_des = GameText()
    xi_che_des.Text = xi_che.des
    xi_che_des.Size = 30
    xi_che_des.Rgb = white
    xi_che_des.Coords = X_1, Y_7
    xi_che_des.Display_Update()

    gan_mao_tipt = GameText()
    gan_mao_tipt.Text = gan_mao.tipt
    gan_mao_tipt.Size = 40
    gan_mao_tipt.Rgb = white
    gan_mao_tipt.Coords = X_1, Y_8
    gan_mao_tipt.Display_Update()

    gan_mao_zs = GameText()
    gan_mao_zs.Text = gan_mao.zs
    gan_mao_zs.Size = 40
    gan_mao_zs.Rgb = white
    gan_mao_zs.Coords = 250, Y_8
    gan_mao_zs.Display_Update()

    gan_mao_des = GameText()
    gan_mao_des.Text = gan_mao.des
    gan_mao_des.Size = 30
    gan_mao_des.Rgb = white
    gan_mao_des.Coords = X_1, Y_9
    gan_mao_des.Display_Update()

    yun_dong_tipt = GameText()
    yun_dong_tipt.Text = yun_dong.tipt
    yun_dong_tipt.Size = 40
    yun_dong_tipt.Rgb = white
    yun_dong_tipt.Coords = X_1, Y_10
    yun_dong_tipt.Display_Update()

    yun_dong_zs = GameText()
    yun_dong_zs.Text = yun_dong.zs
    yun_dong_zs.Size = 40
    yun_dong_zs.Rgb = white
    yun_dong_zs.Coords = 250, Y_10
    yun_dong_zs.Display_Update()

    yun_dong_des = GameText()
    yun_dong_des.Text = yun_dong.des
    yun_dong_des.Size = 30
    yun_dong_des.Rgb = white
    yun_dong_des.Coords = X_1, Y_11
    yun_dong_des.Display_Update()

    zi_wai_tipt = GameText()
    zi_wai_tipt.Text = zi_wai.tipt
    zi_wai_tipt.Size = 40
    zi_wai_tipt.Rgb = white
    zi_wai_tipt.Coords = X_1, Y_12
    zi_wai_tipt.Display_Update()

    zi_wai_zs = GameText()
    zi_wai_zs.Text = zi_wai.zs
    zi_wai_zs.Size = 40
    zi_wai_zs.Rgb = white
    zi_wai_zs.Coords = 350, Y_12
    zi_wai_zs.Display_Update()

    zi_wai_des = GameText()
    zi_wai_des.Text = zi_wai.des
    zi_wai_des.Size = 30
    zi_wai_des.Rgb = white
    zi_wai_des.Coords = X_1, Y_13
    zi_wai_des.Display_Update()

    day1_date = GameText()
    day1_date.Text = day1.date
    day1_date.Size = 30
    day1_date.Rgb = white
    day1_date.Coords = X_1, Y_14
    day1_date.Display_Update()

    day1_weather = GameText()
    day1_weather.Text = day1.weather
    day1_weather.Size = 30
    day1_weather.Rgb = white
    day1_weather.Coords = X_1, Y_15
    day1_weather.Display_Update()

    day1_wind = GameText()
    day1_wind.Text = day1.wind
    day1_wind.Size = 30
    day1_wind.Rgb = white
    day1_wind.Coords = X_1, Y_16
    day1_wind.Display_Update()

    day1_temperature = GameText()
    day1_temperature.Text = day1.temperature
    day1_temperature.Size = 30
    day1_temperature.Rgb = white
    day1_temperature.Coords = X_1, Y_17
    day1_temperature.Display_Update()

    # -------------------------------2
    day2_date = GameText()
    day2_date.Text = day2.date
    day2_date.Size = 30
    day2_date.Rgb = white
    day2_date.Coords = X_2, Y_14
    day2_date.Display_Update()

    day2_weather = GameText()
    day2_weather.Text = day2.weather
    day2_weather.Size = 30
    day2_weather.Rgb = white
    day2_weather.Coords = X_2, Y_15
    day2_weather.Display_Update()

    day2_wind = GameText()
    day2_wind.Text = day2.wind
    day2_wind.Size = 30
    day2_wind.Rgb = white
    day2_wind.Coords = X_2, Y_16
    day2_wind.Display_Update()

    day2_temperature = GameText()
    day2_temperature.Text = day2.temperature
    day2_temperature.Size = 30
    day2_temperature.Rgb = white
    day2_temperature.Coords = X_2, Y_17
    day2_temperature.Display_Update()

    day3_date = GameText()
    day3_date.Text = day3.date
    day3_date.Size = 30
    day3_date.Rgb = white
    day3_date.Coords = X_3, Y_14
    day3_date.Display_Update()

    day3_weather = GameText()
    day3_weather.Text = day3.weather
    day3_weather.Size = 30
    day3_weather.Rgb = white
    day3_weather.Coords = X_3, Y_15
    day3_weather.Display_Update()

    day3_wind = GameText()
    day3_wind.Text = day3.wind
    day3_wind.Size = 30
    day3_wind.Rgb = white
    day3_wind.Coords = X_3, Y_16
    day3_wind.Display_Update()

    day3_temperature = GameText()
    day3_temperature.Text = day3.temperature
    day3_temperature.Size = 30
    day3_temperature.Rgb = white
    day3_temperature.Coords = X_3, Y_17
    day3_temperature.Display_Update()

    Update_Time_text = GameText()
    Update_Time_text.Text = "更新时间："
    Update_Time_text.Size = 20
    Update_Time_text.Rgb = white
    Update_Time_text.Coords = 1100, Y_16
    Update_Time_text.Display_Update()

    Update_Time_date = GameText()
    Update_Time_date.Text = Time_Data
    Update_Time_date.Size = 20
    Update_Time_date.Rgb = white
    Update_Time_date.Coords = 1100, Y_17
    Update_Time_date.Display_Update()

    pygame.display.update()  # 更新显示

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_f:
                full_screen = not full_screen
                if full_screen:
                    GameScreen = pygame.display.set_mode(ScreenSize, FULLSCREEN, 32)
                    pygame.display.update()  # 更新显示
                    print("全屏")
                else:
                    GameScreen = pygame.display.set_mode(ScreenSize, RESIZABLE, 32)
                    pygame.display.update()  # 更新显示
                    print("默认大小")
            if event.key == K_q:
                Thread1_flg = 0
                t1.join()
                print("已结束")
                exit()