Getting started
=================

Clone this repository
-----------------------
This will download all the files in this repository to your current folder.

`git clone https://github.com/sdcityrobotics/zoidberg_software/`

Read, run, and try to understand all the files in this repository
-------------------------------------------------------------------
Read all the files in this repository and try to undestand what's going on. Run them on your own comptuer and see if you were right. Play around with it by changing some things around and seeing what happens. Google anything that's new or confusing. If you still have questins, post in the 'software write permissions' discussion group or on slack.

If you're having errors when running these files
-------------------------------------------------
Check your python and opencv versions. I'm using the following:
Python 2.7.1
OpenCV 2.4.11

To download the opencv version above:

`conda create --name new_environment`

`source activate new_environment`

`conda install -c menpo opencv`

OR you can follow this tutorial for isntalling OpenCV on your system python (you do not need anaconda for this):

*change OPENCV_VERSION='3.2.0'*

`https://github.com/milq/milq/blob/master/scripts/bash/install-opencv.sh`

Upload your own code
---------------------
We want to learn from each other, so please upload any code you've been working on! Don't forget to comment your code as much as possible so that we can all understand you're train of thought

Creating Object Detection Code
================================
This is what we're really trying to tackle. Once everything on your computer is working and you have a better understanding of OpenCV, it's time to start writing your own object detection code. There are two objects were focused on detecting for the moment: bouys and the gate (*I will add photos of both soon*). There is a lot of code online for underwater bouy detection. Google "underwater buoy detection github" and you'll find that many people have worked on accomplishing this in different ways. It can be difficult to understand other people's code at first, but it gets easier and it's a great resource for us. 

If you start to feel stuck, post on the discussion page and we'll help you out!
