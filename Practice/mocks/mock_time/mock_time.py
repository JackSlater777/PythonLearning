# mock_time.py
import datetime


def discount_calculator(value: float, due_date: datetime.date, discount: float, days: int) -> float:
    """
    value - абсолютное значение суммы, с которой хотим получить скидку;
    due_date - та дата, до которой действует скидка;
    discount - размер скидки;
    days - количество дней дедлайна до истечения срока действия скидки.
    """
    # Вычисляем разницу между датой окончания скидки и текущей датой
    diff = due_date - datetime.date.today()
    # Если мы попали в интервал между сегодняшним днем и конечным днем...
    if datetime.timedelta() <= diff < datetime.timedelta(days=days):
        # ... применяем скидку
        return value * (1.0 - discount)
    else:
        return value
