def displayInfo(election_list, district_num):
    """
    -------------------------------------------------------
    This function takes the list of dictionary and prints information (The number of polling stations,
    The number of valid ballots, The total ballots cast, Percentage of voter turnout) given an electoral district number
    -------------------------------------------------------
    Parameters:
        election_list - list of dictionaries
        district_num - an integer the user inputted from q3_q1.py
    Returns:
        None
    -------------------------------------------------------
    """
    # start a for loop in list to access each dictionary
    for row in election_list:
        # check if the number is in the values of the dictionary
        if str(district_num) in row.values():
            # print the following values of that dictionary
            print("Polling Stations:", row.get('Polling Stations')+',', 'Valid Ballots:', row.get('Valid Ballots')+',', 'Total Ballots Cast:', row.get('Total Ballots Cast')+',', 'Voter Turnout:', row.get('Percentage of Voter Turnout')+'%')


def uniqueDistricts(name, election_list):
    """
    -------------------------------------------------------
    This function takes a province name and returns a list of the names of the electoral districts in that province
    -------------------------------------------------------
    Parameters:
        name - string; province name user inputted from a3_q1
        election_list - list of dictionaries
    Returns:
        province_list - list
    -------------------------------------------------------
    """
    # empty list
    province_list = []

    # start for loop in list of dictionaries to access each dictionary
    for row in election_list:
        # check if the name is in the values of the dictionary
        if name in row.values():
            # append the value of the key 'Electoral District Name'
            province_list.append(row.get('Electoral District Name'))

    return province_list


def findMax(election_list, topic):
    """
    -------------------------------------------------------
    This function find the max value for the supplied key value among any of (Electors, Population, Polling Stations,
    Valid Ballots, Rejected ballots, Total ballots)
    -------------------------------------------------------
    Parameters:
       election_list - list of dictionaries
       topic - string; user inputted from a3_q1.py
    Returns:
        max_value, associated - list with found max value and associated electoral district name
    -------------------------------------------------------
    """
    # empty list
    values = []

    # start for loop in list of dictionaries to access each dictionary
    for row in election_list:
        # check if the user's input is in the keys of the dictionary
        if topic in row.keys():
            # append the associated value to list
            values.append(row.get(topic))

    # insertion sorting
    # start for loop
    for i in range(1, len(values)):
        # check which value is greater than the other
        while i > 0 and values[i-1] > values[i]:
            # swap the index
            values[i-1], values[i] = values[i], values[i-1]

            # check with previous value
            i = i-1

    # assign the last value to max_value since it is sorted to least to greatest
    max_value = values[-1]

    # start for loop to access each dictionary
    for row in election_list:
        # check if the max value is in the dictionary
        if max_value in row.values():
            # assign the value of the key 'Electoral District Name' to variable
            associated = row.get('Electoral District Name')

    return max_value, associated


def findMin(election_list, topic):
    """
    -------------------------------------------------------
    This function find the min value for the supplied key value among any of (Electors, Population, Polling Stations,
    Valid Ballots, Rejected ballots, Total ballots)
    -------------------------------------------------------
    Parameters:
        election_list - list of dictionaries
        topic - string; user inputted from a3_q1.py
    Returns:
        min_value, associated - list with found min value and associated electoral district name
    -------------------------------------------------------
    """
    # empty list
    values = []

    # start for loop to access each dictionary in the list
    for row in election_list:

        # check if the user's input is in the keys of the dictionary
        if topic in row.keys():

            # append the associated value to the list
            values.append(row.get(topic))

    # insertion sorting
    # start for loop
    for i in range(1, len(values)):

        # check which value is greater than the other
        while i > 0 and values[i-1] > values[i]:

            # swap the index
            values[i-1], values[i] = values[i], values[i-1]

            # check with previous one
            i = i-1

    # assign the index 0 to variable since list is sorted least to greated
    min_value = values[0]

    # start for loop to access each dictionary in list
    for row in election_list:

        # check if the min value is the values of the dictionary
        if min_value in row.values():

            # assign the value of the key 'Electoral District Name' to variable
            associated = row.get('Electoral District Name')

    return min_value, associated


def totalVotes(election_list):
    """
    -------------------------------------------------------
    This function returns a list of dictionaries that has the total number of ballots cast in every Canadian province
    and territory.
    -------------------------------------------------------
    Parameters:
        election_list - list of dictionaries
    Returns:
        total - list of dictionaries
    -------------------------------------------------------
    """
    # empty lists
    total = []
    provinces_added = []
    total_ballots = []

    # start for loop to access each dictionary in list
    for district in election_list:
        # check if value of the key 'Province' is not in the list
        if district['Province'] not in provinces_added:
            # append the value to list
            provinces_added.append(district['Province'])
            # append the value of the key 'Total Ballots Cast'
            total_ballots.append(int(district['Total Ballots Cast']))

        # check if value of the key 'Province' is in the list
        elif district['Province'] in provinces_added:
            # find index of the value
            index = provinces_added.index(district['Province'])
            # add the value to the existing value
            total_ballots[index] += int(district['Total Ballots Cast'])

    # start for loop to add total ballots to each province
    for province in range(len(provinces_added)):
        # create new dictionary adding province name and total ballots to respective keys
        dictionary = {'Province': provinces_added[province], 'Total Ballots Cast': total_ballots[province]}
        # append the dictionary to the list
        total.append(dictionary)

    return total


def selectionSort(election_list, given_key):
    """
    -------------------------------------------------------
    This function takes the list of dictionaries and a key and sorts the list of dictionaries into increasing order
    based on the given key the user inputted.
    -------------------------------------------------------
    Parameters:
        election_list - list of dictionaries
        given_key - string; user inputted from a3_q1
    Returns:
        election_list - list of dictionaries which is sorted based on specified key
    -------------------------------------------------------
    """
    size = len(election_list)

    # start for loop
    for i in range(size):
        # assign first index as the minimum value
        min_idx = i

        # start nested for loop
        for j in range(i + 1, size):

            # check if the value of the given key is greater than the min
            if int(election_list[j][given_key]) < int(election_list[min_idx][given_key]):
                # reassign min
                min_idx = j

        # check if the value does not equal to the min
        if min_idx != i:
            # swap index positions
            election_list[i], election_list[min_idx] = election_list[min_idx], election_list[i]

    return election_list


def binarySearch(election_list, num):
    """
    -------------------------------------------------------
    This function searches for an electoral district based on its electoral district number and returns the associated
    percentage of voter turnout.
    -------------------------------------------------------
    Parameters:
        election_list - list of dictionaries
        num - integer; user inputted an electoral district number from a3_q1.py
    Returns:
        value #descripe what it returns; or None
    -------------------------------------------------------
    """
    # call function; selectionSort to sort the list of dictionaries in increasing order based on Electoral District Number
    selectionSort(election_list, 'Electoral District Number')

    start = 0
    end = len(election_list) - 1

    while start <= end:
        # find and assign the middle index
        mid = (end + start) // 2

        # check if the user's given district number is the middle value
        if int(election_list[mid]['Electoral District Number']) == num:
            return election_list[mid]['Percentage of Voter Turnout']

        # check if the mid-value is greater than user's given district number
        elif num < int(election_list[mid]['Electoral District Number']):
            # reassign end value
            end = mid-1
        else:
            # reassign the start value if user's district number is less than mid-value
            start = mid + 1

    return None
