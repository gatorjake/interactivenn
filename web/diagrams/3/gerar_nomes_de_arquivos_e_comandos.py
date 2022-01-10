import  shutil
import os
#shutil.move(src,dst) #move file
#shutil.copy(src,dst) #copy file



intersections = ['a','b','c',"ab","ac","bc","abc"]

names =["ab","ac","bc","abc"]


for name in names:
    newname = "3waydiagram_"+name+".svg"
    shutil.copy("3waydiagram.svg",newname)
    union = []
    splited = name.split('_')
    for part in splited:
        part_union = []
        for c in part:
            part_union.append(c)
        union.append(part_union)
        
            
        
    #inkscape -f 5waydiagram.svg --select=elipseA --select=elipseB --       verb=SelectionUnion --verb=FileSave --verb=FileClose
    command = "inkscape -f "+newname+" --verb=EditDeselect "
    for part in union:
        for e in part:
            command = command + "--select=elipse"+e.upper()+" "
        command = command + "--verb=SelectionUnion --verb=EditDeselect "
    command = command + "--verb=FileSave --verb=FileClose"
    
    os.system(command)
    print newname +" saved"
