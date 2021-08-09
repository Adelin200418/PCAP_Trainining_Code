def is_year_leap(year):
 return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if (is_year_leap(year)== False and month==2):
        return 28
    elif (is_year_leap(year)== True and month==2):
        return 29
    elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        return 31
    elif(month<12 and month >1):
        return 30

def day_of_year(year, month, day):
    days=0
    if(days_in_month(year, month)>day):
        days=day
        month-=1
        
    while (month>0):
        print(month,days)
        
        days=days+days_in_month(year,month)
        month-=1
    return days

print(day_of_year(2007, 9, 29))
