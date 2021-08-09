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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11,]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
