# network-power-saver - Work in progress

This is a small project to detect movement and on detection run an action. 

To save power in my small office, if no movement is detected for 30 minutes the monitor smart plugs (connecting to wall screens and printers) and Access-points powered via POE on a Cisco Swicth and swicthed off. 

These actions are logged in a CSV file to calculate savings over time which also account for the Raspberry Pis power consumption 

## Installation
I use poetry to manage the packages, you will need to install poetry and make sure it's in path before starting. You can download poetry from here.. https://python-poetry.org/

Once poetry is installed and you have cloned the repo, create a shell 'poetry shell' and install the packages ' poetry install'

## Pins

![alt text](https://github.com/grevster/network-power-saver/blob/main/images/pi-pins.jpg?raw=true)