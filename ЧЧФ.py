def human_read_format(size):
    if 0 <= size <= 2 ** 10:
        return f"{round(size)}Б"
    elif 2 ** 10 < size <= 2 ** 20:
        return f"{round(size / 2 ** 10)}КБ"
    elif 2 ** 20 < size <= 2 ** 30:
        return f"{round(size / 2 ** 20)}МБ"
    elif 2 ** 30 < size <= 2 ** 40:
        return f"{round(size / 2 ** 30)}ГБ"
    elif 2 ** 40 < size <= 2 ** 50:
        return f"{round(size / 2 ** 40)}ТБ"
    elif 2 ** 50 < size <= 2 ** 60:
        return f"{round(size / 2 ** 50)}ПБ"
    elif 2 ** 60 < size <= 2 ** 70:
        return f"{round(size / 2 ** 60)}ЭБ"
