
import math
import csv




footignBarType = {}
mBars = {}
mBarsRings = {}
barsTotalInFeet = {}
barsWeight={}

def footing(xF, xInch, yF, yInch,spacingInchX,spacingInchY, barSize, foldingLength, numberColumns):
    #print("footing calculation start")
    xLen  = xF*12+xInch
    numBarsX = xLen/spacingInchX+1
    numBarsX = math.ceil(numBarsX)
    
    #need to consider points half
    yLen =yF*12+yInch
    numBarsY = yLen/spacingInchY+1
    numBarsY = math.ceil(numBarsY)
    totalLen = numBarsX*(yLen+2*foldingLength) + numBarsY*(xLen+2*foldingLength)
    totalLen  = totalLen*numberColumns
    totalLenInFeet = totalLen/12
    return totalLenInFeet
    
    
    
def column(partition, barSize,numberOfBars, numberColumns):
    #print("column calculation start")
    totalLen = (numberOfBars*(40/partition))/40*numberColumns
    totalLenInFeet = totalLen*12
    return totalLenInFeet
    
def columnRings(partition,spacing, x, y,barSize, numberOfBars, numberColumns):
    #print("column calculation start")
    singleRingPerimeter = 2*(x-2)+2*(y-2)+2 #2 is folding
    length = 40/partition
    numRings = (length*12)/spacing+1
    return (singleRingPerimeter*numRings)/12   #returning in feet    
    
    
def beam():
    print("beam calculation start")

def display():
    print("printing footing bar type details->")
    for x,y in footignBarType.items():
        print(x,y)
        if x in barsTotalInFeet.keys():
            barsTotalInFeet[x] = barsTotalInFeet[x]+y
        else:
            barsTotalInFeet[x] = y            
    
    
    print("\n")
    print("\n")
    print("printing bars COLUMNS type details->")
    for x,y in mBars.items():
        print(x,y)
        if x in barsTotalInFeet.keys():
            barsTotalInFeet[x] = barsTotalInFeet[x]+y
        else:
            barsTotalInFeet[x] = y            
        
    
    print("\n")
    print("\n")
    print("printing bar RINGS details->")
    for x,y in mBarsRings.items():
        print(x,y)
        if x in barsTotalInFeet.keys():
            barsTotalInFeet[x] = barsTotalInFeet[x]+y
        else:
            barsTotalInFeet[x] = y            


    print("\n")
    print("\n")
    print("printing bars Total Leng in FEET and WEIGHT details->")
    for x,y in barsTotalInFeet.items():
        print(x,y)
    

    print("\n")
    print("\n")
    print("printing bars Total  Number of BARS and WEIGHT details->")
    for x,y in barsTotalInFeet.items():
        print(x,y/40,(((y/40)*x*x)/162.5)*12)
        
    print("PRINTING DONE")
            
def main():
    # reading csv file
   # opening the CSV file
    with open('inputFooting.csv', mode ='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            #print(lines)
            totalFootingLen = 0
            xF=int(lines['xF'])
            xInch=int(lines['xInch'])
            yF=int(lines['yF'])
            yInch=int(lines['yInch'])
            spacingInchX=int(lines['spacingInchX'])
            spacingInchY=int(lines['spacingInchY'])
            barSize=int(lines['barSize'])
            foldingLength=int(lines['foldingLength'])
            numberColumns=int(lines['numberColumns']) 
            if(barSize in footignBarType.keys()):
                footignBarType[barSize] = footignBarType[barSize] + footignBarType[barSize]+footing(xF, xInch, yF, yInch,spacingInchX,spacingInchY, barSize, foldingLength, numberColumns)
            else:
                footignBarType[barSize] = footing(xF, xInch, yF, yInch,spacingInchX,spacingInchY, barSize, foldingLength, numberColumns)        
                            
    #read input csv file
    distinctColumns = 2

    
    with open('inputColumn.csv', mode ='r') as file: 
        csvFile = csv.DictReader(file)
        for lines in csvFile:        
            partition=int(lines['partition'])
            barSize= int(lines['barSize'])
            numberOfBars =int(lines['numberOfBars']) 
            numberColumns = int(lines['numberColumns'])
            if(barSize in mBars.keys()):
                mBars[barSize] = mBars[barSize]+column(partition, barSize,numberOfBars, numberColumns)
            else:
                mBars[barSize] = column(partition, barSize,numberOfBars, numberColumns)
                
    with open('inputRings.csv', mode ='r') as file: 
        csvFile = csv.DictReader(file)
        for lines in csvFile: 
            partition=int(lines['partition'])
            barSize= int(lines['barSize'])
            numberOfBars =int(lines['numberOfBars']) 
            numberColumns = int(lines['numberColumns'])     
            spacing = int(lines['spacing']) 
            x= int(lines['x'])
            y= int(lines['y'])
                         
            if(barSize in mBarsRings.keys()):     
                mBarsRings[barSize] = mBarsRings[barSize] + columnRings(partition,spacing, x, y,barSize, numberOfBars, numberColumns)
            else:
                mBarsRings[barSize] = columnRings(partition,spacing, x, y,barSize, numberOfBars, numberColumns)
                
    #print("starting beam")
    
    display()
    #beam()
    #display output
    

if __name__ == "__main__":
    main()