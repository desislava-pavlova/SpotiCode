@echo off
setlocal

set ERRORS=

:ask_db
set /p DB_NAME=Enter database name (required): 
if "%DB_NAME%"=="" (
    echo Database name cannot be empty!
    goto ask_db
)

REM Optional host, default to localhost
set /p DB_HOST=Enter host [localhost]: 
if "%DB_HOST%"=="" set DB_HOST=localhost

REM Optional user, default to postgres
set /p DB_USER=Enter user [postgres]: 
if "%DB_USER%"=="" set DB_USER=postgres

REM Prompt for password once (hidden input not native in batch, but simple echo off)
for /f "usebackq delims=" %%p in (`powershell -Command "$pw = Read-Host 'Enter password' -AsSecureString; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($pw))"`) do set PGPASSWORD=%%p


echo.
echo Using:
echo   DB_NAME=%DB_NAME%
echo   DB_HOST=%DB_HOST%
echo   DB_USER=%DB_USER%
echo.
pause


REM === FUNCTIONS ===
for /r functions %%f in (*.sql) do (
    echo Running %%f
    psql -h %DB_HOST% -U %DB_USER% -d %DB_NAME% -f "%%f"

    if errorlevel 1 (
	echo ERROR in %%f
	set ERRORS=!ERRORS!%%f\n
    )
)


REM === TRIGGERS ===
for /r triggers %%f in (*.sql) do (
    echo Running %%f
    psql -h %DB_HOST% -U %DB_USER% -d %DB_NAME% -f "%%f"

    if errorlevel 1 (
	echo ERROR in %%f
	set ERRORS=!ERRORS!%%f\n
    )
)


REM === VIEWS ===
for /r views %%f in (*.sql) do (
    echo Running %%f
    psql -h %DB_HOST% -U %DB_USER% -d %DB_NAME% -f "%%f"

    if errorlevel 1 (
	echo ERROR in %%f
	set ERRORS=!ERRORS!%%f\n
    )
)


echo.
echo ==========================
echo EXECUTION FINISHED
echo ==========================

if defined ERRORS (
    echo The following scripts FAILED:
    echo.
    echo !ERRORS!
) else ( 
    echo All SQL scripts applied successfully on %DB_NAME%.
)

endlocal
pause
