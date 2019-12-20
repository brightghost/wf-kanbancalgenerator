#! /bin/python3

import datetime as dt
import sys
import subprocess

def run():
    # generate a formatted calendar from arguments provided on command line
    for a in sys.argv:
        if a == "--help" or a == "-h":
            # a help flag found anywhere prints usage and exits
            print('''Usage:

                kanban-generator.py
                    Default: generate 12 month's of formatted calendar from today's date
                kanban-generator.py 2020-2-5
                    Generate a formatted calendar starting at today's date and ending at the provided date
                kanban-generator.py 2020-2-5 2020-2-28
                    Generate a formatted calendar encompassing the start and end dates provided.

                kanban-generator.py (-h|--help)
                    Print this usage information and exit

                ''')
            sys.exit(0)
    if len(sys.argv) == 3:
        # kanban-generator ISO-start-date ISO-end-date
        print("argv - ", str(sys.argv[1]))
        start_date = kbDate.fromisoformat(sys.argv[1])
        end_date = kbDate.fromisoformat(sys.argv[2])
    elif len(sys.argv) == 2:
        # kanban-generator ISO-end-date
        #   generates a calendar from today--ISO-end-date
        start_date = kbDate.today()
        end_date = kbDate.fromisoformat(sys.argv[1])
    elif len(sys.argv) == 1:
        # defualt: generate 12-mo of data starting today
        start_date = kbDate.today()
        assert isinstance(start_date, kbDate)
        end_date = start_date + dt.timedelta(365)
        assert isinstance(end_date, kbDate)
    print("generating cal for dates " + str(start_date) + "--" + str(end_date) + "...\n")
    arr = create_date_array(start_date, end_date)
    print_date_array(arr)
    copy_date_array(arr)

def create_date_array(start_date, end_date):
    output_arr = []
    d = start_date
    assert isinstance(d, kbDate)
    last_mo = None
    last_yr = None

    ### assemble the output array ###

    # first mo header:
    # output_arr.append(d.get_month_string())
    while d <= end_date:
        assert isinstance(d, kbDate)
        if d.year != last_yr:
            output_arr.append(d.get_year_string())
            last_yr = d.year
        if d.month != last_mo:
            output_arr.append(d.get_month_string())
            last_mo = d.month
        # date
        output_arr.append("\t" + d.get_date_string())
        d = d + dt.timedelta(1) # increment day
    return output_arr

def print_date_array(array):
    '''Prints date array to terminal.'''
    for i in array:
        print(i)

def copy_date_array(array):
    # https://stackoverflow.com/a/51977242/2920201
    ''' testing shows workflowy ui likes html:
            $ xclip -selection clipboard -o -t TARGETS
            [...]
            text/html'''
    string = ""
    for l in array:
        string = string + l + "\n"

    if str(type(string)) == "<class 'str'>":
        string = bytearray(string, 'utf8')
    subprocess.Popen(['xclip', '-selection', 'clipboard', '-t', 'text/html'], stdin=subprocess.PIPE).communicate(string)


class kbDate(dt.date):
    """A date object with methods for printing in our preferred format."""
    def __init__(self, *args, **kwargs):
        # super(kbDate, self).__init__()
        self.weekday_names = [
#            "M","Tu","W","Th","F","St","Sn"]
#            "m","t","w","th","f","st","s"]
            "Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    #https://stackoverflow.com/a/20288506/2920201
    def __add__(self, other):
         res = super(kbDate, self).__add__(other)
         return type(self)(res.year, res.month, res.day)

    def get_dow_string(self):
        '''Return a formatted string representating of the day of week.'''
        return self.weekday_names[self.weekday()]

    def get_year_string(self):
        '''Return a formatted string for the year header of this object.'''
        return "<b>" + self.strftime("%Y") + "</b>"

    def get_month_string(self):
        '''Return a formatted string for the month header of this object.'''
        return "<b>" + self.strftime("%B") + "</b>"

    def get_date_string(self):
        '''Return a formatted string for the date listing of this object.
        Ex:
            #12-19 Th
            #12-20 F
            #12-21 St
            #12-22 Sn
            #12-23 M
            '''
        return("<b><i>#" + str(self.month) + "-" + str(self.day) + " " + self.get_dow_string() + "</i></b>")

    def fromisoformat(self, isodate):
        '''Returns a kbDate generated from the provided isodate (YYYY-MM-DD)'''
        # datetime.date.fromisoformat() : new in python3.7

        # strptime returns a datetime
        date_obj = dt.strptime(isodate, "%Y-%m-%d").date()

        return type(self)(date_obj.year, date_obj.month, date_obj.day)

if __name__ == "__main__":
    run()
