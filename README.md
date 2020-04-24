# To interact with the GUI
1. Click Load Data file
2. Select the .csv/.xls/.xlsx file you wish to create a profile of
3. Select the directory to save the profile (.html file)
4. Click Create Profile

The created profile is saved in the chosen directory and will automatically open in your browser.
The newly saved file adds the prefix "Profile_" to the original file name.

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
