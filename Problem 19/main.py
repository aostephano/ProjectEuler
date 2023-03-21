def IsLeapYear(year):
    isCentury = False if (year%100 > 0) else True #have remainder with 10 and 100
    if isCentury:
        if year%400 == 0:
            return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False

leapYearList = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000]

for year in leapYearList:
    if not IsLeapYear(year):
        print(year)

# sundayCount = 0
# dayCount = 0
#
# #How many sundays have from 1901 to 2001
# for year in range(1901, 2001):
#     print("Year:", year)
#     for day in range(1, 367 if IsLeapYear(year) else 366):
#         dayCount += 1
#         # if year == 1910 and day == 360:
#         #     pass
#         if dayCount%7 == 0:
#             sundayCount += 1

normalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundayCount = 0
totalDayCounter = 0
sundayDayList = []

for year in range(1901, 2001):
    dayMonthYear = leapYear if IsLeapYear(year) else normalYear
    monthCounter = 0

    for dayCountByMonth in dayMonthYear:
        monthCounter += 1 #jan(1)/fev(2)/...
        for day in range(1, dayCountByMonth+1):
            totalDayCounter += 1
            if totalDayCounter%7 == 0 and day == 1:
                if totalDayCounter != 0:
                    sundayCount += 1
                    sundayDayList.append([day, monthCounter, year])



print(totalDayCounter)
for data in sundayDayList:
    print(data)
print(sundayCount-1) ##Hardcode, but removing 0%7 == 0


