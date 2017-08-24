import  shutil
import os
#shutil.move(src,dst) #move file
#shutil.copy(src,dst) #copy file



intersections = ['a','b','c','d',"ab","ac","ad","bc","bd","cd","abc","abd","acd","bcd","abcd"]

names =["ab","ac","ad","bc","bd","cd","abc","abd","acd","bcd","abcd","ab_cd","ac_bd","ad_bc","abcd"]


for name in names:
    newname = "4waydiagram_"+name+".svg"
    shutil.copy("4waydiagram.svg",newname)
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
