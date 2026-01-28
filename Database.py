'''

Student ID: F325508

Database Module

This module provides the key functionality for all other modules when interacting with the files.
This includes all the functions required to manipulate files.

Key Features:
- Appends lists and lines to a file
- Writes lists and lines to a file
- Converts lists to strings and writes to file
- Reads a file and converts lists to strings

Fucntions:
- AppendLine_File(Line, file_name): Accepts a line and a file and
appends the line to the end of the file
- Read_File(file_name): Accepts any file and reads the file, returning the file
as a list of lists.
- WriteLine_File(Line, file_name): Accepts a line and a file and
overwrites the contents in the file with the single line
- WriteList_File(List, file_name): Accepts a list and a file and converts
the list to a string before overwriting the contents in the file with the list

'''
def AppendLine_File(Line, file_name):
    """
    Appends a single line to the last line of a file.

    Parameters:
    - Line (str): The line to append to the file.
    - file_name (str): The name of the file to which the line will be appended.

    Returns:
    - None

    Opens the specified file in 'append' mode ("a"), writes the provided line to the file,
    and closes the file after writing.
    """
    file = open(file_name,"a")
    file.write("\n"+Line)
    file.close()
    
def Read_File(file_name):
    """
    Reads a file and returns its content as a list of rows.

    Parameters:
    - file_name (str): The name of the file to be read.

    Returns:
    - List_of_rows_in_file (list): A list containing rows of the file content.

    Opens the specified file in 'read' mode ("r"), reads each line, strips the newline character,
    splits the lines by comma (',') delimiter, and appends them to a list. Returns the list
    containing the rows of the file content after closing the file.
    """

    file = open(file_name, "r")
    List_of_rows_in_file = []
    while True:
        line = file.readline()
        if line == '':  
            break
        else:
            List_of_rows_in_file.append(line.replace("\n","").split(","))
    file.close()
    return List_of_rows_in_file


def WriteList_File(List, file_name):
    """
    This function writes the input list to a file, converting elements of the list to strings, overwriting the file.

    Parameters:
    - List (list): The list whose elements will be written to the file.
    - file_name (str): The name of the file to which the list elements will be written.

    Returns:
    - None

    Opens the specified file in 'write' mode ("w"), iterates through each element in the list,
    converts each element to a string, formats the output by removing brackets, quotes,
    spaces, and trailing commas, and writes each formatted element as a line to the file.
    Closes the file after writing.
    """
    file = open(file_name,"w")
    for i in List:
        i = str(i)
        file.write(i.replace("[","").replace("\'","").replace("]","")
                   .replace(", \'",",").replace(" ","")+"\n")
    file.close()

if __name__ == "__main__":
    # Test cases or demonstration for the functions in Database module


    # Demonstrating Read_File function
    print("Testing AppendLine_File function:")
    Subscriptions = Read_File("Subscription_Info.txt")
    print("Subscription information list: " +"\n",Subscriptions)
    print("Function works correctly as you can see above")
    
    # Demonstrating AppendLine_File function
    print("Testing AppendLine_File function:")
    AppendLine_File("PGA04,11-12-2023,NULL,GOBL","Rental.txt")
    RentalFile = Read_File("Rental.txt")
    print("Last line of rental file:",RentalFile[-1])
    print("Function works correctly as you can see above")

