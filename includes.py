import multiprocessing
from multiprocessing import Process
import threading
from threading import Lock
import webview
import os
import signal

# from flask import Flask, jsonify
from flask import Flask, render_template, session, request, copy_current_request_context, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from flask_cors import CORS
