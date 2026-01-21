@echo off
title Orion Boot Loader
color 0A

echo Starting Orion OS...
timeout /t 1 >nul

:: Boot Screen
start "" "%cd%\System\BootScreen\Index.html"

echo Loading Media...
timeout /t 1 >nul
start "" "%cd%\Media"

echo Loading Data...
timeout /t 1 >nul
start "" "%cd%\Data"

echo Loading System...
timeout /t 1 >nul
start "" "%cd%\System"

echo Boot complete.
exit
