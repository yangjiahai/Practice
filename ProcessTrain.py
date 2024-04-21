import multiprocessing
#from multiprocessing import Process
import os,time
from multiprocessing import Pool,Process

'''
进程是操作系统的一个程序
create process的方式有os.fork() multiprocess模块和Pool


#multiprocess Process
def test():
    print('我是子进程')

def main():
    p = multiprocessing.Process(target=test, args=())
    p.start()
    print('我是主进程')
'''

def child_1(interval):
    print("p1进程：%s,父进程%s" % (os.getpid(),os.getpid()))
    t_start = time.time()   #开始
    time.sleep(interval)
    t_end = time.time() #结束
    print('p1进程：%s执行时间%s' % (os.getpid(),t_end-t_start))

def child_2(interval):
    print("p2进程：%s,父进程%s" % (os.getpid(),os.getpid()))
    t_start = time.time()  # 开始
    time.sleep(interval)
    t_end = time.time()  # 结束
    print('p2进程：%s执行时间%s' % (os.getpid(), t_end - t_start))

if __name__ == '__main__':
    print('父进程的pid:%s'%os.getpid())
    #Process([group[,target[,name[,args[,kwargs]]]])
    p1=multiprocessing.Process(target=child_1, args=(1,),name="Python-1")
    p2=multiprocessing.Process(target=child_2, args=(2,))
    p1.start()
    p2.start()
    print('p1的进程：%s'%p1.name)
    print('p2的进程：%s'%p2.name)
    print('p1的pid：%s'%p1.pid)
    print('p2的pid：%s'%p2.pid)
    print("等待子进程......")
    p1.join()
    p2.join()

'''
2.可以用继承Process类的方式来创建进程
class subProcess(Process):
3.假如需要上百进程，可以使用Pool进程池
'''
