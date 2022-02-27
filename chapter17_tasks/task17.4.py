"""
Task 17.4
Create function write_last_log_to_csv.
Function arguments:
* source_log - the name of the csv file from which the data is read (mail_log.csv)
* output - the name of the csv file into which the result will be written
The function returns None.
The write_last_log_to_csv function processes the csv file mail_log.csv.
The mail_log.csv file contains the logs of the username change.
User cannot change email, only username.
The write_last_log_to_csv function should select from the mail_log.csv file
only the most recent entries for each user and write them to another csv file.
In the output file, the first line should be the column headers as in the source_log file.
For some users, there is only one record, and then it is necessary to write
to the final file only her. For some users, there are multiple entries with
different names. For example, a user with email c3po@gmail.com changed his
username several times:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24
Of these three records, only one should be written to the final file - the most recent:
C-3PO,c3po@gmail.com,16/12/2019 17:24
It is convenient to use datetime objects from the datetime module
for comparing dates. To make it easier to work with dates,
the convert_str_to_datetime function has been created - it converts a date
string in the format 11/10/2019 14:05 into a datetime object.
The resulting datetime objects can be compared with each other.
The second function, convert_datetime_to_str, does the opposite — it turns
a datetime object into a string.
It is not necessary to use the functions convert_str_to_datetime and convert_datetime_to_str
"""
from pprint import pprint
import csv
import datetime

"""
lambda arguments : expression
"""


def convert_str_to_datetime(datetime_str):
    """
    Converts a date string formatted as 11/10/2019 14:05 to a datetime object.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, final_output):
    with open(source_log) as f:
        data = list(csv.reader(f))  # add everything to list
        headers = data [ 0 ]  # grab list for header
    send_to_dictionary = {}  # create empty dictionary
    sorted_by_date = sorted(data [ 1: ], key=lambda x: convert_str_to_datetime(x [ 2 ]))  # sort the list with help of
    # lambda function ,at the end list will be sorted based on dates ,since x[2] is taking 3rd index which date
    print(sorted_by_date)
    for name, email, date in sorted_by_date:
        send_to_dictionary [ email ] = (name, email, date)  # here all data are stored in dictionary ,remember only
        # last email address will be taken since we will have multiple email address due to multiple username change
        # and only last one will be taken because it was sorted above based on date function
        print(send_to_dictionary)
    with open(final_output, "w") as final_output:
        writer = csv.writer(final_output)
        writer.writerow(headers)  # write firstly header to new csv file.
        for row in send_to_dictionary.values():  # iterate for values in dictionary ,not the keys.
            writer.writerow(row)  # write tuples to csv


if __name__ == "__main__":
    pprint(write_last_log_to_csv("mail_log.csv", "final_log.csv"))
