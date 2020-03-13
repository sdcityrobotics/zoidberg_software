### Linux Documentation
Linux Tutorial
* Linux
* Shell
* Commands
* Configuration
* Tools
* Compiliation
* [TX2](https://github.com/sdcityrobotics/zoidberg_software/tree/master/Linux#getting-started-with-the-tx2)
1. Linux
	* I'd just like to interject for moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it,uGNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.
	Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.
	There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux!)

2. Commands
* ls
* cat
* cd
* nano (or vim)
* [ssh](https://youtu.be/ORcvSkgdA58)

3. configuration of the operating system
Most linux distributions have similar ways of configuration, the main differences are a small subset of files(Technincly everything is a file in linux even your devices like your keyboard) These are general reffrenced as the run commands or rc files.

For example your shell will be bash, when the command bash is ran, the configuration is loaded from the run command. The file is most offten is located at "~/.bashrc" These symbols all have a specific meaning. This is offten refered to the path. The tilda symbol is a refrence to the home directory of the current user(Who you are logged in as.
The slash is a refrence to the next directory, unlike windows linux uses forward slash

4. [Alias](https://youtu.be/vz2DGSBBpXg)(aka how to save your fingers from repeated torture)
5. [Linux Directories](https://www.youtube.com/watch?v=HbgzrKJvDRw)
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

`sudo apt install python3-pip glances python3-serial python3-setuptools python3-scipy git curl`



# WORK IN PROGRESS BEYOND THIS POINT

## Allowing x11 forwarding
| #/etc/ssh/sshd_config   |
| ---------------------- |
| X11Forwarding yes      |
| X11DisplayOffset 10    |
| X11UseLocalhost no     |
## Setup git on tx2
A quick `git clone` can enable you to clone the full repository
`mkdir ~/github && cd ~/github && git clone https://github.com/sdcityrobotics/zoidberg_software && git clone https://github.com/sdcityrobotics/zoidberg `

## Getting started with linux
* To get started with Linux you can watch an asortment of videos
* Topics can include
* creating systemd services
* system updates
* disabling hibernation
