subject=[95,25,70,95,90]
sum=0
fail=0
for marks in subject:
    print(marks)
    sum=sum+marks
    print(sum)
    print (len(subject))
    avg=sum/len((subject))
    print(avg)
    if avg>=70:print ("pass")
    if marks<40:fail=1
    if fail==1:print("fail")


    