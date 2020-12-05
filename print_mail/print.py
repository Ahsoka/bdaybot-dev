import os, sys
import win32print
import time

p = win32print.OpenPrinter("HP OfficeJet Pro 8020 series [84EFFB]")

job = win32print.StartDocPrinter(p,1,("hi", None, "RAW"))
win32print.StartPagePrinter(p)
with open("hi.txt", 'r') as file:
    lines = file.readlines()
word = ""
for line in lines:
    word = word + line
print(win32print.WritePrinter(p, bytes(str.encode(word))))
win32print.StartDoc(p, (word, word, word, 32))
win32print.StartPage(p)
win32print.EndDocPrinter(p)
# time.sleep(40)
# win32print.EndPagePrinter(p)
# win32print.ClosePrinter(p)
