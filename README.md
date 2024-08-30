# unitils

## Description

unitils is a simple/minimal program that allows you as a student to easily view your class schedule.  
It is designed to run solely in the terminal and utilizes arguments to refine what you want it to display.  
Setup for unitils should be completed via the config.conf file, as well as any other customizations you may want.  

## Installation

Linux users can install unitils via curl:

Step 1, curl main.py & unitils.conf:
```
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/unitils/main/main.py -o /usr/local/bin/unitils
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/unitils/main/unitils.conf -o /usr/local/bin/unitils.conf
```
Step 2, edit/verify file read & write permissions:
```
sudo chmod a+rx /usr/local/bin/unitils
sudo chmod a+r /usr/local/bin/unitils.conf
```

## Uninstallation

Step 1, cd into the directory:
```
cd /usr/local/bin
```
Step 2, remove the two files:
```
sudo rm unitils
sudo rm unitils.conf
```

If you are not using Linux, you will have to modify main.py to correct the file path for unitils.conf  
After that, you can run it normally with python main.py

## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
