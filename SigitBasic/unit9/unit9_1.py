
#q9_1_1
def are_files_equal(file1, file2):
    try:
        f1 = open(file1, 'r')
        f2 = open(file2, 'r')

        content1 = f1.read()
        content2 = f2.read()

        f1.close()
        f2.close()

        return content1 == content2
    except FileNotFoundError:
        return False

#q9_1_2
def sort_words(file_path):
    words = set()
    with open(file_path, 'r') as file:
        for line in file:
            line_words = line.strip().split()
            words.update(line_words)
    sorted_words = sorted(words)
    print(sorted_words)

def reverse_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            reversed_line = line.strip()[::-1]
            print(reversed_line)

def last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_lines = lines[-n:]
        for line in last_lines:
            print(line.strip())


if __name__ == '__main__':
    print(are_files_equal("c:\\vacation.txt", "c:\\work.txt"))


    file_path = "sampleFile.txt"
    action = input("Enter the action (sort, rev, or last): ")

    if action == 'sort':
        sort_words(file_path)
    elif action == 'rev':
        reverse_lines(file_path)
    elif action == 'last':
        n = int(input("Enter the number of last lines to display: "))
        last_n_lines(file_path, n)
    else:
        print("Invalid action.")