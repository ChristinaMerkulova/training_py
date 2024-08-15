def flip_dates(dates):
    flip_dates = []

    for date in dates:
        year, month, day = date.split('-')
        flip_date = f"{day}/{month}/{year}"
        flip_dates.append(flip_date)

    return flip_dates
"""
На входе:YYYY-MM-DD и на выходе: DD/MM/YYYY
"""


dates = ["2002-09-16", "1997-06-03", "1990-12-21"]
result = flip_dates(dates)
print(result)