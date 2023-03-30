class MyCtxManager:
    def __enter__(self):
        print("Hello")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye")


with MyCtxManager():
    x = 100
    y = 200
    print(f"{x + y = }")
