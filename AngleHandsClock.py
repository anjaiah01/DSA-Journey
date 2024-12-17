
def angle(hour,minute):
    h=float(hour%12+float(minute)/60)*30
    m=float(minute)*6
    
    angle=abs(h-m)
    return 360 - angle if angle > 180 else angle

hour=int(input())
minutes=int(input())

angle=angle(hour,minutes)
print(angle)