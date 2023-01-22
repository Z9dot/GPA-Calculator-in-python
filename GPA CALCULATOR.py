dash = '-'
print("*****", dash * 10, "*****\n")

print("Welcome to GPA Calculator.\n")

print("*****", dash * 10, "*****\n")


def Quiz_Marks():
    print(dash * 10)

    print("\nQuiz Marks:\n")

    count = int(input("Enter Number of Quizes:"))

    Obtained_Marks = [0] * count

    Total_Marks = [0] * count

    Number = [0] * count

    count = count - 1

    i = 0

    Obtained_Quiz_Marks = 0

    Total_Quiz_Marks = 0

    while i <= count:

        print("Marks Obtained in Quiz", i + 1, ":")

        Obtained_Marks[i] = eval(input())

        print("Total Marks of Quiz", i + 1, ":")

        Total_Marks[i] = eval(input())

        if Obtained_Marks[i] <= Total_Marks[i]:

            Obtained_Quiz_Marks = Obtained_Quiz_Marks + Obtained_Marks[i]

            Total_Quiz_Marks = Total_Quiz_Marks + Total_Marks[i]

            i = i + 1

        else:

            print("You Have Entered Wrong Marks\nEnter Marks Again")
            i = i

    c = 1

    while c == 1:

        Quiz_Marks.Quiz_Weightage = int(input("\nEnter Weightage of Quiz in Final Result:"))

        if Quiz_Marks.Quiz_Weightage >= 1 and Quiz_Marks.Quiz_Weightage <= 100:

            Quiz_Marks.Final_Quiz_Marks = ((Obtained_Quiz_Marks / Total_Quiz_Marks) * Quiz_Marks.Quiz_Weightage)

            print("\nYour Final Quiz Marks Are:", round(Quiz_Marks.Final_Quiz_Marks, 2))

            c = c + 1

        else:

            print("You Entered Wrong Percentage.\nEnter Correct Percentage.")

            c = c


def Assignment_Marks():
    print(dash * 10)

    print("\nAssignment Marks:")

    count = int(input("\nEnter Number of Assignments:"))

    Obtained_Marks = [0] * count

    Total_Marks = [0] * count

    count = count - 1

    i = 0

    Obtained_Assignment_Marks = 0

    Total_Assignment_Marks = 0

    while i <= count:

        print("Marks Obtained in Assignment", i + 1, ":")

        Obtained_Marks[i] = eval(input())

        print("Total Marks of Assignment", i + 1, ":")

        Total_Marks[i] = eval(input())

        if Obtained_Marks[i] <= Total_Marks[i]:

            Obtained_Assignment_Marks = Obtained_Assignment_Marks + Obtained_Marks[i]

            Total_Assignment_Marks = Total_Assignment_Marks + Total_Marks[i]

            i = i + 1

        else:

            print("You Have Entered Wrong Marks\nEnter Marks Again")
            i = i

    c = 1

    while c == 1:

        Assignment_Marks.Assignment_Weightage = int(input("\nEnter Weightage of Assignment in Final Result:"))

        if 0 < Assignment_Marks.Assignment_Weightage <= 100:

            Assignment_Marks.Final_Assignment_Marks = (Obtained_Assignment_Marks / Total_Assignment_Marks) * Assignment_Marks.Assignment_Weightage

            print("\nYour Final Assignment Marks Are:", round(Assignment_Marks.Final_Assignment_Marks, 2))

            c = c + 1

        else:

            print("You Entered Wrong Percentage.\nEnter Correct Percentage.")

            c = c


def Mids_Marks():
    print(dash * 10)

    print("\nMid-Term Marks:\n")

    Obtained_Marks = [0]

    Total_Marks = [0]

    count = 1

    while count <= 1:

        Obtained_Marks[0] = eval(input("Enter Obtained Marks:"))

        Total_Marks[0] = eval(input("Enter Total Marks:"))

        if Obtained_Marks[0] <= Total_Marks[0]:

            count += 1

        else:

            print("You Have Entered Wrong Marks\nEnter Marks Again")

            count = count

    c = 1
    while c == 1:

        Mids_Marks.Mids_Weightage = int(input("\nEnter Weightage of Mids in Final Result:"))

        if 1 <= Mids_Marks.Mids_Weightage <= 100:

            Mids_Marks.Final_Mids_Marks = ((Obtained_Marks[0] / Total_Marks[0]) * Mids_Marks.Mids_Weightage)

            print("\nYour Mids Marks Are:", round(Mids_Marks.Final_Mids_Marks, 2))

            c += 1

        else:

            print("You Entered Wrong Percentage.\nEnter Correct Percentage.")

            c = c


def Terminal_Marks():
    print(dash * 10)

    print("\nTerminals Marks Calculation:\n")

    Obtained_Marks = [0]

    Total_Marks = [0]

    count = 1

    while count <= 1:

        Obtained_Marks[0] = eval(input("Enter Obtained Marks:"))

        Total_Marks[0] = eval(input("Enter Total Marks:"))

        if Obtained_Marks[0] <= Total_Marks[0]:

            count += 1

        else:

            print("You Have Entered Wrong Marks\nEnter Marks Again")

            count = count

    c = 1

    while c == 1:

        Terminal_Marks.Terminal_Weightage = int(input("\nEnter Weightage of Terminal Marks in Final Result:"))

        if Terminal_Marks.Terminal_Weightage >= 1 and Terminal_Marks.Terminal_Weightage <= 100:

            Terminal_Marks.Final_Terminal_Marks = (
                    (Obtained_Marks[0] / Total_Marks[0]) * Terminal_Marks.Terminal_Weightage)

            print("\nYour Terminal Marks Are:", round(Terminal_Marks.Final_Terminal_Marks, 2))

            c += 1

        else:

            print("You Entered Wrong Percentage.\nEnter Correct Percentage.")

            c = c


