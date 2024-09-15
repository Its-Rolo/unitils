# unitils

## Description

unitils is a simple/minimal program that allows you as a student to easily view your class schedule.  
It is designed to run solely in the terminal and utilizes arguments to refine what you want it to display.  
Setup for unitils should be completed via the unitils.conf file, as well as any other customizations you may want.  

## Installation

Linux users can install unitils via curl:

Step 1, curl main.py & unitils.conf:
```
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/unitils/main/main.py -o /usr/local/bin/unitils
sudo curl -L https://raw.githubusercontent.com/Its-Rolo/unitils/main/unitils.conf -o /usr/local/bin/unitils.conf
```
Step 2, modify/verify file read & write permissions:
```
sudo chmod a+rx /usr/local/bin/unitils
sudo chmod a+rw /usr/local/bin/unitils.conf
```
Step 3, edit unitils.conf with any text editor to include your classes & settings (for example):
```
cd /usr/local/bin
vim unitils.conf
```

If you are not using Linux, you can clone the github repo. You must also edit main.py as the file path structure is designed for linux.  
After completing those two steps, you can run the script as normal with 'python main.py'

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

## Usage

unitils can be run directly in the terminal via the command:  
```
unitils
```
Using this command without any arguments will display the entire week schedule.  
unitils also has multiple arguments that you can use to refine what it displays, listed below:  

The --nextclass argument will display when the next upcoming class is that day.  
```
unitils --nextclass
```
The day arguments will display the schedule only for the specified day. For example:  
```
unitils --monday
```
Arguments cannot be combined.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
