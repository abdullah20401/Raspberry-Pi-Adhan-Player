from playsound import playsound
import datetime as dt
import time
import requests, json

city = 'chicago'

url = "https://muslimsalat.com/{}/daily/{}.json?key=6b5ff2c1479a28e4db4d82ce90d68a33".format(city, '4')

filename = 'adhan.wav'

def get_prayer():
    
    '''Opens Text File To Store Prayer Timings'''
    prayer_log = open('prayer.txt', 'w+')

    '''Writes The Text File'''
    prayer_log.write(requests.get(url).json()['items'][0]['fajr'].upper()+"\n")
    prayer_log.write(requests.get(url).json()['items'][0]['dhuhr'].upper()+"\n")
    prayer_log.write(requests.get(url).json()['items'][0]['asr'].upper()+"\n")
    prayer_log.write(requests.get(url).json()['items'][0]['maghrib'].upper()+"\n")
    prayer_log.write(requests.get(url).json()['items'][0]['isha'].upper())

    '''Closes The File'''
    prayer_log.close()

    '''Opens The File To Read The Prayer Timings'''
    read = open('prayer.txt', 'r+')

    '''Reads The Text File And Difines It As Prayer'''
    lines = read.readlines()
    
    '''Let The Variable Prayer Be Accessed Outside Of The Function'''
    global prayer
    
    '''Defines The Prayer Variable And Removes The Next Line '''
    prayer = list(map(str.rstrip, lines))

    '''Closes The File'''
    read.close()
    
get_prayer()    
    
while True:
        
    if time.strftime("%-I:%M %p", time.localtime()) == prayer[0]:
        playsound(filename)

    elif time.strftime("%-I:%M %p", time.localtime()) == prayer[1]:
        playsound(filename)

    elif time.strftime("%-I:%M %p", time.localtime()) == prayer[2]:
        playsound(filename)

    elif time.strftime("%-I:%M %p", time.localtime()) == prayer[3]:
        playsound(filename)

    elif time.strftime("%-I:%M %p", time.localtime()) == prayer[4]:
        playsound(filename)
        get_prayer()