from flask import Flask, redirect, url_for, request, render_template, session, flash, send_file, jsonify, Blueprint
import os

server_getlevel = Blueprint("server_getlevel", __name__, static_folder="static")

@server_getlevel.route("/<name>")
def get_level(name):
    try:
        return send_file(f"svr_levels/{name}.tlvl")
    except:
        return "That level does not exist on the server."