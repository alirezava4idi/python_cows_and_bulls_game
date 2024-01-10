import random


len_random_number = 4


random_number = str(random.randint(1000, 9999))


def noDuplicates(num):
    return len(set(num)) == len_random_number
        

while not noDuplicates(random_number):
    random_number = str(random.randint(1000, 9999))

finished = False
    
while True:
    if finished:
        break
    print("Enter the number of tries: ", end="")
    try:
        num_of_tries = int(input())  

        count_tries = 0
        for i in range(num_of_tries):   
            print("Enter your guess (it's a four digit code): ", end="")
            guess = input()

            if len(guess) != len_random_number:
                raise

            if not noDuplicates(guess):
                print("Number should not have repeated digits. Try again")
                continue

            count_bulls = 0
            count_cows = 0
            for i in range(len_random_number):
                if guess[i] == random_number[i]:
                    count_bulls += 1
                    continue

                if guess[i] in random_number and guess[i] != random_number[i]:
                    count_cows += 1
                
            print(f"Response: {count_bulls} bulls, {count_cows} cow")
            count_tries += 1
            if count_tries == num_of_tries:
                print(f"you ran out of tries. Number was {random_number}")
                finished = True
                break

            if guess == random_number:
                print("you guessed right!")
                finished = True
                break
    except:
        print("invalid input", end="\n\n")
        print("try again? y/N")
        ans = input()

        if ans.lower() != 'y':
            break

