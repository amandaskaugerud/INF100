def will_work(city, salary):
    if (city == 'Bergen' and salary < 400_000) or (city == 'Bodø' and salary < 900_000) :
        return False
    elif (city == 'Bergen' and salary >= 400_000) or (city == 'Bodø' and salary >= 900_000):
        return True
    elif city == 'Verdensrommet':
        return True
    elif salary >= 600_000:
        return True
