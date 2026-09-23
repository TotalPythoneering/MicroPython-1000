# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: udp_rad_sender.py
# AUTHOR: Randall Nagy
#
import socket

SERVER_IP = '10.0.0.22'
SERVER_PORT = 5050

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = '\n'
while message[0].lower() != 'q':
    try:
        message = input("Message: ")
        if message[0] == 'q':
            continue
        sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
        sock.settimeout(5)
        data, server = sock.recvfrom(1024)
        print("Received from server:", data.decode())
    except socket.timeout:
        print("No response from server, request timed out.")

sock.close()
