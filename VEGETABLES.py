vegetables=["ONION","CHILLI","POTATO","BRINJAL","OKRA"]
print(vegetables[0])
print(vegetables[1:3])
vegetables[3]="TOMATO"
print(vegetables)
cordinates=("223265.00, 5236656.23", "2236546.00,5565332.00","225879.69,55.123658.08")
print(cordinates[1])
my_data={"Name": "AJMAL USMAN","AGE":"32","MARRIED":"YES","No.of KIDS": "1","Address":"Remraam,Dubailand,PO Box 112365"}
print (my_data)
my_data["Name"]="AJMAL RASHID USMAN"
print (my_data)
my_data.get("Name")
print(my_data.get("Name"))
print(my_data["Name"])
subjects=[85,90,85,40,92]
sum=0
fail=0
for item in subjects:
    print(item)
    if item<45:
        fail=1
    sum=sum+item
print (sum)
print(len(subjects))
avg=sum/len(subjects)
print(avg)
print (fail)
if fail==1:
    print("Fail")
elif avg>=75:
    print("distiction")
else:
    print("Pass")
    
mark_cutoff=45
