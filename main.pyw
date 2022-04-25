import threading
from dotenv import load_dotenv
import pystray
from pystray import Icon, Menu, MenuItem
from PIL import Image
from TwitterMain import twmain
import psutil
import os

#.envファイルを読み込み
load_dotenv()

#ブロッカースレッド
blockerThread = threading.Thread(target=twmain.BlockerStart)

#タスクトレイに表示させる関数
def thread_st():
    global icon
    options_map = {'終了': lambda: thread_quit()}

    items = []
    for option, callback in options_map.items():
        items.append(MenuItem(option, callback, default=True if option == 'Show' else False))

    menu = Menu(*items)
    image = Image.open("favicon.ico")
    icon=pystray.Icon("name", image, "PeriodicCheckBlock", menu)
    icon.run()

def thread_quit():
    #自身をタスクキルする
    #ソースから実行してると多分Python自体が終了する
    p = psutil.Process(os.getpid())
    p.kill()

def main():
    #ブロッカースレッドとタスクトレイスレッドを実行
    blockerThread.start()
    threading.Thread(target=thread_st).start()

if __name__ == "__main__":
    main()