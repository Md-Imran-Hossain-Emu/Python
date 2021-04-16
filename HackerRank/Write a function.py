

def is_leap(n):
    year = False
    if n%4==0 and n%100!=0:
        year = True
    elif n%100 == 0 and n%400 == 0 :
        year = True
    return year

year = int(input())

print(is_leap(year))