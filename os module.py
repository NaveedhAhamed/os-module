
import os
import platform
import shutil

# ==========================================
# 1. BASIC OS INFORMATION
# ==========================================

print("\n========== 1. OS INFORMATION ==========")

# Get the operating system name
print("Operating system:", os.name)

# Get more detailed system information
print("System:", platform.system())
print("OS release:", platform.release())
print("Python running on:", platform.python_version())

# Get the current working directory
print("Current directory:", os.getcwd())


# ==========================================
# 2. CHANGE WORKING DIRECTORY
# ==========================================

print("\n========== 2. WORKING DIRECTORY ==========")

# Change the current directory
# os.chdir(r"C:\Users\YourName\Desktop")

# The line above is commented out for safety.
# Replace YourName with your actual Windows username
# and remove # if you want to use it.

print("Python is currently working in:", os.getcwd())


# ==========================================
# 3. CREATE AND LIST DIRECTORIES
# ==========================================

print("\n========== 3. DIRECTORIES ==========")

# Create a directory if it does not already exist
os.makedirs("os_demo/subfolder", exist_ok=True)

# List files and folders in the current directory
print("Items in current directory:")
print(os.listdir("."))

# Check whether a path exists
print("Does os_demo exist?", os.path.exists("os_demo"))

# Check whether it is a directory
print("Is os_demo a directory?", os.path.isdir("os_demo"))

# Check whether it is a file
print("Is os_demo a file?", os.path.isfile("os_demo"))


# ==========================================
# 4. FILE OPERATIONS
# ==========================================

print("\n========== 4. FILE OPERATIONS ==========")

# Create a text file and write something into it
with open("os_demo/example.txt", "w", encoding="utf-8") as file:
    file.write("Hello! This file was created using Python.\n")
    file.write("We are learning the OS module.")

print("File created successfully.")

# Read the file
with open("os_demo/example.txt", "r", encoding="utf-8") as file:
    print("File contents:")
    print(file.read())

# Get file size in bytes
print(
    "File size:",
    os.path.getsize("os_demo/example.txt"),
    "bytes"
)

# Rename a file
os.rename(
    "os_demo/example.txt",
    "os_demo/renamed.txt"
)

print("File renamed successfully.")


# ==========================================
# 5. PATH OPERATIONS
# ==========================================

print("\n========== 5. PATH OPERATIONS ==========")

path = os.path.join("os_demo", "renamed.txt")

print("Combined path:", path)

# Extract parts of a path
print("Directory:", os.path.dirname(path))
print("Filename:", os.path.basename(path))
print("Filename without extension:", os.path.splitext(path)[0])
print("File extension:", os.path.splitext(path)[1])

# Convert a path into an absolute path
print("Absolute path:", os.path.abspath(path))

# Normalize a path
print("Normalized path:", os.path.normpath(path))


# ==========================================
# 6. ENVIRONMENT VARIABLES
# ==========================================

print("\n========== 6. ENVIRONMENT VARIABLES ==========")

# Read an environment variable
print("Username:", os.environ.get("USERNAME", "Not available"))

# Get the home directory safely across operating systems
print("Home directory:", os.path.expanduser("~"))

# Get the temporary directory
print("Temporary directory:", os.getenv("TEMP") or os.getenv("TMPDIR"))

# List environment variable names
print("Some environment variables:")
print(list(os.environ.keys())[:10])


# ==========================================
# 7. WALK THROUGH DIRECTORIES
# ==========================================

print("\n========== 7. WALK THROUGH DIRECTORIES ==========")

# Display directories and files inside os_demo
for folder, subfolders, files in os.walk("os_demo"):
    print("Current folder:", folder)
    print("Subfolders:", subfolders)
    print("Files:", files)


# ==========================================
# 8. FILE AND DIRECTORY INFORMATION
# ==========================================

print("\n========== 8. FILE INFORMATION ==========")

file_path = "os_demo/renamed.txt"

# Get detailed information about the file
info = os.stat(file_path)

print("Size:", info.st_size, "bytes")
print("Last modified timestamp:", info.st_mtime)
print("Permissions:", info.st_mode)


# ==========================================
# 9. USE SHUTIL WITH OS
# ==========================================

print("\n========== 9. SHUTIL OPERATIONS ==========")

# shutil provides higher-level file and directory tools.

# Copy the file
shutil.copy(
    "os_demo/renamed.txt",
    "os_demo/copied.txt"
)

print("File copied successfully.")

# Get disk usage for the current drive/filesystem
disk = shutil.disk_usage(os.getcwd())

print("Total disk space:", disk.total // (1024 ** 3), "GB")
print("Used disk space:", disk.used // (1024 ** 3), "GB")
print("Free disk space:", disk.free // (1024 ** 3), "GB")


# ==========================================
# 10. RUN AN OS COMMAND
# ==========================================

print("\n========== 10. OS COMMANDS ==========")

# Run a simple command using os.system()
# The command differs between operating systems.

if os.name == "nt":
    print("Windows directory listing:")
    os.system("dir")
else:
    print("Directory listing:")
    os.system("ls")

# Note:
# For more advanced command execution, prefer subprocess.
# Avoid running commands built from untrusted user input.


# ==========================================
# 11. FILE DESCRIPTORS AND PROCESS ID
# ==========================================

print("\n========== 11. PROCESS INFORMATION ==========")

# Get the current Python process ID
print("Current process ID:", os.getpid())

# Get the parent process ID
print("Parent process ID:", os.getppid())


# ==========================================
# 12. DELETE A FILE
# ==========================================

print("\n========== 12. DELETE A FILE ==========")

# Remove a specific file
os.remove("os_demo/copied.txt")

print("Copied file deleted.")

# Remove an empty directory
# os.rmdir("os_demo/subfolder")

# The directory is left in place so you can explore it.


# ==========================================
# 13. ERROR HANDLING
# ==========================================

print("\n========== 13. ERROR HANDLING ==========")

try:
    os.mkdir("os_demo")
except FileExistsError:
    print("The directory already exists.")
except OSError as error:
    print("An operating system error occurred:", error)


# ==========================================
# END
# ==========================================

print("\n========== PROGRAM FINISHED ==========")
print("Explore the os_demo folder to see the results.")
