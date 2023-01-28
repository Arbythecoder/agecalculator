def my_calculator (year,month,day):
    import datetime
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date (year,month,day)
    age = int((today-date_of_birth).days /365.25)
    print(age)

my_calculator (2016,6,3)

