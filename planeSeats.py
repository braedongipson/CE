#Braedon Gipson
#January 2, 2023

DEFAULT = 10 #max amount of 4 person families that could fit on the plane with no reservations
NUM_ROWS = 5
LEFT_SECTION_START = 1
LEFT_SECTION_END = 3
PLANE_MIDDLE = 5
RIGHT_SECTION_START = 7
RIGHT_SECTION_END = 9
colLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'] #The Letters representing the columns in the plane seating

def reserve(input):
    ''' Takes a string containing the seats that are reserved
    Uses MaxFamilies() method to return the maximum number of 4 person families that can be seated on the plane with the given reservations
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

    taken_seats = []
    for i in range(0, len(input)-1, 2):
        taken_seats.append(''.join(input[i:i+2]))
    seats = {}

    for i in range (1, NUM_ROWS+1):
        seats[i] = {}
        for c in colLetters:
            if str(i) + c in taken_seats:
                seats[i][c] = 'x'
            else:
                seats[i][c] = ' '
    
    return maxFamilies(seats)


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

def maxFamilies(seats):
    ''' takes 2 dimensional dictionary of seating arrangements
        Returns the maximum number of 4 person families that can be seated
    Parameters
    ----------
    input : dict{dict{int: str}} required
        the seats their codes '1A' and whether or not they are reserved: (reserved == 'x', available == ' ')
    output: int 
        number of 4 person families that can be seated
    Time complexity: O(s*m) where s is the number of columns in a section being checked and m is the number of rows
    Space complexity: O(n * m)
    '''
    num_families = 0
    for i in range(1, NUM_ROWS+1):
        #check middle section D E F G
        middle_section = [str(seats[i][colLetters[n]]) for n in range(LEFT_SECTION_END, RIGHT_SECTION_START)]
        middle_section = ''.join(middle_section)

        if('x' in middle_section): #a middle seat is reserved
            if ('x' in ''.join([str(seats[i][colLetters[n]]) for n in range(PLANE_MIDDLE, RIGHT_SECTION_START)])): #if F or G are reserved check for B C D E
                left = ''.join([str(seats[i][colLetters[n]]) for n in range(LEFT_SECTION_START, PLANE_MIDDLE)])
                if 'x' not in left:
                    num_families += 1
                    continue
            else:  #if D or E are reserved check for F G H J
                right = ''.join([str(seats[i][colLetters[n]]) for n in range(PLANE_MIDDLE, RIGHT_SECTION_END)])
                if 'x' not in right:
                    num_families += 1
                    continue
        else: #if middle section is clear check B C and H J
            left = ''.join([str(seats[i][colLetters[n]]) for n in range(LEFT_SECTION_START, LEFT_SECTION_END)])
            right = ''.join([str(seats[i][colLetters[n]]) for n in range(RIGHT_SECTION_START, RIGHT_SECTION_END)])
            if ( 'x' not in left and 'x' not in right): #If if both are clear... +2 families 
                num_families += 2 
            else:
                num_families += 1 #if one or neither are clear + 1 families
    return num_families

if __name__ == "__main__":
    print(reserve("1A 2F 1C 3E 4F 5H"))
    print(reserve("")) 
    print(reserve("5E 5F 4E 4F 3E 3F 2E 2F 1E 1F"))
    print(reserve("1B 1E 3A 3D 2H 4C 4E 5E"))
    print(reserve("1D 1E 1F 1G"))
    print(reserve("1B 1C 1D 1E"))
