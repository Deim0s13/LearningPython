def open_read_file(file):
    """ Opens the given file, reads each line and prints to the console.
    Closes the given file"""

    # Open the given file in read mode
    f = open(file, "r")
    print(type(f)) # print the type of the stream f

    cnt = 0

    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

        cnt += 1

    print('')
    print('there are', cnt, 'lines in the file')

    f.close()

def open_read_append_new_file(file1, file2):
    """ Opens the first file, and reads all the lines into a list.
    Reverses the lines, and appends them to the second file."""

    # Open the first file in read mode
    with open(file1) as fin:

        # Read all the lines into a list
        lst = fin.readlines()

        # Reverse the list
        lst.reverse()

        # Open second file for appending
        fout = open(file2, "a")

        # write reversed lines to second file
        fout.writelines(lst)

        # Close the second file
        fout.close()

def open_read_append_same_file(file):
    """ Opens the given file and reads all lines as a list.
    Appends lines in the same file."""

    # Open the file for reading and writing
    f = open(file, "r+")

    # Read all lines into a list
    lst = f.readlines()

    # Updating list for appending back to same file
    lst.insert(0, '\n')
    lst.insert(0, 'here is some new text')
    lst.insert(0, '\n')

    # Append the lines
    f.writelines(lst)

    # Close file
    f.close()

def open_read_write_new_file(file1, file2):
    """ Opens the first file and reads all the text as a string.
    Copies or writes all the text to the second file."""

    # Open the first file for reading
    with open(file1) as fin:

        # Reads all lines as a single string
        text = fin.read()

        # Open second file in write mode
        fout = open(file2, "w")

        # Write single string to second file
        fout.write(text)

        # Close second file
        fout.close()


def main():

    # open_read_file('news.txt')
    # open_read_append_new_file('news.txt', 'news_out.txt')
    # open_read_append_same_file('news.txt')
    open_read_write_new_file('news.txt', 'news_copy.txt')

if __name__ == '__main__':
    main()