import random
import sys

categories = ['animals', 'food', 'musical instruments', 'car brands', 'country capitals']

categories_dict = \
    {'animals':
     ['antelope', 'bear', 'cat', 'dog', 'elephant', 'fox', 'giraffe', 'hyena', 'iguana', 'jaguar', 'kangaroo',
      'llama', 'monkey', 'turtle', 'octopus', 'bee', 'rat', 'snake', 'tiger', 'unicorn', 'whale', 'zebra'],
     'food':
     ['bagel', 'beans', 'biscuit', 'bread', 'broth', 'burger', 'butter', 'cake', 'candy', 'caramel', 'caviar',
      'cheese', 'chili', 'chocolate', 'cocoa', 'coffee', 'cookie', 'croissant', 'dessert', 'dish',
      'eggs', 'fish', 'flour', 'hamburger', 'ice', 'juice', 'ketchup', 'kitchen', 'margarine', 'mayonnaise',
      'meat', 'mousse', 'muffin', 'mushroom', 'noodle', 'oil', 'olive', 'omelette', 'pasta', 'pastry', 'pie',
      'pizza', 'pudding', 'raclette', 'rice', 'salad', 'salsa', 'sandwich', 'sauce', 'soup', 'steak', 'tartar',
      'toast', 'waffle', 'yogurt'],
     'music':
     ['Accordion', 'Banjo', 'Bongo', 'Cello', 'Clarinet', 'Cymbal', 'Drums', 'Flute', 'Gong', 'Guitar',
      'Harmonica', 'Harp', 'Harpsichord', 'Mandolin', 'Melodica', 'Oboe', 'Ocarina', 'Organ', 'Piano',
      'Piccolo', 'Recorder', 'Saxophone', 'Sitar', 'Synthesizer', 'Tambourine', 'Timpani', 'Triangle',
      'Trombone', 'Trumpet', 'Tuba', 'Ukulele', 'Viola', 'Violin', 'Xylophone', 'Zither'],
     'cars':
     ['Audi', 'Bentley', 'Benz', 'BMW', 'Bugatti', 'Cadillac', 'Chevrolet',
      'Chrysler', 'Citroen', 'Corvette', 'Dacia', 'Daewoo', 'Dodge', 'Ferrari', 'Fiat', 'Ford', 'Honda',
      'Hummer', 'Hyundai', 'Jaguar', 'Jeep', 'KIA', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus',
      'Lotus', 'Martini', 'Maserati', 'Mazda', 'McLaren', 'Mercedes', 'Mini', 'Mitsubishi',
      'Nissan', 'Opel', 'Peugeot', 'Pontiac', 'Porsche', 'Renault', 'Saab',
      'Seat', 'Skoda', 'Smart', 'Subaru', 'Suzuki', 'Toyota', 'Volkswagen', 'Volvo'],
     'capitals':
     ['KABUL', 'TIRANA', 'ALGIERS', 'LUANDA', 'YEREVAN', 'CANBERRA', 'VIENNA', 'BAKU', 'NASSAU',
      'MANAMA', 'DHAKA', 'BRIDGETOWN', 'MINSK', 'BRUSSELS', 'BELMOPAN', 'THIMPHU', 'SUCRE', 'SARAJEVO',
      'GABORONE', 'BRASILIA', 'SOFIA', 'OUAGADOUGOU', 'BUJUMBURA', 'PRAIA', 'YAOUNDE', 'OTTAWA',
      'BANGUI', 'SANTIAGO', 'BEIJING', 'BOGOTA', 'MORONI', 'KINSHASA', 'YAMOUSSOUKRO',
      'ZAGREB', 'HAVANA', 'NICOSIA', 'PRAGUE', 'COPENHAGEN', 'ROSEAU', 'QUITO', 'CAIRO', 'MALABO', 'ASMARA',
      'TALLINN', 'MBABANE', 'PALIKIR', 'SUVA', 'HELSINKI', 'PARIS', 'LIBREVILLE', 'BANJUL', 'TBILISI', 'BERLIN',
      'ACCRA', 'ATHENS', 'CONAKRY', 'BISSAU', 'GEORGETOWN', 'TEGUCIGALPA', 'BUDAPEST', 'REYKJAVIK', 'NEW DELHI',
      'JAKARTA', 'TEHRAN', 'BAGHDAD', 'DUBLIN', 'ROME', 'KINGSTON', 'TOKYO', 'AMMAN', 'ASTANA', 'NAIROBI',
      'PRISTINA', 'BISHKEK', 'VIENTIANE', 'RIGA', 'BEIRUT', 'MASERU', 'MONROVIA', 'TRIPOLI',
      'VADUZ', 'VILNIUS', 'LUXEMBOURG', 'SKOPJE', 'ANTANANARIVO', 'LILONGWE', 'MALE', 'BAMAKO', 'VALLETTA',
      'MAJURO', 'NOUAKCHOTT', 'CHISINAU', 'MONACO', 'ULAANBAATAR', 'PODGORICA', 'RABAT', 'MAPUTO',
      'WINDHOEK', 'KATHMANDU', 'AMSTERDAM', 'WELLINGTON', 'MANAGUA',
      'NIAMEY', 'ABUJA', 'PYONGYANG', 'OSLO', 'MUSCAT', 'ISLAMABAD', 'NGERULMUD',
      'ASUNCION', 'LIMA', 'MANILA', 'WARSAW', 'LISBON', 'DOHA', 'BRAZZAVILLE', 'BUCHAREST', 'MOSCOW',
      'KIGALI', 'BASSETERRE', 'CASTRIES', 'KINGSTOWN', 'APIA', 'RIYADH', 'DAKAR', 'BELGRADE', 'VICTORIA',
      'FREETOWN', 'SINGAPORE', 'BRATISLAVA', 'LJUBLJANA', 'HONIARA', 'MOGADISHU', 'SEOUL', 'JUBA', 'MADRID',
      'KHARTOUM', 'PARAMARIBO', 'STOCKHOLM', 'BERN', 'DAMASCUS', 'DUSHANBE', 'DODOMA', 'BANGKOK', 'DILI', 'LOME',
      'TUNIS', 'ANKARA', 'ASHGABAT', 'FUNAFUTI', 'KAMPALA', 'KIEV', 'LONDON', 'MONTEVIDEO', 'TASHKENT',
      'CARACAS', 'HANOI', 'LUSAKA', 'HARARE']}

