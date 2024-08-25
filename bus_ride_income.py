wine_count=0
child_count=0
adult_count=0
passenger_count=0

while passenger_count<20:
    age=int(input())
    if age == 0:
        break
    elif age <18:
        child_count +=1
    else:
        adult_count +=1
    passenger_count +=1
    print("")