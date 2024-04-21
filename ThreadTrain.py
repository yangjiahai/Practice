#threading 和_thread模块创建线程
#import ProcessTrain
import os
import threading,time
#ProcessTrain.child_1(5)
def process():
    for i in range(3):
        time.sleep(1)
        print("线程%s:启动了"%(threading.current_thread().name))

if __name__ == '__main__':
    print("主进程开始。")
    threads=[threading.Thread(target=process) for i in range(3)]#列表[]存储线程
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("主进程结束。")