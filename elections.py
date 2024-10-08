from functions3 import displayInfo
from functions3 import uniqueDistricts
from functions3 import findMax
from functions3 import findMin
from functions3 import totalVotes
from functions3 import selectionSort
from functions3 import binarySearch

# empty list
election_info = []


try:
    given_data = open('electionsData.txt', 'r')

    # read first line and take out '\n'
    heading = given_data.readline().strip('\n')
    # split line into list
    headings = heading.split(',')

    # start for loop to read data
    for line in given_data:

        # split line into list and get rid of '\n'
        sections1 = line.strip('\n').split(',')

        # assign each index of two list as pairs
        d = {headings[i]: sections1[i] for i in range(len(headings))}

        # append the dictionary to list
        election_info.append(d)

    given_data.close()

except OSError:
    print('A file error occurred.')

# menu
option = 0  # initialize variable to get loop started

# while the user does not choose the exit option

while option != 8:
    print('MENU: \n'
          'This program runs different functions on Canadian election data.\n'
          'Here are the various functions that can be executed \n'
              '1. Display information for an electoral district\n'
              '2. Show unique district by the given province\n'
              '3. Find the maximum value of the given subject\n'
              '4. Find the minimum value of the given subject\n'
              '5. Displays the total number of ballots in each province/territory\n'
              '6. Sorts the information in increasing order based on the specified key\n'
              '7. Provides the percentage of voter turnout based on the given electoral district\n'
              '8. Exit\n')
    try:
        option = int(input('Please enter the corresponding number you wish to execute: '))
        # if the user inputs a number out of range (1-8), it will continuously ask for a valid input
        while option < 1 or option > 8:
            option = int(input('Error! Please enter a number on the menu you wish to execute: '))


        if option == 1:
            try:
                district_number = int(input("Please enter an electoral district number: "))
                displayInfo(election_info, district_number)

            # if the user enters a string instead of an integer, it will send user back to the menu
            except ValueError:
                print('Error! Invalid input. Try again!')


        elif option == 2:

            # initialize flag variable
            valid_input = False
            # if the user's given province is not in the list, it will continuously ask for a valid input
            while not valid_input:
                province = input('Please enter an existing province name (case-sensitive):')

                # for loop to check if user's province is in the list
                for row in election_info:
                    if province in row.values():
                        valid_input = True

            print(uniqueDistricts(province, election_info))


        elif option == 3:
            try:
                supplied_key = input('- “Electors”\n'
                                         '- “Population”\n'
                                         '- “Polling Stations”\n'
                                         '- “Valid Ballots”\n'
                                         '- “Rejected Ballots”\n'
                                         '- “Total Ballots”\n'
                                         'Please enter a section provided below you wish to find the max value for (case-sensitive): ')
                max_info = findMax(election_info, supplied_key)
                print('Max', supplied_key+':', max_info[1], max_info[0])

            # if the user inputs a non-existent key, it will send user back to menu
            except IndexError:
                print('You did not enter a section from the list. Try again')


        elif option == 4:
            try:
                supplied = input('- “Electors”\n'
                                 '- “Population”\n'
                                 '- “Polling Stations”\n'
                                 '- “Valid Ballots”\n'
                                 '- “Rejected Ballots”\n'
                                 '- “Total Ballots”\n'
                                 'Please enter a section provided below you wish to find the min value for (case-sensitive): ')
                min_info = findMin(election_info, supplied)
                print('Min', supplied+':', min_info[1], min_info[0])

            # if the user inputs a non-existent key, it will send user back to menu
            except IndexError:
                print('You did not enter a section from the list. Try again')


        elif option == 5:

            # assign list to variable
            votes = totalVotes(election_info)

            length = len(votes)

            # selection sort
            for i in range(length):

                # assign min index
                min_idx = i

                # start nested for loop
                for j in range(i + 1, length):
                    # check if the value province is alphabetically lower than the min
                    if votes[j]['Province'] < votes[min_idx]['Province']:
                        # reassign min index
                        min_idx = j

                if min_idx != i:
                    # swap positions if value does not equal to min
                    votes[i], votes[min_idx] = votes[min_idx], votes[i]

            for pair in votes:
                # print each values of 'province' and 'total ballots cast
                print(pair['Province']+':', pair['Total Ballots Cast'])


        elif option == 6:
            # initialize flag variable
            valid = False

            # if user inputs an non-existing key, it will repeatably ask again until valid
            while not valid:
                user_key = input('Please enter an existing section you wish the list of dictionary to be ordered in an increasing order (case-sensitive): ')

                # start for loop to access each dictionary
                for row in election_info:
                    # check if user's input is in the keys of the dictionary
                    if user_key in row.keys():
                        # trigger flag variable to exit the loop
                        valid = True

            selectionSort(election_info, user_key)
            print('Sorted by', user_key)


        elif option == 7:
            try:
                district_number = int(input('Please enter an existing electoral district number: '))

                # assign return value to variable
                result = binarySearch(election_info, district_number)

                # check if return value returned nothing (None)
                if result is None:
                    print('Item Was Not Found')

                # check if return value returned a value
                else:
                    print('Found:', result)

            # if user inputs a string, it will send user back to menu
            except ValueError:
                print('Error! You entered an invalid value\n')

    except ValueError:
        print('Error.')
        print('Try again')


# if user chooses 8, it will exit the program
print('Thank you. Goodbye.')
quit()
