# carplate.py
# Date created: 13th July 2012
# Created by: Koh Jing Yu
# Description: Check if a car plate number is valid car plate number and output.
# An invalid car plate number will also be written to a text file INVALID.DAT.

def get_checksum(number):
    checksum = ['A', 'Y', 'U', 'S', 'P', 'L', 'J', 'G', 'D', 'B', 'Z', 'X', 'T', 'R', 'M', 'K', 'H', 'E', 'C']
    return checksum[number]

def check_validity(plate_number):
    #get checksum
    checksum = plate_number[-1]
    plate_number = plate_number.lower()
    #remove checksum
    plate_number = plate_number[0:(len(plate_number)-1)]
    values = []
    weight = [14, 2, 12, 2, 11, 1]

    result = 0

    for i in range(0, len(plate_number)):
        values.append(plate_number[i])

    int_count = 0
    first_int_index = -1

    for i in range(0, len(values)):
        try:
            # valueis an int
            int(values[i])
            int_count += 1

            #first_int_index has not been set
            if(first_int_index == -1):
                first_int_indx = i
        except:
            pass

    if(int_count < 4):
        #only 3 ints, add a 0
        first_half = values[0:first_int_index - 2]
        second_half = values[first_int_index - 2:]
        final_values = first_half
        final_values.append(0)

        for i in range(0, len(second_half)):
            final_values.append(second_half[i])

        values = final_values

    for i in range(0, 3):
        try:
            #is not a char
            values[i] = int(values[i])
            break
        except:
            #is a char
            #convert to int representative (a = 1, b = 2, c = 3, etc)
            values[i] = ord(values[i]) - 96

        if(i == 2):
            # 3 alphabets, remove the first one
            values[0] = 0

    #convert values to int
    for i in range(0, len(values)):
        values[i] = int(values[i])

    start_position = len(values) - len(weight)

    for i in range(start_position, len(values)):
        result += values[i] * weight[i - start_position]

    correct_checksum = get_checksum(result % 19)

    if(checksum == correct_checksum):
        #valid!
        return ("Valid, checksum is " + correct_checksum)
    else:
        #invalid checksum
        #write checksum to INVALID.DAT
        plate_number = plate_number.upper()
        outfile = open("INVALID.DAT", "a")
        outfile.write(plate_number + "\n")
        outfile.close()
        
        return ("Invalid, checksum is " + correct_checksum)

plate_number = input("Enter a car plate number.\n")
print(check_validity(plate_number))
