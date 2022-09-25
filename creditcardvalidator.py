def user():
    
    while True:
        
        card_number = []
        
        try:
            inp = input("Credit card number (or [break] to stop): ")
            
            if inp == "break":
                break
            else:
                for element in inp:
                    if element.isdigit():
                        card_number.append(int(element))
                    elif element == " " or element == "-":
                        pass
                    else:
                        raise TypeError()

                if len(card_number) != 16:
                    raise TypeError()
        except:
            print("Please provide a 16 digit number.")
        else:
            break
    
    return card_number

def step_one(card):
    
    ind = 0
    
    for digit in card:
        
        if ind == len(card) - 1:
            pass
        elif ind%2 == 0:
            card[ind] *= 2
            
            if card[ind] > 9:
                sum = 0
                for digit in str(card[ind]):
                    sum += int(digit)
                card[ind] = sum
                    
        else:
            pass
        
        ind += 1
        
    
    return card

def step_two(step_one_result):
    
    control_number = step_one_result.pop()
    
    if (sum(step_one_result) + control_number) % 10 == 0:
        return True
    else:
        return False

def main():
    while True:
        credit_card = user()

        try:
            firststep = step_one(credit_card)

            secondstep = step_two(firststep)
            
            if secondstep == True:
                print("Card Accepted")
                return True
                break
            else:
                print("Sorry, wrong card number.")
            
        except:
            print("Goodbye")
            break

if __name__ == "__main__":
    main()
