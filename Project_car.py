from typing import ForwardRef


mycar={"Cost":100000,
"Age":5,
"Brand":"Honda",
"milege":[12,15,5],
"Topspeed":158,
"Accidents":4,
"4WD":True,
"D_pattern":[10,10,50]
}
fuel=10
A=mycar["milege"]
B=mycar["D_pattern"]
fuel_per_km=(B[0]/A[0])+(B[1]/A[1])+(B[2]/A[2])
print(fuel_per_km)
x=fuel_per_km*fuel
print(x)
#insurance=[1000]
#total_expense=[X]+[insurance]
#print(total_expense)
Vehicles={"Veh_sec1":["BMW","Mercedes","Tesla","Jaguar"],
"Veh_Sec2":["Toyoa","Mitsubishi","Honda"],
"Veh_Sec3":["KIA","Hyundai","Ford"]}
for Dep in Vehicles["Veh_sec1"]:
    if Dep==mycar["Brand"]:
        rate_of_dep=30
for dep2 in Vehicles["Veh_Sec2"]:
    if dep2==mycar["Brand"]:
        rate_of_dep=20
for dep3 in Vehicles["Veh_Sec3"]:
    if dep3==mycar["Brand"]:
        rate_of_dep=10
print(rate_of_dep)
Dep_max_value=mycar["Cost"]-10000
Current_car_value=Dep_max_value-(mycar["Age"]*Dep_max_value/rate_of_dep)
print(Current_car_value)
insurance=800
if mycar["Topspeed"]>=100 and mycar["Topspeed"]<=140:
    Current_insurace_cost =  insurance+Current_car_value*(2/100)
if mycar["Topspeed"]>140 and mycar["Topspeed"]<=200:
    Current_insurace_cost =  insurance+Current_car_value*(4/100)
if mycar["Topspeed"]>200:
    Current_insurace_cost =  insurance+Current_car_value*(6/100)
if mycar["Accidents"]==0:
    Current_insurace_cost=Current_insurace_cost-(Current_insurace_cost)*(10/100)
if mycar["Accidents"]>=1 and mycar["Accidents"]<=3:
    Current_insurace_cost=Current_insurace_cost+(Current_insurace_cost)*(15/100)
if mycar["Accidents"]>3:
    Current_insurace_cost=Current_insurace_cost+(Current_insurace_cost)*(30/100)
SUM=0
for list in mycar["D_pattern"]:
    SUM=SUM+list
offroad_percentage=SUM*40/100
if mycar["4WD"]==True and B[2]>offroad_percentage:
    Current_insurace_cost=Current_insurace_cost+(Current_insurace_cost)*(20/100)
print(Current_insurace_cost)












    

