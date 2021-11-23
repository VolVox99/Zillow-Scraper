"# Zillow-Scraper" 
# Instructions

All terminal commands are highlighted.
Make sure you first have python 3 installed.
You can check this by running "python -V" in the terminal.
If the version it writes is not 3, download python 3 and for the instructions, usepython
everywhere instead ofpython.

## Steps for the very first time

1. unzip the downloaded folder
2. Open the terminal
3. Type incdand space
4. open the terminal and drag (click, hold down and move mouse) the unzipped folder onto
    the terminal
5. It should have pasted the folders path after cd onto the terminal. Press enter
6. typepython -m pip install -r requirements.txtandpress enter

Every other time you would like to run the script, you need to redo steps 2-4 from the first time,
so your terminal is running in the folder of the script.

Now that your terminal is in the folder of the code, you can run the script.
You can typepython main.pyinto the terminal andpress enter to run the script without any
options.

There are two options in the form of flags you can supply to alter the functionality of the script.

## URL

Where URL is the base URL of the city who’s listings you want to scrape. Example:
https://www.zillow.com/westchester-county-ny/

example:
python main.py https://www.zillow.com/westchester-county-ny/


## -ownr

This flag is optional. Only listings for sale by the owner will be grabbed. Defaults to False if not
present
example:
python main.py https://www.zillow.com/westchester-county-ny/-ownr

## --help

This will not run the script, it will only display a message showing all the available flags and how
to use them
Note: there are two dashes in the command

example:
python main.py --help

## Output while running

While the script is running, it will output certain information about what it is doing.

Finally it will output “FINISHED”. It is done running and you can now open the output file to view
the results. You cannot have the file open in something such as excel while the script is running
or it will error as it will not be able to write to it.

If it ever displays something cryptic such as

### Traceback (most recent call last):

### File "C:\Users\\main.py", line 99, in <module>

### main()

### File "C:\Users\main.py", line 35, in main

### with open(outFile, 'r+' if continue_file else 'w', newline = '', encoding = 'utf-8') as

### csvfile:

### PermissionError: [Errno 13] Permission denied: 'output.csv'

and stops running, that means an error has occurred. It is unlikely for any unaccounted errors to
occur, since I addressed any that had the possibility of occurring during my testing, but
something unexpected can always happen. To address this, copy paste the entire error
message, or take a screenshot, and contact me. I will fix it and get back to you.


The output does not need to be monitored, it is just auxiliary information while it is running.

If you run into any issues, or have any additional questions, feel free to reach out to me again.


