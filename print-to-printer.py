import socket

PRINTER_IP_ADDRESS = '192.168.1.87'
PORT = 9100

printer = socket.socket()
printer.connect((PRINTER_IP_ADDRESS, PORT))
# NOTE: This is an unreliable way to print.
# This method of sending data to the printer
# also cause weird printing output.
# You need to do more research on the exact
# way the data should be formatted to print
# as we would normally expect text to be printed.
printer.send(b'Please print this text')
printer.close()
