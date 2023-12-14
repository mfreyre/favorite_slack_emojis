
#!/bin/bash

# Change to the directory containing the files
cd meow

for file in *; do
    newname=$(echo $file | sed -e 's/ ([0-9])//')
    # Rename the file
    mv "$file" "$newname"
done
