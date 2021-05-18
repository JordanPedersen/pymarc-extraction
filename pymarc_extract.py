import pymarc
from pymarc import MARCReader
import sys, csv, traceback, warnings, logging, re
import pandas as pd

def extractsub():
    #ask user to define the variables for inputmarc file and outputtxt file
    inputmarc = input("Insert 'filename.mrc' Here >>> ")   
    outputtxt = input("Insert 'filename.txt' Here >>> ")

    #create dataframe
    marc_data = []
    #Configure the max width display for column
    pd.set_option('display.max_colwidth', None)
    reader = MARCReader(open(inputmarc, 'rb'), hide_utf8_warnings=True, force_utf8=True, utf8_handling='ignore', file_encoding='utf-8')

    try:
        for record in reader:
            ##this is a new line from old version
            if record is not None:
                # print(record) --- this is also a new line
                if record.get_fields('651') is not None:
                    for f in record.get_fields('651'):  
                        # print(f)
                        if f['a'] is not None:
                            catkey = record['001'].value()
                            geosub = (f['a'])
                            if type(geosub) == None.__class__:
                                geosub = ""
                            
                            #print((record['001']), "|", geosub)
                            marc_data.append(str(catkey)+"|"+ geosub)

                else:
                    print("something wrong")

        #store data in dataframe
        df = pd.DataFrame(marc_data)

        # export to tab delimited file
        df.to_csv(outputtxt, sep='\t', encoding='utf-8', index = False)

    except:
        traceback.print_exc()

if __name__ == "__main__":
    #Define extractsub as main
    extractsub()
