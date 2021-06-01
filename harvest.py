############
# Part 1   #
############


class MelonType():
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        'Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint')

    cas = MelonType(
        'Casaba', 'cas', 2003, 'orange', False, False)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')

    cren = MelonType(
        'Crenshaw', 'cren', 1996, 'green', False, False)
    cren.add_pairing('prosciutto')

    yw = MelonType(
        'Yellow Watermelon', 'yw', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')

    all_melon_types.extend([musk, cas, cren, yw])

    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'\n{melon.name} pairs with')

        for pairing in melon.pairings:
            print(f'- {pairing}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_dict = {}

    for melon in melon_types:
        melons_dict[melon.code] = melon

    return melons_dict

############
# Part 2   #
############

class Melon():
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
        """Initialize a melon in a melon harvest"""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Determine if melon is able to be sold"""
        
        if self.color_rating > 5 and self.shape_rating > 5 and self.field != 3:
            return True
        return False


melons_by_id = make_melon_type_lookup(melon_types)

def make_melons(melon_types):           #call with make_melon_types() function
    """Returns a list of Melon objects."""

    all_melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
  
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    all_melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, 
                            melon_6, melon_7, melon_8, melon_9])

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        msg = f'Harvested by {melon.harvested_by} from Field {melon.field}'

        if melon.is_sellable():
            print(f'{msg} (CAN BE SOLD)')
        else:
            print(f'{msg} (NOT SELLABLE)')

#pass in make_melons(melon_types) as list of melon objects


def make_melon_objects(filename):

    with open(filename) as f:
        for line in f:
            l = line.rstrip().split(' ')

            shape, color, melon_type, harvested_by, field = l[1], l[3], l[5], l[8], l[11]
           
            melon_object = Melon(melons_by_id[melon_type], 
                                shape, color, field, harvested_by)
           
            print(melon_object)

