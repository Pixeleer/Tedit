import os
import requests
import turtle
import base64

server = open("current_server.txt", "r").read()
defualt_port = "36676"

port_check = server.split(":")
if len(port_check) == 1:
    server = server+":"+defualt_port

if server.startswith("http://") or server.startswith("https://") != True:
    server = "http://"+server

cmd = input("WIP Editor >> ")
cmd_parts = cmd.split(" ")

if cmd_parts[0] == "post":
    if os.path.exists(cmd_parts[1]+".tlvl") != True:
        print("Level doesn't exist.")
        os.system("pause")
        exit()

    print("Contacting server....")
    try:
        data = open(cmd_parts[1]+".tlvl", "r").read()
        message_bytes = data.encode('ascii')
        b64encoded_temp = base64.b64encode(message_bytes)
        b64encoded = b64encoded_temp.decode("ascii")

        r = requests.post(server+"/postlevel/"+cmd_parts[1]+"/"+b64encoded)

        print(r.text)
        os.system("pause")
    except Exception as e:
        print("Connection to the server failed. Contact the server host if this persists.\n"+str(e))
        os.system("pause")

if cmd_parts[0] == "get":
    if os.path.exists(cmd_parts[1]+".tlvl") == True:
        print("Level already downloaded.")
        os.system("pause")
        exit()

    print("Contacting server....")
    try:
        r = requests.get(server+"/getlevel/"+cmd_parts[1])

        l = open(cmd_parts[1]+".tlvl", "wb")
        l.write(r.content)
        l.close()

        print("Downloaded from server.")
        os.system("pause")
    except:
        print("Connection to the server failed. Contact the server host if this persists.")
        os.system("pause")
    