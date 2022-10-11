
import math
import csv




footignBarType = {}
mBars = {}
mBarsRings = {}
barsTotalInFeet = {}
barsWeight={}
beamLenDir = {}
beamRingsDir = {}

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

def beamRings(spacing, x, y, barSize, length,numberBeams, numberColumns=1):
    #print("column calculation start")
    singleRingPerimeter = 2*(x-2)+2*(y-2)+2 #2 is folding
    numRings = math.ceil((length*12)/spacing)+1
    return (singleRingPerimeter*numRings)/12*numberBeams   #returning in feet    
    
    
    
def beam(bottomStraightCount, bottomStraightLen, bottomStraightBarSize,
         bottomCurtailCount, bottomCurtailBarSize, 
         topStraightCount, topStraightBarSize, 
         topLeftCount, topLeftBarSize,
         topRightCount, topRightBarSize,
         numberBeams):
    
    print("beam calculation start")
    bottomStraight = bottomStraightCount * bottomStraightLen *numberBeams
    bottomCurtail = bottomCurtailCount * bottomStraightLen/2 *numberBeams
    topStraight = topStraightCount * bottomStraightLen * numberBeams
    topCurtailLeft= topLeftCount * bottomStraightLen/4 * numberBeams
    topCurtailRight = topRightCount * bottomStraightLen/4 * numberBeams
    
    if(bottomStraightBarSize in beamLenDir.keys()):
        beamLenDir[bottomStraightBarSize] = beamLenDir[bottomStraightBarSize] + bottomStraight 
    else:
        beamLenDir[bottomStraightBarSize] = bottomStraight 
    
    if(bottomCurtailBarSize in beamLenDir.keys()):
        beamLenDir[bottomCurtailBarSize] = beamLenDir[bottomCurtailBarSize] + bottomCurtail 
    else:
        beamLenDir[bottomCurtailBarSize] = bottomCurtail 
    
    if(topStraightBarSize in beamLenDir.keys()):
        beamLenDir[topStraightBarSize] = beamLenDir[topStraightBarSize] + topStraight 
    else:
        beamLenDir[topStraightBarSize] = topStraight     
    
    if(topLeftBarSize in beamLenDir.keys()):
        beamLenDir[topLeftBarSize] = beamLenDir[topLeftBarSize] + topCurtailLeft 
    else:
        beamLenDir[topLeftBarSize] = topCurtailLeft                 

    if(topRightBarSize in beamLenDir.keys()):
        beamLenDir[topRightBarSize] = beamLenDir[topRightBarSize] + topCurtailRight 
    else:
        beamLenDir[topRightBarSize] = topCurtailRight                 
        
    
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
    print("printing bar BEAM details->")
    for x,y in beamLenDir.items():
        print(x,y)
        if x in barsTotalInFeet.keys():
            barsTotalInFeet[x] = barsTotalInFeet[x]+y
        else:
            barsTotalInFeet[x] = y  


    print("\n")
    print("\n")
    print("printing BEAM RINGS details->")
    for x,y in beamRingsDir.items():
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
    
    with open('inputBeam.csv', mode ='r') as file: 
        csvFile = csv.DictReader(file)
        for lines in csvFile: 
            bottomStraightCount = int(lines['bottomStraightCount'])
            bottomStraightLen = int(lines['bottomStraightLen'])
            bottomStraightBarSize = int(lines['bottomStraightBarSize'])
            bottomCurtailCount = int(lines['bottomCurtailCount'])
           
            bottomCurtailBarSize = int(lines['bottomCurtailBarSize'])
            topStraightCount = int(lines['topStraightCount'])
            topStraightBarSize = int(lines['topStraightBarSize'])
            topLeftCount = int(lines['topLeftCount'])
            topLeftBarSize = int(lines['topLeftBarSize'])
            topRightCount = int(lines['topRightCount'])
            topRightBarSize = int(lines['topRightBarSize'])
            ringBarSize = int(lines['ringBarSize'])
            spacing = int(lines['spacing']) 
            x= int(lines['x'])
            y= int(lines['y'])
            numberBeams = int(lines['numberBeams'])
            
            beam(bottomStraightCount, bottomStraightLen, bottomStraightBarSize, 
                 bottomCurtailCount, bottomCurtailBarSize, 
                 topStraightCount, topStraightBarSize, 
                 topLeftCount, topLeftBarSize,
                 topRightCount, topRightBarSize,
                 numberBeams)
            
            if(ringBarSize in beamRingsDir.keys()):     
                beamRingsDir[ringBarSize] = beamRingsDir[ringBarSize] + beamRings(spacing, x, y, ringBarSize, bottomStraightLen)
            else:
                beamRingsDir[ringBarSize] = beamRings(spacing, x, y, ringBarSize, bottomStraightLen)
            
            
    #display output
    display()

if __name__ == "__main__":
    main()
