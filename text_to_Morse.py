#!/usr/bin/python3
import os
import time
duration_short = 0.3
duration_long = 0.8
freq = 1000

dict = {
    "A" : "01",
    "B" : "1000",
    "C" : "1010",
    "D" : "100",
    "E" : "0",
    "F" : "0010",
    "G" : "110",
    "H" : "0000",
    "I" : "00",
    "J" : "0111",
    "K" : "101",
    "L" : "0100",
    "M" : "11",
    "N" : "10",
    "O" : "111",
    "P" : "0110",
    "R" : "010",
    "S" : "000",
    "T" : "1",
    "U" : "001",
    "V" : "0001",
    "W" : "011",
    "X" : "1001",
    "Y" : "1011",
    "Z" : "1100"
}



def convert_table_to_Morse(list):
    for key in list:
        if key in dict.keys():
            beep(dict[key])
            time.sleep(1)
        else:
            time.sleep(2)


def beep(v):
    sign = list(v)
    for a in sign:
        if a == "0":
            os.system('play -nq -t alsa synth {} sine {}'.format(duration_short, freq))
            print(".")
            time.sleep(0.5)
        elif a == "1":
            os.system('play -nq -t alsa synth {} sine {}'.format(duration_long, freq))
            print("-")
            time.sleep(0.5)
