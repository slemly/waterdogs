IMPORTANT: PUT ALL FILES IN YOUR DOCUMENTS FOLDER IF YOU DO NOT KNOW HOW TO USE A COMMAND LINE TO NAVIGATE A COMPUTER


1. Before using, copy all cylindrospermosin data into a new .csv file in the same folder as <TTest.py> and <ttestfuncs.py>. 
2. Name this file "cylindrospermosin.csv"
3. Format your data in a single column with no units or header. 
   Enter a value, press enter to jump to a new line, and enter the next value. Repeat until finished.
4. Next, copy all cylindrospermosin data into a new .csv file in the same folder as <TTest.py> and <ttestfuncs.py>. 
5. Name this file cylindrospermosin.csv
6. Repeat this process for your microcystin data. Name this file "microcystins.csv"


If you don't know how to run a Python script, start here:
To run this program, open a command line on your machine.

    Navigation:

    MAC: Press [CMD] + [SPACE] and type 'Terminal' and press enter when the suggestion appears. 
        Alternatively, Look for Terminal in your Applications > Utilities folder.
        A terminal window will appear once you start the utility.
        *Type "pwd" into the terminal and press enter. This shows your current directory. 
        By default this will be /Users/<YOUR_NAME_HERE>/
        Typing "cd <FILEPATH OF THE DOWNLODADED FOLDER>" into the terminal should bring you to the working directory for this program.
            Replace the text between the < > above with the filepath for the project folder for TTest.py and ttestfuncs.py.
            If this works for you, proceed to the "Execution" section. If not, continue below.
        Type "cd Documents" into the terminal.
        You are now in your Documents directory.
        Type "ls" into the terminal. This displays the contents of your Documents folder.
        If you see the folder that you downloaded this program in, type "cd <NAME_OF_THE_FOLDER_GOES_HERE>" into the terminal.
        Now you are ready to go to the "Execution" section. See below.

    PC: 
        Install Git Bash or MobaXTerm to use Bash command line tools:
            Git Bash: https://git-scm.com/download/win
            MobaXTerm: https://mobaxterm.mobatek.net/download.html

        Git Bash: In Windows Explorer, navigate inside of the folder that this README is in. 
                    Right Click on the blank space inside of the folder. Select "Git Bash here".
                    A terminal window should open. 
                    Type "pwd" into the terminal and confirm the filepath is the proper filepath for the folder that contains this README.
                    If this works, proceed to the "Execution" section. See below.
                    If this does not work, start up Git Bash as an application and follow the instructions for Mac from the * onward. 
        MobaXTerm: In Windows Explorer, navigate inside of the folder that this README is in. 
                    Right Click on the blank space inside of the folder. Select "New MobaXTerm Window here".
                    Type "pwd" into the terminal and confirm the filepath is the proper filepath for the folder that contains this README.
                    If this works, proceed to the "Execution" section. See below.
                    If this does not work, start up MobaXTerm as an application.
                         Select "Local Terminal", then follow the instructions for Mac from the * onward.
    Linux:

        If you have Linux installed, I'm assuming you know what you're doing.


    
    Execution:

        Type "python -V" or "python3 -V" into the command line to check what version of Python you have.
            If this gives an error, you need to install Python : https://www.python.org/downloads/ 

        If you have Python installed, type "python" into the command line and press enter.
        This opens a new python instance that is now running in your terminal. A ">>>" on the left side of the command line signifies this.

        Type "import numpy as np" in to the python instance. If this yields an error, you need to install the python module "numpy".
        Press CTRL+D to exit the python instance. Type "pip install numpy" into the command line. numpy should begin installing.
            If this doesn't work, install numpy here: https://www.scipy.org/scipylib/download.html 

        Type "import pandas as pd" in to the python instance. If this yields an error, you need to install the python module "pandas".
        Press CTRL+D to exit the python instance. Type "pip install pandas" into the command line. pandas should begin installing.
            If this doesn't work, install pandas here: https://pandas.pydata.org/getpandas.html 

        Once both modules are installed and your .csv files are made, type "python TTest.py" into the command line. This executes the script.
        If you have multiple versions of Python installed, you may need to type "python3 TTest.py" into the command line instead, or 
            "python2.7 TTest.py" into the command line, depending on your version. The numbers will change based upon the version.

        Results should print to the terminal once the script is complete. Be sure all data is formatted identically to the example .csv files given.

        