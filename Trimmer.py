import os
from win32com.client import Dispatch

shell = Dispatch('WScript.Shell')
mainFol = input("Program folder directory: ")
dirFol = input("Shortcut folder directory: ")
toggleNames = int(input("Name shortcut after folder or .exe file? (0/1): "))
print("Searching folder...")
for x in next(os.walk(mainFol))[1]: #loop through folders
    for y in os.listdir(str(mainFol) + "\\" + x ): #loop through files
        biggest = 0
        
        if y.endswith(".exe"): #find largest .exe file (excluding unity crash handler)
            if y.__sizeof__() > biggest and str(y) != "UnityCrashHandler64.exe":
                biggest = y.__sizeof__()
                biggestY = y

    if(toggleNames == 0): #create shortcut at shortcut folder named after folder / exe file
        print(x + "   done")
        shortcut = shell.CreateShortCut(dirFol+"\\"+y+".lnk") 
    else:
        print(biggestY + " done")
        shortcut = shell.CreateShortCut(dirFol+"\\"+biggestY+".lnk")

    shortcut.Targetpath = mainFol+"\\"+x+"\\"+biggestY #select largest file and confirm
    shortcut.save()

