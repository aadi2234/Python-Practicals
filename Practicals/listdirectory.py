import os

# Function to create a directory if it doesn't exist
if not os.path.exists("first_dir"):
    os.mkdir("first_dir")

# Get the current working directory
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# Print contents of the current directory
print("Contents of the current directory:")
print(os.listdir(current_dir))

# Rename the directory
if not os.path.exists("renamed_dir"):
    os.rename("first_dir", "renamed_dir")

# Change directory to the renamed directory
os.chdir("renamed_dir")
print("Changed to directory:", os.getcwd())

# Check if the renamed directory exists
if os.path.exists("renamed_dir"):
    print("Directory exists")

# Traverse the directory using os.walk
print("Using os.walk to traverse the directory:")
for root, dirs, files in os.walk("D:\\KKWP\\SEM-6\\PWP\\Practicals"):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
