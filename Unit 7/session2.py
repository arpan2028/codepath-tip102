def find_cruise_length(cruise_lengths, vacation_length):
    # check if list is empty 
    if not cruise_lengths:
        return False
    # create mid
    mid = len(cruise_lengths) // 2
    # if mid == vacation length
    if cruise_lengths[mid] == vacation_length:
        # return trur
        return True
    # elif mid < vacation length
    elif cruise_lengths[mid] < vacation_length:
    # call function and move to the left
        find_cruise_length(cruise_lengths[mid + 1:], vacation_length)
    # else
    else:
    # call function and move to the right 
        find_cruise_length(cruise_lengths[:mid], vacation_length)
        

  


print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


def find_cruise_length(cruise_lengths, vacation_length):
    # check if list is empty 
    if not cruise_lengths:
        return False
    # create mid
    mid = len(cruise_lengths) // 2
    # if mid == vacation length
    if cruise_lengths[mid] == vacation_length:
        # return trur
        return True
    # elif mid < vacation length
    elif cruise_lengths[mid] < vacation_length:
    # call function and move to the left
        find_cruise_length(cruise_lengths[mid + 1:], vacation_length)
    # else
    else:
    # call function and move to the right 
        find_cruise_length(cruise_lengths[:mid], vacation_length)
        

  


print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))