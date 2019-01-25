# coding: utf-8
# Sample to draw graph values acquired with 2SMPD-02E.

from __future__ import print_function

import time
import datetime

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

import grove_2smpb_02e

sensor = grove_2smpb_02e.Grove2smpd02e()

COLOR_RED = 'tab:red'
COLOR_BLUE = 'tab:blue'

def main():
    plt.ion()
    fig, ax1 = plt.subplots()
    
    plt.title('2SMPD-02E Demo')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Pressure[hPa]', color=COLOR_BLUE)
    ax2 = ax1.twinx()
    ax2.set_ylabel('Temperature[degree]', color=COLOR_RED)

    formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
    ax1.yaxis.set_major_formatter(formatter)
    ax2.yaxis.set_major_formatter(formatter)

    pressList = []
    tempList = []
    timeList = []
    
    print ("start")
    
    while True:
        try:
          press, temp = sensor.readData()
        except OSError:
          print('Failed to get value.')
          break

        now = datetime.datetime.today()
        pressList.append(press)
        tempList.append(temp)
        timeList.append(now)
        
        ax1.plot(timeList, pressList, color=COLOR_BLUE)
        ax1.tick_params(axis='y', labelcolor=COLOR_BLUE)
        
        ax2.plot(timeList, tempList, color=COLOR_RED)
        ax2.tick_params(axis='y', labelcolor=COLOR_RED)

        plt.gcf().autofmt_xdate()
        myFmt = mdates.DateFormatter('%H:%M:%S')
        plt.gca().xaxis.set_major_formatter(myFmt)
        
        fig.tight_layout()
        fig.canvas.draw()
        plt.show()

        print(datetime.datetime.today().strftime("[%Y/%m/%d %H:%M:%S]")
                        ,"pressure=%.1f[hPa] temperature=%.1f[degC]" %(press,temp))

if __name__ == '__main__':
  main()
