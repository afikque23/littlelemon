@echo off
setlocal
echo ================================================================
echo   Push Little Lemon Capstone Project to GitHub (afikque23)
echo ================================================================
echo.

set REPO_URL=https://github.com/afikque23/littlelemon.git

echo Target repository: %REPO_URL%
echo.
echo If you have already created the repository 'littlelemon' on GitHub:
echo (Make sure the repo is created at: https://github.com/new)
echo.

git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main

echo Pushing code to GitHub main branch...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================
    echo SUCCESS! Your repository is now live at:
    echo %REPO_URL%
    echo ================================================================
) else (
    echo.
    echo ----------------------------------------------------------------
    echo If the push failed, verify:
    echo 1. You created the repo named 'littlelemon' at https://github.com/new
    echo 2. You have write permissions or your GitHub credentials are ready
    echo ----------------------------------------------------------------
)

echo.
pause
