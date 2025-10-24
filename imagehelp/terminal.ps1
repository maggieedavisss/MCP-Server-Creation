PS C:\Users\magdav01> uv init tiger
error: Project is already initialized in `C:\Users\magdav01\tiger` (`pyproject.toml` file exists)
PS C:\Users\magdav01> cd tiger
PS C:\Users\magdav01\tiger> ls


    Directory: C:\Users\magdav01\tiger


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        10/24/2025   4:02 PM            109 .gitignore
-a----        10/24/2025   4:02 PM              5 .python-version
-a----        10/24/2025   4:02 PM             83 main.py
-a----        10/24/2025   4:02 PM            151 pyproject.toml
-a----        10/24/2025   4:02 PM              0 README.md


PS C:\Users\magdav01\tiger> uv venv
Using CPython 3.11.9 interpreter at: C:\Users\magdav01\AppData\Local\Programs\Python\Python311\python.exe
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
PS C:\Users\magdav01\tiger> .venv\Scripts\activate
(tiger) PS C:\Users\magdav01\tiger> uv add mcp[cli] httpx
Resolved 35 packages in 621ms
Prepared 19 packages in 1.00s
Installed 34 packages in 1.72s
 + annotated-types==0.7.0
 + anyio==4.11.0
 + attrs==25.4.0
 + certifi==2025.10.5
(tiger) PS C:\Users\magdav01\tiger> new-item tiger.py


    Directory: C:\Users\magdav01\tiger


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        10/24/2025   4:04 PM              0 tiger.py
