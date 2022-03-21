import edu
import Algorithm
import Python
import compNet
import time


def callMe(ui):
    score = 0
    for i in ui.question:
        print()
        print("*" * 70)
        print()
        print(i)
        ans = input("Enter the Correct Answer : ")

        if ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd':

            if ans == ui.question[i]:
                time.sleep(1)
                print("\nCorrect Answer")
                score += 1
                time.sleep(1)

            else:
                time.sleep(1)
                print("\nWrong Answer ")
                time.sleep(1)
                print(f"The Correct Answer Is : {ui.question[i]}")
        else:
            print("Please Enter only (a/b/c/d)")

    return score,len(ui.question)


def main():
    name = input("\nEnter Your Name : ")

    print(f"Welcome {name.capitalize()} to Quizz competition program")
    
    print()
    
    print("WHICH FIELD DO YOU WANT TO CHOOSE ? \n")

    print("1) General Knowledge \t2) Algorithm \t3) Computer Network   \t4) Python \n")

    choose = int(input("Enter Your Selection Here : "))


    dict = {1:edu, 
            2:Algorithm, 
            3:compNet, 
            4:Python
            }

    score,totalScore = callMe(dict[choose])

    print("\nYOU GOT ", abs(score),"/",totalScore)

    if score < 5:
        print("Poor Score :-( ")
        
    elif 6 <= score < 8:
        print("Good Score :-) ")
    
    else:
        print("Excellent score ✌️")



if __name__ == "__main__":
    main()

    
