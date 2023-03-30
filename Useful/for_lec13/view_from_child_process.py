import multiprocessing


def fun():
    global status
    print(f"{status} in process {__name__}")
    status = "Ready"
    print(f"{status} in process {__name__}")


status = "Not ready"

t = multiprocessing.Process(target=fun, args=())
t.start()
t.join()

print(f"{status} in process {__name__}")

fun()