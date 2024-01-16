#StudentID = 3905185
#Name = Chander Mohan 
#The highest level of my code is DI LEVEL
import sys
#using list of student, challenge, result
students_list = []
challenges_list = []
result_list = []
average_of_students = []
max_attr = None
#define student class
class Student:
    counter = 0
    #constructor for student class
    def __init__(self, ID, NAME=None, TYPE=None, NFINISH=None, NONGOING=None, AVERAGETIME=None):
        self.ID=ID
        self.NAME = NAME
        self.TYPE = TYPE
        self.NFINISH = NFINISH
        self.NONGOING = NONGOING
        self.AVERAGETIME = AVERAGETIME
        Student.counter += 1
    #setter for student data 
    def setData(self, NAME, TYPE, NFINISH, NONGOING, AVERAGETIME):
        self.NAME = NAME
        self.TYPE = TYPE
        self.NFINISH = NFINISH
        self.NONGOING = NONGOING
        self.AVERAGETIME = AVERAGETIME
    #getter for student ID attribute
    def getID(self):
        return self.ID
    #getter for student Name attribute  
    def getName(self):
        return self.NAME
    #getter for student type attribute
    def getType(self):
        return self.TYPE
    #getter for finish attribute
    def getNfinish(self):
        return self.NFINISH
    def getNongoing(self):
        return self.NONGOING
    def getAverageTime(self):
        return self.AVERAGETIME
    


#defining challenge class
class Challenge:
    counter = 0
     #constructor for challenge class
    def __init__(self, ID, NAME=None, WEIGHT=None, NFINISH=None, NONGOING=None, AVERAGETIME=None):
        self.ID=ID
        self.NAME = NAME
        self.WEIGHT = WEIGHT
        self.NFINISH = NFINISH
        self.NONGOING = NONGOING
        self.AVERAGETIME = AVERAGETIME

        Challenge.counter += 1
    #setter for challenge data 
    def setData(self, NAME, TYPE, WEIGHT, NFINISH, NONGOING, AVERAGETIME):
        self.NAME = NAME
        self.TYPE = TYPE
        self.WEIGHT = WEIGHT
        self.NFINISH = NFINISH
        self.NONGOING = NONGOING
        self.AVERAGETIME = AVERAGETIME
    def getID(self):
    #getter for challenge ID attribute
        return self.ID
    def getName(self):
    #getter for challenge Name attribute
        return self.NAME
    def getType(self):
    #getter for challenge type  attribute
        return self.TYPE
    def getWeight(self):
    #getter for weight attribute
        return self.WEIGHT

    def getNfinish(self):
        return self.NFINISH

    def getNongoing(self):
        return self.NONGOING

    def getAverageTime(self):
        return self.AVERAGETIME
    #function using for no of challenges
    def noOfChallenge():
        c=0
        for challenge in challenges_list:
            if challenge.getType()=='S':
                c=c+1
        return Challenge.counter-c, c
    






#defining competition class 
class Competition:
    @staticmethod 
    # read_result function which receives all existing results from text file
    def read_results(file):
        # try block to handle exception
        try:
            file_objct=open(file,"r+")
            lines=file_objct.readline()
            n=0
            while(lines!=""):
                resulltt =[] 
                fields=lines.strip().split(', ')
                
                if fields[0]=='':
                    
                    for i in range(1,len(fields)):
                        challenges_list.append(Challenge(fields[i]))
                else:
                    students_list.append(Student(fields[0]))
                    for j in range(1,len(fields)):
                        if fields[j]=='444' or fields[j]=='TBA' or fields[j]=='tba':
                            fields[j]='--'
                        elif fields[j]=='-1' or fields[j]=='NA' or fields[j]=='x':
                            fields[j]=' '
                        resulltt.append(fields[j])
                    result_list.append(resulltt)
                
                lines=file_objct.readline()
                
                

                n+=1
            file_objct.close()
        except Exception as e:
            print(e)

#read challenge function which receives all existing Challenge from text file
  
    @staticmethod
    def readChallengeData(f):
        # try block to handle exception
        try:
            file_object=open(f,"r+")
            line=file_object.readline()
            while(line!=""):
                field=line.strip().split(', ')
                temp = None
                #using for loop for challenge_list
                for c in range(len(challenges_list)):
                    if (challenges_list[c]).getID()==field[0]:
                        temp=c
                        break
                time = 0
                count = 0
                ncount = 0
                #using for loop for result list 
                for r in result_list:
                    if r[c] == '--':
                        ncount += 1
                    elif r[c] == ' ':
                        continue
                    else:
                        time += float(r[c])
                        count += 1
                time = float(time)/count
                (challenges_list[temp]).setData(field[2], field[1], float(field[3]),int(count),int(ncount),float(time))
                line=file_object.readline()
            file_object.close()

        except Exception as e:
            print(e) 

#read Student function which receives all existing student from text file

    @staticmethod
    def readStudentData(f):
        # try block to handle exception
        try:
            file_object=open(f,"r+")
            line=file_object.readline()
            while(line!=""):
                field=line.strip().split(', ') 
                temp = None
                req=True
                #using for loop for student list 
                for c in range(len(students_list)):
                    if (students_list[c]).getID()==field[0]:
                        temp=c
                        break 
                time = 0 
                count = 0
                ncount = 0
                manC = 0 #mandatory challenge counter
                speC = 0 #special challenge counter
                for i in range(len(result_list[c])):
                    if result_list[c][i] == '--':
                        ncount += 1
                    elif result_list[c][i] == ' ':
                        continue
                    else:
                        if (challenges_list[i]).TYPE == 'M':
                            manC+=1
                        else:
                            speC+=1
                        time += float(result_list[c][i])
                        count += 1
                time = float(time)/count
                m, c = Challenge.noOfChallenge()
                if(m!=manC):
                    req=False
                else:
                    if field[2]=='U' and speC<1:
                        req=False
                    elif field[2]=='P' and speC<2: 
                        req=False

                if req==False:
                    field[1] = '!'+field[1]
                (students_list[temp]).setData(field[1], field[2],int(count),int(ncount),float(time))
                line=file_object.readline()
            file_object.close() 
        except Exception as e:
            print(e) 
    
