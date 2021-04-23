# Python-Projekt-Setup
This is a generell structure, along with a setup guide for the Distributed Systems Projekt at https://www.hhz.de/master/digital-business-engineering/

-  steps you have already done you may be able to skip
-  some parts of this setup only work in windows

## Step by step guide

1. read this document carefully and in full
2. first all the downloads:
3. make a github account  https://github.com/
4. download VSCODE https://code.visualstudio.com/download 
5. you can use other Code editors (or IDE) but VSCODE is just the best so.....
6. download python 3.9 https://www.python.org/downloads/
![python install 1](./pictures/download_Python.png)
7. check all checkboxes and do Install now
![python install 2](./pictures/download_Python3.png)
8. if you dont know git I recommend using a git GUI that visualises everything
I like to use https://www.gitkraken.com/ (free version only works for public github repositorys); 
u can also use https://www.sourcetreeapp.com/
or a git extension inside VSCode)
9. now you should have everything downloaded and have all the accounts and stuff
10. now try out python in your commandline (u can use the Terminal in VSCode ) ('ctrl + ö', if it is not visible)
``` powershell
py -0  # to see which python versions you have installed
py # to start python
# continue as shown in the image below
# ctrl + z is the same as quit()
```
![ninite install](./pictures/python_in_commandLine.png)

11.  py -h # a -h or -?   in the commandline next to a command is sometimes helpfull, to see what you can do
12.  Now python should work on your system and we can proceed
13.  Note: it could be that you have to restart your system or add your python installation manually to your path, for the 'python' or 'python3' command to work
14.  restart your pc, because ... windows .... maybe do it twice, just to be sure i dont know (I did not need to do it)
15.  Now: you will use pip  (not anaconda) to manage your python enviroment and python modules (or packages, not sure what the correct name is)
16.  Open the terminal, and  type
```powershell
pip -V #to make sure your pip is connected with your 3.9 version
pip list # to show which python packages are installed
py -3.9 -m pip install --upgrade pip # to update your pip installation
pip install numpy # to install a python package (here numpy)
```
![ninite install](./pictures/pip.png)

17.   now you could use your python installation (python enviroment), that is installed in c:\users\du-wa\appdata\local\programs\python\python39\

But thats kind bad, because then you use the same python enviroment for all of your personal projekts. Which means changing something for one of your python projekts could screw up your other projekt.
Also if you work with multiple poeple on the same projekt, it is hard to make sure, that everyone has the same enviroment setup and everyone has the same package versions installed.
It will happen, that you want to install a new package and then it works for one of you and maybe the other teammember gets it working, but for whatever reason it doesnt work for one. (maybe because windows) \rant off

18. You want to use a virtual enviroment; put if you are lucky this repository will handle everything for you :D
19. 