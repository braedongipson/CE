import string

colLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']

def reserve(input):#take seat string "4J 3J 2J 1J 5J" and mark as taken
    if input == "":
        return 0
    input =  processString(input)
    #print(input)
    taken_seats = []
    for i in range(0, len(input)-1, 2):
        taken_seats.append(''.join(input[i:i+2]))
   # print(taken_seats)

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
    str = list(str)
    ret = []
    for item in str:
        if item != ' ':
            ret.append(item)
    return ret

def maxFamilies(seats):
   # middle section D E F G
   # left isle B C D E
   # right isle F G H J

    num_families = 0
    for i in range(1, 6):
        #check middle section D E F G
        middle_section = seats[i]['D'] + seats[i]['E'] + seats[i]['F'] + seats[i]['G']
        if('x' in middle_section): #a middle seat is reserved
            if ('x' in (seats[i]['F'],seats[i]['G'])): #if F or G are reserved check for B C D E
                left = seats[i]['B'] + seats[i]['C'] + seats[i]['D'] + seats[i]['E']
                if 'x' not in left:
                    num_families += 1
                    continue
            else:  #if D or E are reserved check for F G H J
                right = seats[i]['F'] + seats[i]['G'] + seats[i]['H'] + seats[i]['J']
                if 'x' not in right:
                    num_families += 1
                    continue
        else: #if middle section is clear check B C and H J
            left = seats[i]['B'] + seats[i]['C']
            right = seats[i]['H'] + seats[i]['J']
            if ( 'x' not in left and 'x' not in right): #If if both are clear... +2 families 
                num_families += 2 
            else:
                num_families += 1 #if one or neither clear + 1 families
    return num_families

#x means taken 
#o is a possible valid reservation
if __name__ == "__main__":
    print(reserve("1A 2F 1C 3E 4F 5H")) #expect 5
    print(reserve("")) #0
    print(reserve("5E 5F 4E 4F 3E 3F 2E 2F 1E 1F")) #0
    print(reserve("1B 1E 3A 3D 2H 4C 4E 5E")) #5