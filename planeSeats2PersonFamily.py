#Braedon Gipson
#January 2, 2023

DEFAULT = 20 #max amount of 4 person families that could fit on the plane with no reservations
NUM_ROWS = 5
LEFT_SECTION_END = 3
RIGHT_SECTION_START = 7
FIRSTROWEND = 2
SECONDROWEND = 6
THIRDROWEND = 9
colLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'] #The Letters representing the columns in the plane seating

def reserve(input):
    ''' Takes a string containing the seats that are reserved
    Uses MaxFamilies() method to return the maximum number of 2 person families that can be seated on the plane with the given reservations
    if the string is empty returns 10
    Parameters
    ----------
    input : str, required
        The seats in format '1A 2B 3D' that are reserved
    output: int 
        number of 4 person families that can be seated
    '''
    if input == "":
        return DEFAULT
    input =  processString(input)

    selected_rows = set([int(input[x]) for x in range(0,len(input), 2)])
 
    taken_seats = []
    for i in range(0, len(input)-1, 2):
        taken_seats.append(''.join(input[i:i+2]))
    seats = {}

    for i in range (1, NUM_ROWS+1):
        for c in colLetters:
            if str(i) + c in taken_seats:
                seats[(i,c)] = False #reserved
            else:
                seats[(i,c)] = True #available
    return maxFamilies(seats, selected_rows)


def processString(str):
    '''takes string of reserved seats on plane
        returns a list of the seats (str) without white space
    Parameters
    ----------
    input : str
    output : list(str)
    '''
    str = list(str)
    ret = []
    for item in str:
        if item != ' ':
            ret.append(item)
    return ret

def checkNext(seats,rowNum, start, end):
    ret = 0
    for i in range(start, end-1):
        if seats[(rowNum, colLetters[i])] and seats[(rowNum, colLetters[i+1])]:
            ret += 1
            return ret
    return 0



def maxFamilies(seats, selected_rows):
    ''' takes 2 key dictionary of seating arrangements
        Returns the maximum number of 2 person families that can be seated
    Parameters
    ----------
    input : {dict(tuple) : str} required
        the seats their codes '1A' and whether or not they are reserved: (reserved == 'x', available == ' ')
    output: int 
        number of 2 person families that can be seated
    '''
    num_families = 0
    for i in selected_rows:
        if all([seats[(i,colLetters[n])] for n in range(LEFT_SECTION_END, RIGHT_SECTION_START)]):
            num_families += 2
        num_families += checkNext(seats,i, 0, FIRSTROWEND) + checkNext(seats,i, FIRSTROWEND+1, SECONDROWEND) + checkNext(seats,i, SECONDROWEND+1, THIRDROWEND)
    return num_families


if __name__ == "__main__":
   print(reserve("1A 2F 1C 3E 4F 5H"))
   print(reserve(""))
