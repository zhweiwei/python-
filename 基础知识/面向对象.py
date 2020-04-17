from multiprocessing import Process
import os

def run_proc(name):
    print("%s  %s" %(name,os.getpid()))

if __name__== "__main__":
    print("parent %s" % os.getpid())

    p =Process(target=run_proc,args=("test",))
    print("will start")
    p.start()
    p.join()
    print("end")