import multiprocessing
from multiprocessing import Process
import threading
from threading import Lock
import webview
import os
import signal

# from flask import Flask, jsonify
from flask import Flask, render_template, session, request, copy_current_request_context, jsonify, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from flask_cors import CORS


app = Flask(__name__, static_folder='static')
app.config.from_object(__name__)

DEBUG = True
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong33!')


@app.route('/')
def index():
    return app.send_static_file('index.html')
    # return send_from_directory(app.static_folder, 'index.html')


@app.route("/<path:fallback>")
def fallback(fallback):
    if fallback.startswith('css/') or fallback.startswith('js/') \
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


def run_flask():
    app.run()


def run_webview():
    webview.create_window('pyweb测试', 'http://127.0.0.1:5000')  # 创建浏览器窗口

    # webview.create_window('pyweb测试', 'http://www.yono233.cn')  # 创建浏览器窗口
    webview.start()  # 启动 pywebview
