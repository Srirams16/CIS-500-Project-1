#######################################################
# my_date
#
# Name: saiteja sriram 
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False 
print(is_leap_year(2000))               
pass
 
 
 
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    dates_per_month = [0,31,59,90,120,151,181,212,243,273,304,334]
    
    if is_leap_year(year):
        dates_per_month[2] = 60
    
    if month == 1:
        return day
    else:
        return dates_per_month[month - 1] + day
print(ordinal_date(2023, 1, 2))        
pass



def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    O1 = ordinal_date(year1, month1, day1)
    O2 = ordinal_date(year2, month2, day2)
    ord_difference = O2 - O1
    return ord_difference
print(days_elapsed(2023,9,19,2023,11,16))
pass

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    
    
    if is_leap_year(year):
        days_between = days_elapsed(1753,1,1,year,month,day)
        res = (days_between % 7) + 1
        
    else:
        days_between = days_elapsed(1753,1,1,year,month,day)
        res = (days_between % 7)
    return DAYS_OF_WEEK[res]


print(day_of_week(2023,9,29))
    
given_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']    
def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    
    test_day = day_of_week(year, month, day)
    return f"{test_day}, {day:02d} {given_months[month - 1]} {year}"
print(to_str(2023,9,29)) 
pass
              
   