import sqlite3
import datetime
import optparse

def fixDate(timestamp):
    #Chrome stores timestamps in the number of microseconds since Jan 1 1601.
    #To convert, we create a datetime object for Jan 1 1601...
    epoch_start = datetime.datetime(1601,1,1)
    #create an object for the number of microseconds in the timestamp
    delta = datetime.timedelta(microseconds=int(timestamp))
    #and return the sum of the two.
    return epoch_start + delta

def getMetadataHistoryFile(locationHistoryFile, top):
	selectCommand = "SELECT * FROM urls" 
	if top != "":
		selectCommand = selectCommand + " limit " + top
        
	sql_connect = sqlite3.connect(locationHistoryFile)
	for row in sql_connect.execute(selectCommand):
		print("Order:\t", row[0])
		print("Date:\t", fixDate(row[5]))
		print("Name:\t" , row[2])
		print("URL:\t", row[1])
		print("")

	
def main():
    parser = optparse.OptionParser('-location <source location>')
    parser.add_option('-l', dest='location', type='string', help='specify url address')
    parser.add_option('-t',  dest='top', type='string', help='specify number of records')

    (options, args) = parser.parse_args()
    location = options.location
    top = options.top

    if location == None:
        exit(0)
    else:
        getMetadataHistoryFile(location, top)

if __name__ == '__main__':
    main()