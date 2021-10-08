import re
import time
from pathlib import Path

home = str(Path.home())
gamelog = home + r"\Downloads\MoMReborn\MoMReborn\logs\game.txt" # this is where every game message is stored
damageraw = "damagecopy.txt"
output = "output.txt"

lastLine = ""
startTime = 0
endTime = 0

def setLastLine():
    with open(gamelog) as initialGameLog:
        global lastLine
        lastLine = initialGameLog.readlines()[-2]
        initialGameLog.close()
    global startTime
    startTime = time.time()

def getDamageTxt():
    global endTime
    endTime = time.time()
    with open(gamelog) as infile, open(damageraw, "w") as outfile:
        copy = False
        for line in infile:
            if copy:
                outfile.write(line)
            elif line == lastLine:
                copy = True
        infile.close()
        outfile.close() # damageraw should now contain all game text sent while program was sleeping

def getStats(pname):
    getDamageTxt()
    elapsedTime = endTime - startTime
    totalDMG = 0
    dmgList = []
    with open(damageraw, "r") as input:
        for line in input:
            print(line)
            damage = ""
            lineArr = re.split("for | damage!", line)
            try:
                damage = lineArr[1]
            except IndexError:
                None
            try:
                damage = int(damage)
            except ValueError:
                None

            if isinstance(damage, int): # If the line seems compatible, add to dmgdict. Might not be perfect
                name = lineArr[0].split(" ")[2] # more like first word of name, but it's good enough for now
                if name == pname:
                    totalDMG += damage
                    dmgList.append(damage)
        input.close()
    return (totalDMG, elapsedTime, dmgList)
