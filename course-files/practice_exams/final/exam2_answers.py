import helpers

capital_lookup = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}
    
artists = [
    {
        "name": "Lady Gaga",
        "genres": ["dance pop", "pop"],
        "image": {
            "url": "https://i.scdn.co/image/pic1.jpg",
            "width": 640
        },
        "url": "https://open.spotify.com/artist/1HY2Jd0NmPuamShAr6KMms"
    },
    {
        "name": "Rihanna",
        "genres": ["dance pop", "pop", "post-teen pop", "r&b"],
        "image": {
            "url": "https://i.scdn.co/image/pic2.jpg",
            "width": 640
        },
        "url": "https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H"
    },
    {
        "name": "Bob Dylan",
        "genres": ["album rock", "classic rock", "folk"],
        "image": {
            "url": "https://i.scdn.co/image/pic3.jpg",
            "width": 1000
        },
        "url": "https://open.spotify.com/artist/74ASZWbe4lXaubB36ztrGX"
    }
]


def _print_title(title):
    print('\n')
    print('#' * len(title))
    print(title)
    print('#' * len(title))

def problem_1():
    _print_title('Problem 1')
    '''
    Given the following capital_lookup dictionary, write a program that prompts 
    the user for a state and then prints to the screen a full sentence that 
    indicates the state they just entered and the capital of that state. 
    You can assume that your user will spell and capitalize the state as it 
    appears in the dictionary.
    '''
    state = input('Type the name of a state to find out the state capital: ')
    # for convenience:
    if len(state) == 0:
        state = 'Illinois'
    print('The state capital of {0} is {1}'.format(state, capital_lookup[state]))

def problem_2():
    _print_title('Problem 2')
    '''
    Write a program that asks a user for the year they were born as a 4-digit 
    integer. If the user enters anything other than a 4-digit integer, 
    tell the user that their entry was invalid and that they should try again.
    
    Note: this is one solution of *many possible solutions:
    '''
    year = None
    while year is None:
        test_year = input('What year were you born (enter 4-digit number)? ')
        if len(test_year) == 0:
            test_year = '1992'
        # 1. check if the string is 4 characters:
        if len(test_year) != 4:
            print('ERROR: The year must be a 4-digit integer')
            # if it's not, prompt them again!
            continue
        # 2. check if the string is an int (this is most easily accomplished with a
        # try / except block):
        try:
            year = int(test_year)
        except:
            # if there was an error in the conversion, then it's not an int.
            # Prompt them again!
            print('ERROR: The year must be a 4-digit integer')
            continue
    print('Year successfully input! You were born in {0}'.format(year))

def problem_3():
    _print_title('Problem 3')
    a = True
    b = False
    c = True

    if a and b:
        print('teal')
    if not c:
        print('orange')
    if a and not b:
        print('yellow')
    if a and b or c:
        print('green')
    else:
        print('pink')
    if b or a and b:
        print('turquoise')
    elif not a:
       print('violet')
    else:
        print('red')


def problem_4():
    _print_title('Problem 4')
    
    # part 1:
    print(type(artists[0]))
    print(type(artists[0]['genres'][0]))
    print(type(artists[2]['image']['width']))

def problem_5():
    _print_title('Problem 5')
    def get_genres(artists):
        genres = []
        for artist in artists:
            genres += artist['genres']
        return genres
    print(get_genres(artists))


def problem_5_EC():
    _print_title('Problem 5 (Extra Credit)')
    def get_genres(artists):
        genres = []
        for artist in artists:
            for genre in artist['genres']:
                if genre not in genres:
                    genres.append(genre)
        return genres
    print(get_genres(artists))

def problem_6():
    _print_title('Problem 6')
    '''
    The errors have been corrected in this code, but the errors are:
        file_to_data: 
          1. incorrect syntax for adding a dictionary to a list. Use append not +=
          2. needs to skip the first line (because it's a header row)
          3. prints the data list instead of returning it

        generate_mailers:
          4. The string.format is treating the person object as a list,
             but it's a dictionary
    '''
    def file_to_data(file):
        data = []
        counter = 0
        for line in file:
            counter += 1
            if counter == 1:
                # skips header row:
                continue
            line = line.replace('\n', '')
            cells = line.split(',')
            data.append({
                'first_name': cells[0],
                'last_name': cells[1],
                'email': cells[2]
            })
        return data

    def generate_mailers(data):
        for person in data:
            print('''
                    To: {0}
                    Dear {1},
                    Please send us some money for our important cause.
                    -- The Nature Conservancy
                '''.format(person['email'], person['first_name'])
            )

    file_path = helpers.get_file_path('contacts.csv')
    file = open(file_path, 'r')
    generate_mailers(file_to_data(file))
    file.close()

def problem_7():
    _print_title('Problem 7')

    def get_mail_providers(file):
        providers = []
        for line in file:
            line = line.replace('\n', '')
            tokens = line.split('@')
            if len(tokens) == 1:
                continue
            providers.append(tokens[-1])
        return providers
            
    file_path = helpers.get_file_path('contacts.csv')
    f = open(file_path, 'r')
    print(get_mail_providers(f))

def problem_8():
    _print_title('Problem 8')

    def get_mail_groups(file):
        my_dictionary = {}
        for line in file:
            line = line.replace('\n', '')
            cells = line.split('@')
            if len(cells) == 1:
                continue
            provider = cells[1]
            email = line.split(',')[-1]
            if my_dictionary.get(provider) is None:
                my_dictionary[provider] = []
            my_dictionary[provider].append(email)
        return my_dictionary

            
    file_path = helpers.get_file_path('contacts.csv')
    f = open(file_path, 'r')
    print(get_mail_groups(f))


def problem_9():
    _print_title('Problem 9')
    nums = [48, 50, 52, 53, 45, 33, 52, 99, 166, 510, 512, 563]
    for i in range(2, len(nums), 3):
        print(i, nums[i])

def problem_10():
    _print_title('Problem 10')
    nums = [12, 3, 8]
    for num in nums:
        print(num)
        while num > 3:
            num -= 3
            print(num)

      


# problem_1()
# problem_2()
# problem_3()
# problem_4()
# problem_5()
# problem_5_EC()
# problem_6()
# problem_7()
problem_8()
# problem_9()
# problem_10()