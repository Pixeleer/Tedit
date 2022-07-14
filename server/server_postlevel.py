from flask import Flask, redirect, url_for, request, render_template, session, flash, send_file, jsonify, Blueprint
from werkzeug.utils import secure_filename
import os
import base64

server_postlevel = Blueprint("server_postlevel", __name__, static_folder="static")

@server_postlevel.route("/<name>/<data>", methods=["POST"])
def get_level(name, data):
    try:
        if os.path.exists(f"/svr_levels/{name}.tlvl"):
            return "A level with that name already exists on the server."

        decoded_data = base64.b64decode(data).decode("utf-8")
        print(decoded_data)

        l = open("svr_levels/"+name+".tlvl", "w")
        l.write(decoded_data)
        l.close()

        return "Level has been posted to server."
    except Exception as e:
        return "Failed to post level to server.\nException: "+str(e)