from flask import Flask, redirect, url_for, request, render_template, session, flash, send_file, jsonify
from server_getlevel import server_getlevel
from server_postlevel import server_postlevel
import os
from dotenv import load_dotenv

load_dotenv()

print(" * Launching Tedit Server (Flask)")

try:
    app = Flask(__name__)
    
    UPLOAD_FOLDER = '/svr_levels'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    app.register_blueprint(server_getlevel, url_prefix="/getlevel")
    app.register_blueprint(server_postlevel, url_prefix="/postlevel")

    class svr:
        name = os.environ['SVR_NAME']
        host = os.environ['SVR_HOST']
        debug = os.environ['SVR_DEBUG']
        port_str = os.environ['SVR_PORT']

        port = int(port_str)

    @app.route("/")
    def home():
        return jsonify({"svr_name" : svr.name})

    if __name__ == "__main__":
        if svr.debug == "no":
            app.run(host=svr.host, port=svr.port)
        elif svr.debug == "yes":
            app.run(host=svr.host, debug=True, port=svr.port)
        else:
            print(" * Couldn't read debug setting, starting in non-debug mode.")
            app.run(host=svr.host, port=svr.port)
except Exception as e:
    print(" * The Tedit server has failed. Check the configuration and try again.\n * Traceback: "+str(e))
    os.system("pause")