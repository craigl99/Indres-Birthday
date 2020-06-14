'''
Milosz Plichta

Second attempt because I was being stupid :)
This time, using the json library, I can read the file information
and store it as a 'dict' which makes everything really easy.
Then all that was needed to be done is format the output correctly
so that it can be inputted into an excel file.
'''
import json
import datetime
import time

# Uses user input to load the correct file
print("Enter the name of the file:")
fileName = input()

# This loads the information from the json file into a dict format
with open(fileName + '.json', 'r') as f:
    data = json.loads(f.read()) 

outputFile = open('output.txt', 'w', encoding="utf-8")

# For every message, outputs it's content in the correct format
for message in data['messages']:
    date = datetime.datetime.fromtimestamp(message['timestamp_ms']/1000)
    outputFile.write(message['sender_name'].encode('latin1').decode('utf8') + '| ')
    if 'content' in message:
        outputFile.write(message['content'].encode('latin1').decode('utf8') + '|| ')
    elif 'photos' in message:
        outputFile.write('| ')
    else:
        outputFile.write('| ')
    
    
    if 'reactions' in message:
        for reaction in message['reactions']:
            outputFile.write(reaction['reaction'].encode('latin1').decode('utf8'))
        outputFile.write('| ')
    else:
        outputFile.write('| ')

    outputFile.write(date.strftime('%d/%m/%Y| '))
    outputFile.write(date.strftime('%H:%M:%S\n'))
print("Done...")
time.sleep(2)
f.close()
