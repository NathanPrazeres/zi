import os

# Delete all Zone.Identifier files in directory and subdirectories.
def delete_identifiers_in_path(path, all):
    counter = 0
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if len(filename) > 16 and filename[-16:] == ':Zone.Identifier':
                if (os.path.exists(dirpath + '/' + filename)):
                    os.remove(dirpath + '/' + filename)
                    counter += 1
                    print('Removed ' + filename)
                else:
                    print('File ' + filename + ' does not exist.')
        if dirnames == []:
            break
        elif all:
            for dirname in dirnames:
                if dirname[0] == '.':
                    continue
                counter += delete_identifiers_in_path(dirpath + '/' + dirname, all)
        break
    return counter

if __name__ == '__main__':
    path = os.getcwd()

    print('The current directory is ' + path + '.')
    i = input('Begin in current or root directory? [ROOT/here] ')
    if i.lower() == 'here':
        pass
    elif i == '' or i.lower() == 'root':
        path = '/home'
    else:
        print('Invalid input. Aborting...')
        exit(0)

    c = input("Do you wish to also delete Zone.Identifier files in subdirectories? [Y/n] ")
    if c == '' or c.lower() == 'y':
        all = True
    elif c.lower() == 'n':
        all = False
    else:
        print('Invalid imput. Aborting...')
        exit(0)

    print(delete_identifiers_in_path(path, all))
