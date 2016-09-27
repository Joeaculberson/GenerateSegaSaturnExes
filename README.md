# GenerateSegaSaturnExes
A python script to generate your Sega Saturn exes for 1 click playing. Ideal to use with Ice for Steam.

Reason for this script:

SFF does not allow direct usage of bin/cue files. Instead it expects a physical disc. This causes two issues:

  1) You're required to have a disc drive on the device you are on.
  
  2) You can't just specify target params if you are using Steam like with other emulators.
  
This can be sovled by downloading Daemon Tools lite and mounting your bin/cue virtually. This script dares to go one step further. This script creates exe's from bat files so that you can mount the bin/cue file, open SSF, and run the game -- all with one click.

Directions:

Run Ice like you normally would with other emulators.

Use this in the consoles.txt file

[SSF]

location=C:\Users\Joe\Documents\SSF_012_beta_R4\SSF.exe

command=C:\Users\Joe\Desktop\ROMs\Saturn\exes\%fn.exe

in order to use the %fn param I had to download the lastest version of ice from their repo.

Use this in the emulators.txt file

[Saturn]

nickname=Saturn

emulator=SSF

extensions=cue

Assuming your bin/cue files are named correctly (check with http://consolegrid.com/), then you should see your games in Steam after running Ice.

Edit the Python script to point to your DAEMON Tools lite exe and the SSF.exe.

Run the script in the same folder as all of your bin/cue files.