draw_1 = '''                           |------_
                                 |_| 
                                --|--
                                  |                                          
                                 / \\'''
# (n = 5)

draw_2 = '''                           |------
                                  |
                                  _
                                 |_| 
                                --|--
                                  |                                          
                                 / \\'''
# (n = 7)

draw_3 = '''                           |------
                                  |
                                  |
                                  |
                                  |
                                  _
                                 |_| 
                                --|--
                                  |                                          
                                 / \\'''
# (n = 9)


def config_game():
    num_category = input('What category do you want to play in? Choose a category number among the following list:\n'
                         '1: animals, 2: food, 3: musical instruments, 4: car brands, 5: country capitals\n')

    if not num_category.isdigit():
        sys.exit('Please enter a valid option!')

    category_dict = {1: 'animals', 2: 'food', 3: 'music', 4: 'cars', 5: 'capitals'}

    category_name = category_dict[int(num_category)]

    return random.choice(categories_dict[category_name]).lower()


def display_word():
    print('\nUsed letters: ', used_letters)
    printed_word = ''
    for i in word:
        if i in guessed_letters:
            printed_word += i + ' '
        else:
            printed_word += '_ '
    print(printed_word)


def draw_hangman():
    if max_mistakes == 5:
        for i in range(mistakes):
            print(draw_1.split('\n')[i])
    elif max_mistakes == 7:
        for i in range(mistakes):
            print(draw_2.split('\n')[i])
    else:
        for i in range(mistakes):
            print(draw_3.split('\n')[i])


def calc_max_mistakes():
    global max_mistakes
    if 3 < len(word) < 6:
        max_mistakes = 5
    elif 5 < len(word) < 9:
        max_mistakes = 7
    else:
        max_mistakes = 9


def play():
    global mistakes
    calc_max_mistakes()
    for chance in range(len(word)*2):
        if mistakes == max_mistakes:
            break
        if not word_letters:
            print('Congratulations, you guessed the word!')
            break
        display_word()
        guess = input('\nPlease choose a letter: \n')
        if not guess.isalpha():
            return 'You have to enter a valid letter!!!'
        if guess in word_letters:
            word_letters.remove(guess)
            used_letters.append(guess)
            guessed_letters.append(guess)
        else:
            used_letters.append(guess)
            mistakes += 1
        draw_hangman()
    if word_letters:
        print(f'Game over! The word was {word}')


word = config_game()
word_letters = set(word)
used_letters = []
guessed_letters = []
mistakes = 0
diff = ''
max_mistakes = 0

play()
