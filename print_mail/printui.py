import win32ui
# X from the left margin, Y from top margin
# both in pixels
X=50; Y=50
input_string = "hi there"
multi_line_string = input_string.split(" ")
hDC = win32ui.CreateDC ()
hDC.CreatePrinterDC ("HP OfficeJet Pro 8020 series [84EFFB]")
hDC.StartDoc ("hi.txt")
hDC.StartPage ()
for line in multi_line_string:
     hDC.TextOut(X,Y,line)
     Y += 100
hDC.EndPage ()
hDC.EndDoc ()
