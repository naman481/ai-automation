import os

# Walk through a directory tree recursively
for root, dirs, files in os.walk('.'):
    print(f"Current Folder: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("-" * 30)