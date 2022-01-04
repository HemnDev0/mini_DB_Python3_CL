#This project was created by Hemn Ahmed 
#Computer Science Student at The University of Sulaymaniyah.
# completed at 11/15/2021 
#...............................................................................
#Create a python program that work with txt file:
#create mini database using file for student grading system
#input name of student with their grade
#number of student is 10
#subject is:
#Database
#AI
#Security
#Web Programming
#Graphics
#Computation
#program must ask user to choose 
#1- for input new student and his grades
#2- for show All Student information
#3- for show specific student




choose=int(input("1-for input new student and his grades \n2-for show All Student information\n3- for show specific student\n"))
subj=["Database","AI" , "Security" , "Web programming" , "Graphics", "Computation"]
arr=["","","","","","",""]
b=True
def process(num):
    if num==1:
        f=open("db.txt" ,"a")
        name=input("Full Name : " )
        f.write(name+":")
        f.write("\n")
        i=0
        while i<len(subj):
            grade=int(input("Your Grade for "+subj[i]+" : " ))
            if grade>=0 and grade<101:
                if i==5:
                    arr[i]=(subj[i]+"&"+str(grade))
                else:
                    arr[i]=(subj[i]+"&"+str(grade))
                    #f.write(subj[i]+"&"+str(grade))
                    #f.write("\n") 
                i+=1
            else:
                print("Please Input correct grade !!!")
                i=0
                b=False
                while i<len(arr):
                    arr[i]=""
                    i+=1
                break
        for i in arr:
            f.write(i)
            f.write("\n")
        f.close()
    
    if num==2:
        f=open("db.txt" ,"r")
        print(f.read())
        f.close()
    if num==3:
        name=input("Specific student name: ")
        lines = []
        with open('db.txt') as f:
            lines = f.readlines()
        
        
        for index, line in enumerate(lines):
            if name in line:
                print("found it")
                #print(lines[len(line)])
                i=index
                while i<index+7:
                    print(lines[i])
                    i+=1
            
        
        
process(choose)      

