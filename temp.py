import random
Temp=[]
highest_temp_day=""
for i in range(7):
	Temp.append(random.randint(26,40))
daysoftheweek=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
for a in range(7):
	print(daysoftheweek[a]+": "+str(Temp[a]))
	
good_day_count=0
for tempreture in range(7):
	if Temp[tempreture]%2==0:
		good_day_count+=1 
		print(daysoftheweek[tempreture])
print("Shelly has "+ str(good_day_count)+" good day")
highest_temp=Temp[0]
lowest_temp=Temp[2]
highest_temp_day=daysoftheweek[0]
for w in range(7):
	if Temp[w]>highest_temp:
		highest_temp=Temp[w]
		highest_temp_day=daysoftheweek[w]
	
print("the highest temperature of the week was "+ str(highest_temp)+ "on"+ highest_temp_day)


for z in range(7):
	if Temp[z]>lowest_temp:
		lowest_temp=Temp[z]
		lowest_temp_day=daysoftheweek[z]
print("the lowest temperature of the week was "+ str(lowest_temp)+ "on"+ lowest_temp_day)
sum=0
for k in range(7):
	sum += Temp[k]

avg=sum/7
print("the average temparature is "+ str(avg))

for e in range(7):
	if Temp[e]>avg:
		print(Temp[e])


