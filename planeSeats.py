#Braedon Gipson
#January 2, 2023

default = 10 #max amount of 4 person families that could fit on the plane with no reservations
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
        return default
    input =  processString(input)

    taken_seats = []
    for i in range(0, len(input)-1, 2):
        taken_seats.append(''.join(input[i:i+2]))
    seats = {}

    for i in range (1, 6):
        seats[i] = {}
        for c in colLetters:
            if str(i) + c in taken_seats:
                seats[i][c] = 'x'
            else:
                seats[i][c] = 'o'
    
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
    '''
    num_families = 0
    for i in range(1, 6):
        #check middle section D E F G
        
        middle_section = seats[i][colLetters[3]] + seats[i][colLetters[4]] + seats[i][colLetters[5]] + seats[i][colLetters[6]]
        if('x' in middle_section): #a middle seat is reserved
            if ('x' in (seats[i][colLetters[5]],seats[i][colLetters[6]])): #if F or G are reserved check for B C D E
                left = seats[i][colLetters[1]] + seats[i][colLetters[2]] + seats[i][colLetters[3]] + seats[i][colLetters[4]]
                if 'x' not in left:
                    num_families += 1
                    continue
            else:  #if D or E are reserved check for F G H J
                right = seats[i][colLetters[5]] + seats[i][colLetters[6]] + seats[i][colLetters[7]] + seats[i][colLetters[8]]
                if 'x' not in right:
                    num_families += 1
                    continue
        else: #if middle section is clear check B C and H J
            left = seats[i][colLetters[1]] + seats[i][colLetters[2]]
            right = seats[i][colLetters[7]] + seats[i][colLetters[3]]
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
