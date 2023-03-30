# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода
# внутри него.
import time


class MyCtxManager:
    def __enter__(self):  # Выполняется перед кодом, который обернут
        print("Hello")
        self.t = time.time()  # Это старт таймера

    def __exit__(self, exc_type, exc_val, exc_tb):  # Выполняется после кода, который обернут
        # Код внутри exit выполнится всегда, даже если выбросится исключение перед ним
        print(f"Time spent: {time.time() - self.t}")  # Это время, потраченное на вычисления
        print("Bye")


with MyCtxManager():  # Обертка
    print("Some code should be here")
