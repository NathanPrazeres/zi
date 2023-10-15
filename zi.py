import os

path = os.getcwd()
print("The current directory is " + path + ".")
i = input("This directory or root? (Press ENTER for root or type 'curr' for the current dir.) ")
if i == 'curr':
    pass
elif i == '':
    path = '/home'
else: exit(0)

# Delete all Zone.Identifier files in directory and subdirectories.
def delete_identifiers_in_path(mypath, all):
    counter = 0
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        for filename in filenames:
            if len(filename) > 16 and filename[-16:] == ":Zone.Identifier":
                if (os.path.exists(dirpath + "/" + filename)):
                    os.remove(dirpath + "/" + filename)
                    counter += 1
                    print("Removed " + filename)
                else:
                    print("File " + filename + " does not exist.")
        if dirnames == []:
            break
        elif all:
            for dirname in dirnames:
                if dirname == "code" or dirname[0] == ".":
                    continue
                counter += delete_identifiers_in_path(dirpath + "/" + dirname, all)
        break
    return counter

c = input("Do you wish to also delete Zone.Identifier files in subdirectories? (Press ENTER or type 'y' for yes, or type 'n' for no.) ")
if c == '' or c == 'y':
    all = True
elif c == 'n':
    all = False
else: exit(0)
print(delete_identifiers_in_path(path, all))