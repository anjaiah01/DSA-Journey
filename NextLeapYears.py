# Print the next n number of leap years from the given year
#     Example:
#     Input= 2000
#     Output= 2004, 2008, 2012, 2016...
    
def isLeapYear(year):
    if year%400==0 or (year%100!=0 and year%4==0):
        return True 
    return False


def nextLeapYears(year,n):
    leaps=[]
    
    while not isLeapYear(year):
        year+=1
        
    for _ in range(n):
        leaps.append(year)
        year+=4
    return leaps

n=int(input())
year=int(input())
result=nextLeapYears(year,n)
print(result)