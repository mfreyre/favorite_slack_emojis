import os

def replace_underscores_with_hyphens(directory):
    for filename in os.listdir(directory):
        if "_" in filename:
            new_filename = filename.replace("_", "-")
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Replace 'your_directory_path' with the path of your directory
directory_path = 'gif_emojis/unsorted'
replace_underscores_with_hyphens(directory_path)
