import datetime as dt


def validate_year(year):
    now_year = dt.date.today()
    try:
        year <= now_year.year
    except ValueError:
        (f'Некорректный год {year}')
