import glob, os, subprocess
        
dir = os.path.dirname(__file__)

if not os.path.exists(dir+"\\exes"):
    os.makedirs(dir+"\\exes")

print('Generating exes')
for cue_file in glob.glob("*.cue"):
    file_name = os.path.splitext(cue_file)[0]
	
	batLocation = os.path.join(dir, "exes\\"+file_name+ ".bat")
	exeLocation = os.path.join(dir, "exes\\"+file_name+ ".exe")
	
    print(file_name)
    if os.path.exists(batLocation):
        open(batLocation, 'w').close()

    file = open(batLocation, 'w+')
                                
    file.write('"C:\\Program Files\\DAEMON Tools Lite\\DTAgent.exe"' + ' -mount dt, 0, "'+os.path.join(dir, cue_file)+'"')
    file.write("\n")
    file.write('"C:\\Users\\Joe\\Documents\\SSF_012_beta_R4\\SSF.exe"')
                                
    file.close()
    if os.path.exists(exeLocation):
        os.remove(exeLocation)

    subprocess.call(["C:\\Program Files\\Bat To Exe Converter\\Bat_To_Exe_Converter.exe", "-bat" ,file.name, "-save", os.path.join(dir, 'exes\\'+file_name+ '.exe')]) 
    os.remove(file.name)
