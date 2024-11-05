from backend.func import *

if __name__ == '__main__':
    multiprocessing.freeze_support()

    flask_process = Process(target=run_flask)
    flask_process.start()

    webview_process = Process(target=run_webview)
    webview_process.start()

    webview_process.join()
    os.kill(flask_process.pid, signal.SIGTERM)