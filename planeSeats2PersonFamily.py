#Braedon Gipson
#January 2, 2023

DEFAULT = 20 #max amount of 4 person families that could fit on the plane with no reservations
NUM_ROWS = 5
LEFT_SECTION_END = 3
RIGHT_SECTION_START = 7
colLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'] #The Letters representing the columns in the plane seating

def reserve(input):
    if input == "":
        return DEFAULT
    input =  processString(input)

    selected_rows = set([int(input[x]) for x in range(0,len(input), 2)])
 
    taken_seats = []
    for i in range(0, len(input)-1, 2):
        taken_seats.append(''.join(input[i:i+2]))
    seats = {}

    for i in range (1, NUM_ROWS+1):
        seats[i] = {}
        for c in colLetters:
            if str(i) + c in taken_seats:
                seats[i][c] = False #reserved
            else:
                seats[i][c] = True #available
    
    return maxFamilies(seats, selected_rows)


def processString(str):
    str = list(str)
    ret = []
    for item in str:
        if item != ' ':
            ret.append(item)
    return ret

def checkNext(row, start, end):
    ret = 0
    for i in range(start, end-1):
        if row[colLetters[i]] and row[colLetters[i+1]]:
            ret += 1
            return ret
    return 0



def maxFamilies(seats, selected_rows):
    num_families = 0
    for i in selected_rows:
        if all([seats[i][colLetters[n]] for n in range(LEFT_SECTION_END, RIGHT_SECTION_START)]):
            num_families += 2
        num_families += checkNext(seats[i], 0, 2) + checkNext(seats[i], 3, 6) + checkNext(seats[i], 7, 9)
    return num_families


if __name__ == "__main__":
   print(reserve("1A 2F 1C 3E 4F 5H"))
   print(reserve(""))
