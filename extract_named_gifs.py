import os
import shutil

dir_name = "happy"
pokemon_names = ['raichu', 'pikachu', 'charmander', 'bulbasaur', 'squirtle']

# Directory to search for files (replace with your directory)
source_directory = 'gif_emojis/'

# Subdirectory to move Pokémon files to
pokemon_directory = os.path.join(source_directory, f'gif_emojis/{dir_name}')

# Create the 'pokemon' subdirectory if it does not exist
if not os.path.exists(pokemon_directory):
    os.makedirs(pokemon_directory)

# Function to check if a file name contains any Pokémon name
def is_pokemon_file(filename):
    return any(pokemon in filename.lower() for pokemon in pokemon_names)

# Search and move Pokémon files
for filename in os.listdir(source_directory):
    if is_pokemon_file(filename):
        source_path = os.path.join(source_directory, filename)
        destination_path = os.path.join(pokemon_directory, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("Finished moving Pokémon files.")

