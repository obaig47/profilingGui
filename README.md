# To interact with the GUI
1. Click Load Data file
2. Select the .csv/.xls/.xlsx file you wish to create a profile of
3. Select the directory to save the profile (.html file)
4. Click Create Profile

The created profile is saved in the chosen directory and will automatically open in your browser.
The newly saved file adds the prefix "Profile_" to the original file name.

# Required Libraries
- PyQt4
  - To install PyQt4 on Windows you need to install it based on the .whl file available here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4. 
    - pip install <.whl path>
  - Optionally, you can also install the source code instead https://www.riverbankcomputing.com/software/pyqt/download
- pandas_profiling

# Environment

* conda

  * conda create --name env_name --file conda_requirements.txt
* pip
  * python -m venv env
  * source env/bin/activate
  * pip install -r requirements.txt

# Citations
This program makes use of the pandas_profiling library
https://github.com/pandas-profiling/pandas-profiling