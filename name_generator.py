import random
from names import get_random_name

# NPC Data Pools
races = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Tiefling", "Dragonborn", "Half-Orc", "Half-Elf"]
classes = ["Fighter", "Rogue", "Wizard", "Cleric", "Ranger", "Paladin", "Bard", "Warlock", "Monk", "Druid"]
personality_traits = [
    "Brave and fearless", "Cunning and deceptive", "Kind-hearted and generous", "Stoic and reserved", 
    "Hot-tempered and impulsive", "Cheerful and optimistic", "Mysterious and aloof", "Loyal and protective"
]
backgrounds = [
    "Once a noble, now a fugitive seeking redemption.",
    "A former soldier who lost everything in war and now wanders the world.",
    "Raised by thieves, they know the streets like the back of their hand.",
    "A scholar obsessed with uncovering ancient secrets.",
    "A reclusive hermit drawn into the affairs of the world once more.",
    "Exiled from their homeland for a crime they did not commit.",
    "A traveling performer who hides a dangerous past.",
    "Once a cultist, now trying to undo the horrors they helped create."
]

def generate_npc():
    """Generates a random NPC with a name, race, class, personality, and backstory."""
    name = get_random_name()
    race = random.choice(races)
    npc_class = random.choice(classes)
    personality = random.choice(personality_traits)
    backstory = random.choice(backgrounds)

    npc = {
        "Name": name,
        "Race": race,
        "Class": npc_class,
        "Personality": personality,
        "Backstory": backstory
    }

    return npc
