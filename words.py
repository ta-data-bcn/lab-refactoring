import random
import sys

# --- Categories list and dictionary of lists of words --- #

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


def choose_word():
    '''Chosen category to play the game. The input will be an integer. Exits the system if an invalid input is provided.
    :return: int representing the category.
    '''
    num_category = input('What category do you want to play in? Choose a category number among the following list:\n'
                         '1: animals, 2: food, 3: musical instruments, 4: car brands, 5: country capitals\n')

    if not num_category.isdigit():
        sys.exit('Please enter a valid option!')

    category_dict = {1: 'animals', 2: 'food', 3: 'music', 4: 'cars', 5: 'capitals'}

    category_name = category_dict[int(num_category)]

    return random.choice(categories_dict[category_name]).lower()
