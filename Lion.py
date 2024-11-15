# Import the Animal class from the Animal module
from Animal import Animal

class Lion(Animal):
    # create a static class variable to keep track of the number of lions created
    numOfLions = 0

    # Create the lion sound
    lion_sound = " roar...roar "

    # Create a list of lion names.
    list_of_lion_names = []

    file_path = r'animalNames.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num == 7: # Lion names are on the 7th line
                list_of_lion_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # Increment the static variable numOfLions when a new Lion object is created
        Lion.numOfLions += 1

        # Generate the unique ID
        self.gen_unique_id()

        # Call the constructor of the parent class (Animal) with 'Hyena' as the species
        super().__init__("lion", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.lion_sound

    # the lion object will call this method to get an unused lion name. pop() will remove the first element from
    #   the list_of_lion_names[]
    def get_lion_name(self):
        return self.list_of_lion_names.pop(0)

    def gen_unique_id(self):
        # Assuming the unique ID is composed of the species abbreviated and the number of lions
        self.animal_id = "Li" + str(Lion.numOfLions).zfill(2)

