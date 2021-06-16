def add_time(start, duration,day=""):
  #Break start into 24 hr time
  start_time=start.split()
  twenty_four_start=start_time[0].split(":")
  #Convert start times to int
  twenty_four_start[0]=int(twenty_four_start[0])
  twenty_four_start[1]=int(twenty_four_start[1])
  if start_time[1]=="PM":
    twenty_four_start[0]+=12
  #Break duration into int array
  time_added=duration.split(":")
  time_added[0]=int(time_added[0])
  time_added[1]=int(time_added[1])
  #add the times
  new_time=[]
  new_time.append(twenty_four_start[0]+time_added[0])
  new_time.append(twenty_four_start[1]+time_added[1])
  #Handle over 60 min
  new_time[0]+=new_time[1]//60
  new_time[1]%=60
  #Handle over 24 hours
  days_past=new_time[0]//24
  new_time[0]%=24
  #convert back into 12 hr time as string
  time_output=""
  #Handle noon and midnight
  if new_time[0]%12 == 0:
    time_output+="12"
  else:
    time_output+=str(new_time[0]%12)
  time_output+=":"
  #handle 0-9 minutes
  if new_time[1]<10:
    time_output+="0"+str(new_time[1])
  else:
    time_output+=str(new_time[1])
  #Handle AM/PM  
  if new_time[0]<12:
    time_output+=" AM"
  else:
    time_output+=" PM"
  #Handle named days
  if day!="":
    #Make a list of days to act as an Enum
    list_days=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
    #convert day to uppercase to avoid case sensitivity
    start_day=day.upper()
    #use our list to convert day into an int
    for count, DAY in enumerate(list_days):
      if start_day == DAY:
        start_day=count
        break
    #Add the days past to the start day
    current_day=start_day+days_past
    #Handle more than 7 days
    current_day%=7
    #convert back into a string
    for count, DAY in enumerate(list_days):
      if current_day==count:
        current_day=DAY.capitalize()
        break
    #adds comma, space and current_day
    time_output+=", "+current_day
  #Handle if a day has passed
  if days_past>0:
    #Handle next day
    if days_past ==1:
      time_output+=" (next day)"
    else:
      time_output+=" ("+str(days_past)+" days later)"

  return time_output
