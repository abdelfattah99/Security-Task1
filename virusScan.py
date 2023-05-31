# virus scan program
import glob, re, os, csv

# scan for signatures just like Semantec or other anti virus softwar

def checkforSignatures():
    print ("####### checking for virus signatures #######")

    # get all programs in the directary
    programs = glob.glob("*.py")
    for p in programs:
        thisFileInfected = False
        file = open(p, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if (re.search("^# starting virus code", line)):
                # found a virus
                print("!!!!!! virus found in file" + p)
                thisFileInfected = True
        if (thisFileInfected == False):
                 print (p+ " appears to be clean")


    print("###### end section ######")


def getFileData():
    # get an initial scan of file size and date modified. save to a
    programs = glob.glob("*.py")
    programList = []
    for p in programs:
        programSize = os.path.getsize(p)
        programModified = os.path.getmtime(p)
        programData = [p, programSize, programModified]

        programList.append(programData)
    return programList

def WriteFileData(programs):
    if (os.path.exists("fileData.txt")):
        return
    with open("fileData.txt", "w") as file:
        wr = csv.writer(file)
        wr.writerows(programs)
def checkForChanges():
    print("###### check for heuristic changes in the files ######")
    # open the fileData.txt file and compare each line
    # to the current file size and dates

    with open("fileData.txt") as file:
        fileList = file.read().splitlines()
    originalFileList = []
    for each in fileList:
        items = each.split(',')
        originalFileList.append(items)

    # get current data from directory
    currentFileList = getFileData()

    # compre the old and current items. check for differences
    for c in currentFileList:
        for o in originalFileList:
            if ( c[0] == o[0]):
                # file names matched
                if (str(c[1]) !=str(o[1]) or str(c[2]) !=str(o[2])):
                   # file sizes or dates do not match!
                   print("\n##########\nAlert. File mismatch!")
                   # print the data of each file
                   print ("Current values = " + str(c))
                   print ("Original values = " + str(o))
                else:
                    print ("File" + c[0] + "appears to be unchanged")


    print("###### finished checking for changes in files ######")

   
# do an initial scan and save the results in a text file.
WriteFileData(getFileData())
        

                  
checkforSignatures()
checkForChanges()



