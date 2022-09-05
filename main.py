from dicrectory_cleaner import DirectoryCleaner

def main():
    path = input("Enter path to directory you want to be cleaned: ")
    cleaner = DirectoryCleaner(path)
    cleaner.clean_directory()
    print(path + " has been cleaned!")

if __name__ == '__main__':
    main()