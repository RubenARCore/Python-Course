class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            animals = ", ".join(self.mammals)
            species_name = "Mammals"
        elif species == "fish":
            animals = ", ".join(self.fishes)
            species_name = "Fishes"
        elif species == "bird":
            animals = ", ".join(self.birds)
            species_name = "Birds"

        return f"{species_name} in {self.name}: {animals}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))