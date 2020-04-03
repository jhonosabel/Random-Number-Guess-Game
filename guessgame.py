import random
"""
Guess game by mark valdez
"""
def main():
    
    print("Hi welcome to guess game ")
    name = input("Enter your name : ")
    gnum = 0 # number of guess times
    running = True
    score = 0 # user score
    
    while running:
        guesseNum = random.randint(1, 10) # correct humber
        
        print("\n\n\n")
        print("\t\t\t\t player ", name)
        print("\t\t Guess The Number from 1 to 10")
        print("\t\t You have 3 times to guess the number \n")
        print("\t\t Your Current Score : ", score, "\n")
        print("each correct guess you get 10 points")
        print("each 3 times wrong answer you have 5 minus points\n\n")

        #get user input 
        num = int(input("\tEnter your guess number : "))
        print("your Guess number is : ", num) #print user guess number

        
        if num == guesseNum: # if user is correct

            score += 10
            
            print("Your correct")
            gnum -= 3  # guess number times back to zero
            print("The guess number is ", guesseNum)

            #ask user to play again or exit
            x = input("Do you want to play again  [y|n]? : ")
            if x == "y" or x == "Y":
                pass
            elif x == "n" or x == "N":
                running = False
                print("Thank you for playing ")     
            
        elif num > guesseNum: #if user guess if higher number
            
            print("wrong your too high")
            print("The number correct number is ", guesseNum)
            gnum += 1 # add guess times
            print("Your Guesse try is ", gnum , "times")
            if gnum == 3:  # if user got 3 times wrong guess
                score -= 5 # minus (5) points
                gnum -= 3 # guess number times back to zero
                
                #ask user to play again or exit
                x = input("Do you want to play again  [y|n]? : ")
                if x == "y" or x == "Y":
                    pass
                elif x == "n" or x == "N":
                    running = False
                    print("Thank you for playing ")
                    print("Your got ", score, "Points")
                
        elif num < guesseNum: #if user guess if lower number
            
            
            print("The number correct number is ", guesseNum)
            print("wrong your too low")
            gnum += 1
            print("Your Guesse try is ", gnum , "times")
            if gnum == 3:
                score -= 5 # minus (5) points
                gnum -= 3
                x = input("Do you want to play again  [y|n]? : ")
                if x == "y" or x == "Y":
                    pass
                elif x == "n" or x == "N":
                    running = False
                    print("Thank you for playing ", name)
                    print("hi ", name ," Your got ", score, "Points")            

if __name__ == "__main__":
    main()