#For disply the results in a given format 
    @staticmethod 
    def competition_dashboard():
        #open competition_report.txt
        r = open('competition_report.txt','w')
        ogOut = sys.stdout
        sys.stdout = r
        print()
        print('COMPETITION DASHBOARD') 
        
        print(('+'+('-'*12))*6+'+') 
        
        sys.stdout.write('|  Results   ') 
        
        #Check the challenge in the challenge list 
        for challenge in challenges_list:
            
            input1='|'+f"{challenge.getID():^12}" 
            
            sys.stdout.write(input1) 
            
        sys.stdout.write('|')  
         
        print()
        print(('+'+('-'*12))*6+'+')        
        #get each line from file
        for i in range(len(students_list)):
            input1='|'+f"{(students_list[i]).getID():^12}"
            sys.stdout.write(input1)
            for record in result_list[i]:
                input1='|'+f"{record:^12}"
                sys.stdout.write(input1)
            sys.stdout.write('|')
            print()
        print(('+'+('-'*12))*6+'+')
        #printing the data of student and the challenges 
        print('There are',Student.counter,'students and',Challenge.counter,'challenges')
        #checking records in the result_list 
        for records in result_list:
            count=0
            values=0
            for record in records:
                if record==' ' or record=='--':
                    pass
                else:
                    count+=1
                    values+=float(record)
                    
        #getting the top student with the average time    
            average_of_students.append(round(values/count,2))
        index=average_of_students.index(min(average_of_students))   
        print('The top student is',(students_list[index]).getID(),'with an average time of ',min(average_of_students),'minutes.')
        if len(sys.argv)>2:
            Competition.challenge_information()
            if len(sys.argv)>3:
                Competition.student_information()
        r.close()
        sys.stdout = ogOut
        with open('competition_report.txt', 'r') as r:
            print(r.read())
#get the information of challenges
    @staticmethod 
    def challenge_information():
        print()
        print("CHALLENGE INFORMATION")
        print(('+'+('-'*16))*6+'+')
        #using for loop for using the challenge attribute 
        for i in ['Challenge','Name','Weight','Nfinish','Nongoing','AverageTime']:
            
            input1='|'+f"{i:^16}"
            
            sys.stdout.write(input1)
            
        sys.stdout.write('|')
        print()
        print(('+'+('-'*16))*6+'+')
        #Using for loop for challenge list for input 
        for i in range(len(challenges_list)):
            input1='|'+f"{(challenges_list[i]).getID():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(challenges_list[i]).getName()+'('+(challenges_list[i]).getType()+')':^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(challenges_list[i]).getWeight():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(challenges_list[i]).getNfinish():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(challenges_list[i]).getNongoing():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(challenges_list[i]).getAverageTime():^16.3}"
            sys.stdout.write(input1)
            sys.stdout.write('|')
            print()
        print(('+'+('-'*16))*6+'+')
        max_time=0
        for c in challenges_list:
            if c.AVERAGETIME>max_time:
                max_time=c.AVERAGETIME
                max_id = c.ID
        #print the difficult challenge with the average time 
        print("The most difficult challenge is Vote ("+max_id+") with an average time of",'%.2f'%max_time,"minutes.")
        print("Report competition_report.txt generated!")

    # Using student_information function  for student information 
    @staticmethod 
    def student_information():
        print()
        print("STUDENT INFORMATION")
        print(('+'+('-'*16))*6+'+')
        #Using for loop for student class  attribute 
        for i in ['StudentID','Name','Type','Nfinish','Nongoing','AverageTime']:
            
            input1='|'+f"{i:^16}"
            
            sys.stdout.write(input1)
            
        sys.stdout.write('|')
        print()
        print(('+'+('-'*16))*6+'+')
        #input all the student data in txt file 
        for i in range(len(students_list)):
            input1='|'+f"{(students_list[i]).getID():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(students_list[i]).getName():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(students_list[i]).getType():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(students_list[i]).getNfinish():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(students_list[i]).getNongoing():^16}"
            sys.stdout.write(input1)
            input1='|'+f"{(students_list[i]).getAverageTime():^16.4}"
            sys.stdout.write(input1)
            sys.stdout.write('|')
            print()
        print(('+'+('-'*16))*6+'+')
        min_time=(students_list[0]).AVERAGETIME
        for c in students_list:
            if c.AVERAGETIME<min_time:
                min_time=c.AVERAGETIME
                min_inst = c
        #display student fastest average time 
        print("The the student with fastest average time is "+min_inst.ID+" ("+min_inst.NAME+") with an average time of",'%.2f'%min_time,"minutes.")
        print("Report competition_report.txt generated!")
        
    
#using main function for call all the data and competition dashboard 
def main():
    if len(sys.argv) < 2:
        print('[usage:] '+sys.argv[0]+' <result file>')
        sys.exit(1)

    compi = Competition()
    compi.read_results(sys.argv[1])
    if len(sys.argv)>2:
        compi.readChallengeData(sys.argv[2])
        if len(sys.argv)>3:
            compi.readStudentData(sys.argv[3])
    compi.competition_dashboard()


if __name__ == '__main__':
    main()
