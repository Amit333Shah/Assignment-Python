'''Write a script which can read the files line by line with .log ext and print it into a
file , while printing the data from the suffix with present date and time of the system.
 (example of file path are /home/Desktop/demo/test.log,
/home/Desktop/demo/test-1.log, /home/Desktop/demo/test2.log, .....)
 (sample data inside the .log files
 03-17 16:13:38.811 1702 2395 D WindowManager:'''

from datetime import datetime
def fileline(path,file1):
    print(path)
    #fileToread = open(path, "r")
    #print( datetime.now().strftime('c:/log/logfile_%H_%M_%S_%d_%m_%Y.log'),fileToread.read())
    with open(path, 'r') as fpIn, open(file1, 'w') as fpOut:
        lineNumber = 0
        for line in fpIn:
            lineNumber += 1
            line = datetime.now().strftime('%d:%m:%Y:%H:%M:%S 2227 2227 D TextView'),line.rstrip()  # Strip trailing spaces and newline
            fpOut.write("{}: {}\n".format(lineNumber, line))
            # Need \n, which will be translated to platform-dependent newline
        print("Number of lines: {}\n".format(lineNumber))

fileline(r"C:\Users\AMIT SHAH\Desktop\amitlog\amit3.log",r"C:\Users\AMIT SHAH\Desktop\amitlog\amit4.log")