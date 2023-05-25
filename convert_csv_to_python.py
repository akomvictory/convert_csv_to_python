# import the csv and json module using the import keyword.
import csv, json
# take the csv file and store it in a variable
csv_file_handler = 'demo.csv'
# take and empty json file and store it in a variable 
json_file_handler = 'demo.json'
# create an empty dictionary 
json_dictionary = {}
# open the given csv file using open() function
with open(csv_file_handler ) as csv_file_handler :
    # pass the given csv file as an argument to the DictReader() function of the csv module 
    # to convert the given csv file data into dictionary
    # store it in a variable
    csv_file_data = csv.DictReader(csv_file_handler)
    json_dictionary["data"] = []
    # loop through the rows in the json dictionary above
    for row in csv_file_data:
        # print the row data for reference
        print(row)
        # append all the row data to the above created json dictionary
        json_dictionary["data"].append(row)
#open the given json file in write mode using the open() function
with open(json_file_handler, 'w') as json_file_handler:
    #pass the above json dictionary, indent as arguments to the dumps() function
    # of the json module to dump all the data into json_file_handler(demo.json)
    # here indent is used for better printing.
    json_file_handler.write(json.dumps(json_dictionary, indent= 4))    


