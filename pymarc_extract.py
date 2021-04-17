import pymarc
from pymarc import MARCReader
import sys, csv, traceback, warnings, logging, re
import pandas as pd

'''
To run this program, open command line and type python3 pymarc_extract.py if you've saved it with this file name.
Print the help prompt.
'''
def printHelp(exitcode=127):
    print('pymarc_extracts.py <inputmarc> <outputtxt>')
    sys.exit(exitcode)

def extractsub():
    #ask user to define the variables for inputmarc file and outputtxt file
    inputmarc = input("Insert 'filename.mrc' Here >>> ")   
    outputtxt = input("Insert 'filename.txt' Here >>> ")

    #create dataframe
    marc_data = []
    
    #configure the max width display for column
    pd.set_option('display.max_colwidth', None)
    #create reader and make encoding utf8
    reader = MARCReader(open(inputmarc, 'rb'), hide_utf8_warnings=True, force_utf8=True, utf8_handling='ignore', file_encoding='utf-8')

    #extract the subfield/field values from the marc file
    try:
        for record in reader:
            #if you need to change the fields that you're looking for, this is the spot to do it
            for f in record.get_fields('650'):
                 #make sure 650$a exists
                 if f['a'] is not None:
                    #define variable catkey = value in the 001 field
                    catkey = record['001'].value()
                    geosub = (f['a'])
                    # print((record['001']), "|", geosub)
                    marc_data.append(str(catkey)+"|"+ geosub)

        #store data in dataframe
        df = pd.DataFrame(marc_data)

        # export to tab delimited file
        df.to_csv(outputtxt, sep='\t', encoding='utf-8', index = False)

    except:
        traceback.print_exc()

if __name__ == "__main__":
    #Define extractsub as main
    extractsub()
