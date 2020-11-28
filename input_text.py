#!/usr/bin/python3
import text_to_Morse as ttM

def input_text(text):
    text = text.upper()
    table = list(text)
    ttM.convert_table_to_Morse(table)
