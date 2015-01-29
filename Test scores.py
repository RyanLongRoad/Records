#Ryan Cox
#29/01/15
#Store and display students test scores



#Blue print

class studentMarks:

    def __init__(self):
        self.testScore = "-"
        self.studentName = "-"


#main program

def create_record():
    new_studentMarks = studentMarks

def enter_enformation():

    studentMarks.studentName = input("Enter the student's name: ")    
    studentMarks.testScore = int(input("Enter the test score: "))

    scores = []

    scores.append(studentMarks)

    return scores

def disply(scores):
    for each in scores:
        print("The student {0} got the test score of {1}".format(studentMarks.studentName,studentMarks.testScore))

create_record()
scores = enter_enformation()
disply(scores)