def Theory_Marks():
    i = 1
    while i == 1:

        print("\nTHEORY MARKS CALCULATION:")

        print(dash * 10)

        Quiz_Marks()

        Assignment_Marks()

        Mids_Marks()

        Terminal_Marks()
        if (
                Quiz_Marks.Quiz_Weightage + Assignment_Marks.Assignment_Weightage + Mids_Marks.Mids_Weightage + Terminal_Marks.Terminal_Weightage) == 100:

            print(dash * 10)
            print(dash * 10)
            i = i + 1
        else:
            print("You Entered Wrong Weightage.\nEnter Correct Weightage:")

        print(dash * 25)


def Lab_Marks():
    i = 1

    while i == 1:
        print("\nLAB MARKS CALCULATION:")

        print(dash * 10)

        Assignment_Marks()

        Mids_Marks()

        Terminal_Marks()

        if (
                Assignment_Marks.Assignment_Weightage + Mids_Marks.Mids_Weightage + Terminal_Marks.Terminal_Weightage) == 100:
            i = i + 1
        else:
            print("You Entered Wrong Weightage.\nEnter Correct Weightage.")
            i = i

        print(dash * 25)


def Final_Theory_Result():
    Final_Theory_Result.Final_Theory_Marks = round(Quiz_Marks.Final_Quiz_Marks, 2) + round(
        Assignment_Marks.Final_Assignment_Marks, 2) + round(Mids_Marks.Final_Mids_Marks, 2) + round(
        Terminal_Marks.Final_Terminal_Marks, 2)

    print("\nYour Theory Marks are:", round(Final_Theory_Result.Final_Theory_Marks, 2), )

    print(dash * 25)


def Final_Lab_Result():
    Final_Lab_Result.Final_Lab_Score = round(Assignment_Marks.Final_Assignment_Marks, 2) + round(
        Mids_Marks.Final_Mids_Marks, 2) + round(Terminal_Marks.Final_Terminal_Marks, 2)

    print("\nYour Final Lab Marks are:", round(Final_Lab_Result.Final_Lab_Score, 2), )
    print(dash * 25)


def Credit_Hours():
    h = 1
    while h == 1:
        Credit_Hours.Total = int(input("Enter Course Credit Hours:\n"))

        TH = (100 / Credit_Hours.Total) / 100

        Credit_Hours.TCH = int(input("Enter Theory Credit Hours:\n"))

        if Credit_Hours.TCH < Credit_Hours.Total:

            LCH = Credit_Hours.Total - Credit_Hours.TCH

            Theory_Hours = TH * Credit_Hours.TCH

            Credit_Hours.Final_Theory = Final_Theory_Result.Final_Theory_Marks * Theory_Hours

            print("Final Theory Marks are:", round(Credit_Hours.Final_Theory, 2))

            Lab_Hours = LCH * TH

            Lab_Marks()

            Final_Lab_Result()

            Credit_Hours.Final_Lab = Final_Lab_Result.Final_Lab_Score * Lab_Hours

            print("Final Lab Marks are:", round(Credit_Hours.Final_Lab, 2))

            h = h + 1

        elif Credit_Hours.Total == Credit_Hours.TCH:

            Theory_Hours = TH * Credit_Hours.TCH

            Credit_Hours.Final_Theory = Final_Theory_Result.Final_Theory_Marks * Theory_Hours

            print("Final Theory Marks are:", round(Credit_Hours.Final_Theory, 2))

            Credit_Hours.Final_Lab = 0

            h = h + 1

        else:
            print("Invalid Input.\nTry Again.")

            h = h

    print("***", dash * 10, "***\n***", dash * 10, "***")


def GPA():
    GPA.Result = Obtained_Marks
    if 54 >= GPA.Result >= 50:
        gpa = 1.3
        print("Your GPA is:", gpa)
        print("Your Grade is D")

    elif 59 >= GPA.Result >= 55:
        gpa = 1.7
        print("Your GPA is:", gpa)
        print("Your Grade is C-")

    elif 64 >= GPA.Result >= 60:
        gpa = 2.0
        print("Your GPA is:", gpa)
        print("Your Grade is C+")

    elif 69 >= GPA.Result >= 65:
        gpa = 2.3
        print("Your GPA is:", gpa)
        print("Your Grade is C+")

    elif 74 >= GPA.Result >= 70:
        gpa = 2.7
        print("Your GPA is:", gpa)
        print("Your Grade is B-")

    elif 79 >= GPA.Result >= 75:
        gpa = 3.0
        print("Your GPA is:", gpa)
        print("Your Grade is B")

    elif 84 >= GPA.Result >= 80:
        gpa = 3.3
        print("Your GPA is:", gpa)
        print("Your Grade is B+")

    elif 89 >= GPA.Result >= 85:
        gpa = 3.7
        print("Your GPA is:", gpa)
        print("Your Grade is A-")

    elif 100 >= GPA.Result >= 90:
        gpa = 4.0
        print("Your GPA is:", gpa)
        print("Your Grade is A")

    elif GPA.Result < 50:
        print("You are Fail.")


Theory_Marks()

Final_Theory_Result()

Credit_Hours()

Obtained_Marks = Credit_Hours.Final_Theory + Credit_Hours.Final_Lab
print("Your Have Obtained ", round(Obtained_Marks, 2), "% Marks in This Course.")

GPA()
print(dash * 5, "Thank You", dash * 5)
