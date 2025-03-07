import random

# Name Pools for Different Races
human_names = ["Alden", "Marianne", "Edgar", "Felix", "Sophie", "Gideon"]
elf_names = ["Thalorin", "Aeliana", "Eldrin", "Sylvara", "Vaelith", "Loriel"]
dwarf_names = ["Brunhilda", "Thrain", "Durin", "Brom", "Gilda", "Korgan"]
halfling_names = ["Pip", "Merric", "Rosie", "Tobias", "Lyle", "Clover"]

def get_random_name():
    """Generates a random name from different racial name pools."""
    all_names = human_names + elf_names + dwarf_names + halfling_names
    return random.choice(all_names)
