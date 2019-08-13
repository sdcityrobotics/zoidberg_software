### Linux Documentation
While working on the **TX2** many of guides will inform you of packages and methods to install **packages** will be 90% true. This is because while the TX2 does run on linux, the kernnel version or ubuntu version may differ.


## Getting started with the tx2
The TX2 should be flashed with **Jetson Jetpack version 3.3**.
Other versions of jetpack maybe installed but because of the support for our carrier board these may not have the proper kernnel version or modules installed resulting in no boot once on the board.

## Getting started with linux
Once we have flashed the **TX2** we are able to boot in. While it may seem like we are done we still have to find and modify the bootloader.
Tom
## Modify the bootloader to target the propper EMMC flash
to modify the sd card to be bootible we must flash the existing memory onto our sd card.

`sudo cp -ax / ‘/media/nvidia/SD’`

Here we are running the copy command as a super user  saying we want to target our root directory and our destination will be our sd card labeled SD
Once we have copied the contents to our sd card we can proceed to modify the boot configuration on our SD card location.

This location based on previous should be '/media/nvidia/SD/boot/extlinux/extlinux.conf'

We have to find and modify the section labeled 'root=' to 'root=/dev/mmcblk1p1'

Save and reboot. If sucessful a 16~ gig MMC should be avaliable.
## Setting up dependacies
install missing dependacies and reboot

`sudo apt update`

`sudo apt upgrade`

`sudo apt install python3-pip glances python3-serial python3-setuptools python3-scipy install`

## Allowing x11 forwarding
| #/etc/ssh/sshd_config   |  
| ---------------------- | 
| X11Forwarding yes      |
| X11DisplayOffset 10     | 
| X11UseLocalhost no     |
## Setup git on tx2

### Linux Documentation
## Getting started with linux

## Getting started with the tx2

## Setting up dependacies

## Allowing x11 forwarding

## Setup git on tx2
