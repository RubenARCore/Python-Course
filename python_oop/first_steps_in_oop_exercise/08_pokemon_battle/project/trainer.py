from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        checker = next((x for x in self.pokemons if x.name == pokemon_name), None)
        if checker:
            self.pokemons.remove(checker)
            return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]

        for _ in self.pokemons:
            result.append(f"- {_.pokemon_details()}")

        return "\n".join(result)

    
