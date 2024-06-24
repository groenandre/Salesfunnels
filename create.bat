@REM vscode openen
start vscode://file/C:/playwright
 
@REM Container met playwright inspector
wsl docker run --rm --name creator -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix mcr.microsoft.com/playwright:v1.44.0-jammy npx -y playwright open google.com