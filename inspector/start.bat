wsl docker run --rm -ti --name inspector^
    -e DISPLAY=:0 ^
    -v /tmp/.X11-unix:/tmp/.X11-unix ^
    mcr.microsoft.com/playwright:v1.44.1-jammy npx -y playwright open google.com