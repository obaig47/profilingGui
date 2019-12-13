from cx_Freeze import setup, Executable
import sys
import os

build_exe_options = {'include_files': [os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll')]}

setup(name='profilingGui',
      version='0.1',
      description='Apply pandas profiling to data file',
      executables=[Executable("main.py")], requires=['pandas', 'PyQt4'])
