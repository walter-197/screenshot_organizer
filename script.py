import os 
import shutil
from datetime import date, datetime, time

#The Home directory where screenshots will be stored initially and where action will take place
home_dir= "/Users/username/Desktop/Screenshots"

#directory path to the folders where screenshots need to be transferred
dir_one = "/Users/username/Desktop/subject_1/screenshots"              #subject 1 
dir_two = "/Users/username/Desktop/subject_2/screenshots"            #subject 2 
dir_three = "/Users/username/Desktop/subject_3/screenshots"                 #subject 3 
dir_four = "/Users/username/Desktop/subject_4/screenshots"               #subject 4 
dir_five = "/Users/username/Desktop/subject_5/screenshots"                 #subject 5 


#time to compare
class_one_start = time(12,00,00) 
class_one_end = time(14,00,00)
class_two_start = time(15,00,00)
class_two_end = time(17,00,00)
class_three_start = time(18,00,00)
class_three_end = time(20,00,00)

#date after it starts comparing 
start_date = date(2021,1,1)

#listing the content of home directory
files = os.listdir(home_dir)

#main loop to select the name of each file and then convert it to datetime object and then compare it to the class time 
for file in files:
    if file.endswith(".png"): #mainly to check for .ds store file that is present 
        date_time = datetime.strptime(file, "Screenshot %Y-%m-%d at %I.%M.%S %p.png")   #converting the name of the file to a datetime object
        only_time = date_time.time() # selecting only the time
        day = date_time.strftime("%A") #selecting the day of the week from the datetime object
        if datetime.date(date_time) > start_date:
            if (only_time > class_one_start and only_time < class_one_end and day == "Monday") or (only_time > class_two_start and only_time < class_two_end and day =="Tuesday" ): # subject 1 
                print("subject 1")
                shutil.move(home_dir+"/"+file,dir_one+"/"+file)
            elif (only_time > class_two_start and only_time < class_two_end and day == "Monday") or (only_time > class_two_start and only_time < class_two_end and day =="Friday" ): # subject 2 
                print("subject 2 ")
                shutil.move(home_dir+"/"+file,dir_two+"/"+file)
            elif (only_time > class_one_start and only_time < class_one_end and day == "Tuesday") or (only_time > class_one_start and only_time < class_one_end and day =="Thursday" ): # subject 3 
                print("subject 3")
                shutil.move(home_dir+"/"+file,dir_three+"/"+file)
            elif (only_time > class_one_start and only_time < class_one_end and day == "Wednesday") or (only_time > class_one_start and only_time < class_one_end and day =="Friday" ): # subject 4 
                print("subject 4")
                shutil.move(home_dir+"/"+file,dir_four+"/"+file)
            elif (only_time > class_one_start and only_time < class_one_end and day == "Saturday") or (only_time > class_two_start and only_time < class_two_end and day =="Wednesday" ): # subject 5 
                print("subject 5")
                shutil.move(home_dir+"/"+file,dir_five+"/"+file)
            else:
                pass
                #print("Time not bound") --- for screenshots not in the time frame
        else:
            #print("Error") --- for any png images that are not screenshots 
            pass
    
    else:
        #print(file)
        #print("File not compatible") #mainly for .ds store file 
        pass

