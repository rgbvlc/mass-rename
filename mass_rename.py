#!python3

#name=mass_rename
#author=rgbvlc bartek.b133@wp.pl
#info=mass rename all filename or extension in direcory
#status=finished
#final version= X
#todo=X

import os, shutil, sys
print(len(sys.argv))
if len(sys.argv)<3:
    print("Wrong using. Try: python mass_rename [directory] 'new_name'/'.extension'")

def rename(path, new_name):
    num=1
    os.chdir(path)
    for file in os.listdir(path):
        if new_name[0]==".":
            file_ex=os.path.basename(file)
            uext=file_ex[:file_ex.index(".")]
            newN=uext+new_name
            old=os.path.join(os.path.abspath("."),file)
            new=os.path.join(os.path.abspath("."),newN)
            print("Change %s on %s..." % (old,new))
            shutil.move(old,new)
        else:
            file_ex=os.path.basename(file)
            ext=file_ex[file_ex.index("."):]
            newN=new_name+"_"+str(num)
            old=os.path.join(os.path.abspath("."),file)
            new=os.path.join(os.path.abspath("."),newN+ext)
            print("Change %s for %s..." % (old,new))
            shutil.move(old,new)
            num+=1

rename(sys.argv[1], sys.argv[2])

            
        
    
    
