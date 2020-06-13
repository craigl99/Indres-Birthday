"""
Author: Milosz Plichta

Welp, getting back into python was fun xD
This library only contains one function,
but we wanted to extract different types of data
which means using muliple program, all of which need to utilise this function.

Oh and happy birthday Indre!
"""


#Function that retrun an array of strings that contain the data
def extract_data(dataType):
    file = open("data.txt")
    dataArray = []
    while(True):
        line = file.readline()
        line = line.lstrip()
        data = ""
        dataStart = 0
        dataEnd = len(line)
        
        if(line == ""):
            break

        #Find the last quotation mark, that ends that data
        for i in range(len(line)):
            if(line[i] == '"'):
                dataEnd = i

        #Finds the first quotation mark, the beginning of the data
        for j in range((dataEnd-1), 0, -1):
            if(line[j] == '"'):
                dataStart = j

    
        #If the data is found, each packet is stored in a varaible
        #Which are then appended to one array, called dataArray
        if(dataStart != 0 and dataType == (line[0:dataStart].rstrip().lstrip())):
            data = line[(dataStart+1):dataEnd]
            dataArray.append(data)
    file.close()
    return dataArray

    

array = extract_data("contents:")
print(array[0])


