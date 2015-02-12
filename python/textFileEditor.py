import datetime

def insertDateAtFirstLine(filename):
    """Takes any txt file as an argument and replaces the first line of the file with the date and time.
    Coder notes: Re-write to ADD to beginning of file instead of replacing"""
    with open(filename, "r") as readFile:  #Open file
        lines = readFile.readlines() #Store each line of file into a list
        #Store date into today and format it
        today = datetime.datetime.now().strftime('%B %d, %Y %I:%M%p') 
        lines[0] = "\t\t\t   {date}\n".format(date=today) #Replace first line of the file
        with open(filename, "w") as writeFile: #Open same file to write into
            #Re-write new lines into new file
            for line in lines: 
                writeFile.write(line)

#if __name__ == "__main__":
#    insertDateAtFirstLine("kanye.txt")
