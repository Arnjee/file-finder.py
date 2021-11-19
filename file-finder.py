import os
import sys

if len(sys.argv) == 1:
    print("This is script to find files that contain your input. Run the program like this")
    print("python3 nameofscript.py <yourinput>")
    quit()

counter = 0    
search_string = sys.argv[1]

for root, dirs, files in os.walk("/", topdown=False):
    for name in files:
       if search_string.lower() in name.lower():
           print(os.path.join(root, name))
           counter += 1

    for name in dirs:
        if search_string.lower() in name.lower():
            print(os.path.join(root, name))
            counter += 1

print(f'You searched for {search_string} yieling total {str(counter)} results')