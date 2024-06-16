import random
MAX_LINES = 3

TOROW = 3
TOCLM = 3

letter = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9,
}

let_val = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def find_right(colls, bet, lines, let_val):
    winval = 0
    winlines = []
    for line in range(lines):
        let = colls[0][line]
        for coll in colls:
            tempval = coll[line]
            if let != tempval:
                break
        else: 
                winval += let_val[let] * bet[line]
                winlines.append(line + 1)
    return winval, winlines



def print_slot(colls):
    for row in range(len(colls[0])):
        for i, coll in enumerate(colls):
            if i != len(colls) - 1:
                print(coll[row], end=" | ")
            else:
                print(coll[row], end="")

        print()



def get_slot_list(TOROW, TOCLM, letter):
    Total_list = []
    for letters, count in letter.items():
        for _ in range(count):
            Total_list.append(letters)

    colls = []
    for _ in range(TOCLM):
        coll = []
        temp_list = Total_list[:]
        for _ in range(TOROW):
            val = random.choice(temp_list)
            temp_list.remove(val)
            coll.append(val)
        
        colls.append(coll)

    return colls


def get_balance():
    while True:
        amount = input("How much is your balance? $ ")
        if amount.isdigit():
            balance = int(amount)
            if balance > 0:
                break
            else:
                print("Balance needs to be larger than $0.")
        else:
            print("please enter a number.")    
    
    return balance

def get_lines():
    while True:
        line = input(f"How many lines do you want to bet on (1 - {MAX_LINES}). ")
        if line.isdigit():
            lines = int(line)
            if lines <= MAX_LINES:
                break
            else:
                print(f"Pick (1 - {MAX_LINES}). ")
        else:
            print("please enter a number.")    
    
    return lines

def get_bet(lines):
    bet = []
    i = 0
    while True:
        mon = input(f"How much would you like to bet on line {i + 1}. $")
        if mon.isdigit():
            if int(mon) > 0:
                bet.append(int(mon))
                i += 1
                if i == lines:
                    break
            else:
                print("Bet needs to be larger than $0. ")
        else:
            print("please enter a number.")
            
                
    return bet

def game(balance):
    lines = get_lines() 
    while True:
        bet = get_bet(lines)
        if sum(bet) <= balance:
            total_bet = sum(bet) 
            break
        else:
            print ("Balance is too low to make this bet!")
    
    print(f"You are betting ${" $".join(map(str, bet))} on {lines} lines for a total of ${total_bet}!")

    slot = get_slot_list(TOROW, TOCLM, letter)

    print_slot(slot)

    win, winlines = find_right(slot, bet, lines, let_val)

    print(f"you won ${win} on line:", *winlines)
    return win - total_bet

def main():
    balance = get_balance()
    while True:
        print(f"Current balance ${balance}")
        play = input("press enter to play. (q to quit)")
        if play == "q":
            break
        else:
             balance += game(balance) 
    
    print(f"you ended with ${balance}")

main()