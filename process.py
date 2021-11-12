log_file = open("um-server-01.txt")
# assigns a variable to hold the data file


def sales_reports(log_file):
    # define the method

    for line in log_file:
    # set up a loop to iterate through the data file

        line = line.rstrip()
        # reassign the line variable to strip any whitespace for easier manipulation

        day = line[0:3]
        # targeting index 0-3 to pick out the day of the week

        if day == "Mon":
        # change your condition to check for Monday instead of Tuesday

            print(line)
            # print out each line that matches the condition above


sales_reports(log_file)
# invoke the method above 