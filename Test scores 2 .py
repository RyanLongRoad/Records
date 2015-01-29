#Ryan Cox
#29/01/15
#Store and display students test scores

#Only displays last eneterd student's score and name



#Blue print

class studentMarks:

    def __init__(self):
        self.testScore = "-"
        self.studentName = "-"


#functions

def create_record():
    new_studentMarks = studentMarks

def display(scores):
    for each in scores:
        n = 0
        
        print("The student '{0}' got a test score of {1}".format(studentMarks.studentName, studentMarks.testScore))    

        n = n + 1
        
def enter_enformation():
    
    scores = []

    for count in range(3):

        studentName = input("Enter the student's name: ")    
        testScore = int(input("Enter the test score: "))
        

        studentMarks.studentName = studentName
        studentMarks.testScore = testScore

        scores.append(studentMarks)
        
        
    
    

    return scores



#main program
        
create_record()
scores = enter_enformation()
display(scores)


