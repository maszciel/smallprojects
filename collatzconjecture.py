def user():
    
    while True:
        try:
            user = input("Your integer: ")
        except:
            print("Please provide an integer.")
        else:
            break
    
    return int(user)

def collatz(user):
    count = 0
    
    while user != 1:
        
        count += 1
        
        if user%2 == 0:
            user /= 2
        else:
            user = 3*user+1

    return count

if __name__ == "__main__":
    number = user()
    result = collatz(number)
    print(f"Steps to reach 1: {result}")
