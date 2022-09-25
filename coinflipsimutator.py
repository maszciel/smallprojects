import random

def coinFlip():
    while True:
        try:
            inp = int(input("How many times do you want to flip? "))
        except:
            print("Please provide an integer.")
        else:
            break

    heads = 0
    tails = 0

    for e in range(1,inp+1):
        flip = random.randint(0,1)

        if flip == 0:
            heads += 1
        else:
            tails += 1

    return (heads, tails)

if __name__ == "__main__":
    head, tail = coinFlip()
    print(f"Heads: {head}; Tails: {tail}")