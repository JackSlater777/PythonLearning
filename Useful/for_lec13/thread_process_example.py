import threading


def fun():
    global status
    print(f"{status} in process {__name__}")
    status = "Ready"
    print(f"{status} in process {__name__}")


status = "Not ready"

if __name__ == "__main__":
    t = threading.Thread(target=fun, args=())
    t.start()
    t.join()

    print(f"{status} in process {__name__}")
