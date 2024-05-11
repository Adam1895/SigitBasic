
#q9_2_!
def copy_file_content(source, destination):
    try:
        with open(source, 'r') as source_file:
            content = source_file.read()

        with open(destination, 'w') as dest_file:
            dest_file.write(content)
    except FileNotFoundError:
        print(f"File {source} not found.")
    except IOError:
        print(f"An error occurred while copying the file.")


#q9_2_3
def who_is_missing(file_name):
    try:
        with open(file_name, 'r') as file:
            numbers = file.read().split(',')
            numbers = [int(num) for num in numbers]

            n = len(numbers) + 1
            missing_num = sum(range(1, n + 1)) - sum(numbers)

            with open('found.txt', 'w') as output_file:
                output_file.write(str(missing_num))

            return missing_num
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except ValueError:
        print("Invalid numbers in the file.")

if __name__ == '__main__':
    copy_file_content("sampleFile.txt", "paste.txt")
    print(who_is_missing("findMe.txt"))