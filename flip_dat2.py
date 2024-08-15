def flip_dates(dates):
    """
    На входе:YYYY-MM-DD и на выходе: DD/MM/YYYY
    """
    return list(map(lambda date: f"{date.split('-')[2]}/{date.split('-')[1]}/{date.split('-')[0]}", dates))


dates = ["2002-09-16", "1997-06-03", "1990-12-21"]
result = flip_dates(dates)
print(result)