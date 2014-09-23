import gevent,time
import random
def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)
def synchronous():
    for i in range(1,10):
        task(i)
def asynchronous():
    threads = [gevent.spawn(task,i) for i in xrange(10)]
    print type(threads)
    gevent.joinall(threads)
Curtime = time.time()

print ('Synchronous')
#synchronous()
#print time.time() - Curtime
#print ('Asynchronous:')
asynchronous()
print time.time() - Curtime

