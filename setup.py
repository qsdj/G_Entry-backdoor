from distutils.core import setup
import py2exe
from glob import glob

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(
	data_files=data_files,
    #windows=['Gentry.py',"icon_resources": [(1, "myicon.ico")],

    windows = [{
            'script': 'payload.py',
            }], 

    zipfile = None,
    options = {
        'py2exe': {
        'bundle_files': 1, 'compressed': True,

        	'includes': ['lxml._elementpath','win32crypt', 'win32api', 'win32cred'],
        	'bundle_files': 1, 'compressed': True,
            'dll_excludes':["api-ms-win-core-string-l1-1-0.dll", 
            "api-ms-win-core-processthreads-l1-1-2.dll", 
            "api-ms-win-core-sysinfo-l1-2-1.dll", 
            "api-ms-win-core-synch-l1-2-0.dll", 
            "api-ms-win-core-heap-l2-1-0.dll", 
            "api-ms-win-core-registry-l1-1-0.dll", 
            "api-ms-win-core-delayload-l1-1-1.dll", 
            "api-ms-win-core-errorhandling-l1-1-1.dll",
            "api-ms-win-core-profile-l1-1-0.dll",
            "api-ms-win-core-libraryloader-l1-2-0.dll",
            "mswsock.dll", 
            "powrprof.dll",
            "Crypt32.dll",
            "api-ms-win-core-apiquery-l1-1-0.dll"],
             
        }
    }

)