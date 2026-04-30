import os  # Import os module

# Specify the directory path
path = "C:\\Users\\hp\\Desktop\\Python\\Chapter1"

# Get list of files and directories
contents = os.listdir(path)

# Print each item
print("Contents of directory:")
for item in contents:
    print(item)