import datetime
import datetime as dt
now = datetime.now() 
dt_time = now.strftime ("%H:%M:%S")
dt_date = now.strftime("%d/%m/%Y")
print("Date : ", dt_date)
print("Time : ",dt_time)
