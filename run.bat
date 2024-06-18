cd /d "%~dp0"
call direnv\Scripts\activate.bat
start cmd /k "streamlit run src/app.py"
