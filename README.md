# Coachbot Automated Swarm Testbed: Quickstart

The Coachbot Swarm and this repo is owned and maintained by the Rubenstein Lab at Northwestern University. If you have any questions, comments or concerns, please email us at coachbotswarmsystem@gmail.com and someone from our team will get back to you. We ask that you respect the system and help us keep it accessible to fellow swarm enthusiasts by adhering to the guidelines explained in this guide. We reserve the right to refuse access to any individuals who are not courteous to the system or the Coachbot team.

This quickstart guide is a great place to start to build your first experiment but check the user guide for more detailed information about how to use the system and troubleshooting: ***https://coachbotswarm.github.io/User-Guide/***
These guides will walk you through the steps to set up the required environments, how to request access to the platform, link you to the simulator, understand the repositories and files needed to make a submission, break down the robot API, and explain the results that will be returned to you. To familiarize yourself with the platform, the API, and the workflow, we highly recommend you start with submitting code from the Example folder. We also recommend using the simulator for each experiment for faster verification before submitting your algorithm to the physical platform.

If you have any questions about setting up the experiment you would like to run, please reach out to us with any inquiries.

## Required Installs
### Python
Our swarm runs algorithms written in the Python programming language (python 2.7.16). To install python, please visit the official downloads page (https://www.python.org/downloads/) and select the appropriate OS for your machine and scroll down to find the python 2.7.16 release. Once the python set up prompt is complete, ensure that everything is installed properly by opening command prompt (or OS equivalent) and running *python --version*. This should output python 2.7.16 in the terminal. 

If using a later version of python, please make sure that any libraries used in the algorithm are available in the python version specified above.

To begin coding, we recommend using an IDE (Integrated Development Environment). If the reader doesn't have a currently prefered IDE, we recommend Visual Studio Code (https://code.visualstudio.com/download) which is widely used and available for Windows, Mac, and Ubuntu. 

### Github
For our testbed, we currently use the popular system, Github, as a platform for users to submit their experiments to and receive results. To get started, make an account on https://github.com/ (a free account will be sufficient for our system). There are two popular ways to use Github on your local machine, which are explained below.

#### Github Desktop
Github Desktop is a convenient interface to utilize git tools without needing to use the terminal. Download the tool from https://desktop.github.com/. Look for the “Current Repository” Menu on the top left below the banner. In that dropdown menu, click “add” and select “Clone repository…”.  In the Github repo you wish to clone, select the green “< > Code” dropdown button and copy either the https or ssh link. Which you choose is a matter of personal preference, but explore this reference to learn more about the differences: https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories. Once you have either the https or ssh link copied, go to Github Desktop and paste this link in the “URL” section. Make sure your local path points to where you want the repo to be housed and click the blue “clone” button. Now you should be able to pull by clicking “Pull Origin” in the top banner, see your changes on the left bar, commit changes in the bottom left corner, and push code with the button in the top banner. The option to push will not appear if you have no changes. Please remember to always pull before you push and save a local copy of your code outside the repo.  

#### Terminal
To use git through your preferred terminal, you must first download the appropriate packages. Follow this link to download Git for your OS: https://github.com/git-guides/install-git. Once you have downloaded git and checked for successful installation, you can clone the repo. In the Github repo you wish to clone, select the green “< > Code” dropdown button and copy either the https or ssh link. Which you choose is a matter of personal preference, but here is a reference to learn more about the differences: https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories.  In your terminal, navigate to where you want the local repo to be housed. Type *git clone* and paste the https or ssh link and hit enter. This will clone the repo to your local folder and you can now make changes to the files or folders as desired on oyur local machine. The *git status* command highlights any changes on your local system that have not been sent to the repo. To contribute your changes to the repository so that others may access it, first *git add* the files that are shown as changed when you ran *git status*. Once those changes have been added, run *git commit -am ""* with a message between those quotes briefly explaining your changes. Finally now that your changes have been committed, you can use *git pull* to make sure there will be no overriding issues and then *git push* your changes to the repository. As a good git practice, please remember to always run the *git pull* command before you *git push* to avoid any conflicting code between collaborators. A quick guide to important and commonly used git commands can be found here: https://training.github.com/downloads/github-git-cheat-sheet/. The commands that will most commonly be used are *git pull, git status, git add, git commit*, and *git push*.

#### Note for Chromebook Users
Github is not inherently supported on Chromebooks and thus will require some extra setup. We recommend following these two guides to get git set up either for terminal or Github Desktop usage.

GitHub Desktop Setup Guide: https://www.addictivetips.com/chromebook/install-github-desktop-on-chrome-os/

Git Terminal Guide: https://www.geeksforgeeks.org/how-to-install-git-on-chrome-os/

## Obtaining Contributer Access to the Repo
To gain access to our Coachbot-Swarm organization and start submitting experiments, email us at coachbotswarmsystem@gmail.com with your name, university (if applicable), and github username associated with the account. After emailing us, users will receive an email (to the address linked to the Github username) inviting them to join the Coachbot-Swarm organization. Please allow up to one business day for this invitation from when we were emailed. Once the user accepts the invite to the organization, they'll get write access to two repositories, and read access to a third repository. The first of the repositories is named submission_repo, where users will be able to, as the name suggests, submit experiments. Details on this process are outlined in sections below. The second is a private repository which has the same name as the Github username that was requested to be a collaborator to the platform. This repository is where the user and any collaborators they choose to add can iterate on experiments, prep files for submission, and access results. This private repository contains a skeleton template for the 4 files explained below that a submission is comprised of. Further sections below walk through the files needed for submission and the available robot API functions.

## Getting Familiar with the System through the Example Repository
The third repository seen in the organization is *Examples*. This repository contains various examples of submissions highlighting different robot API calls and is a great starting reference point to get familiar with how to submit to the Coachbot Swarm Platform. The simple steps below will help users submit their first experiment to the platform.
1. Clone the Example repository to your local system
2. Navigate to the "Simple Example" Folder and view the 4 files present which make up a submission
3. Clone your private repository to your local system (this will be the repository named with your github username that you received access to once you accepted the invitation to join the Coachbot-Swarm organization)
4. Copy these 4 files to your private repository (without the folder)
5. Open the email_simple_example.txt file and enter in the email address you would like to be associated with this submission
6. Change the name of the github_username.json file to be the github username that matches the name of your private repository (ex. if my github username/repo name is dornadulavaishnavi, then my new file would be dornadulavaishnavi.json)
7. Push these 4 files to the main branch of the private repository
8. Clone the *submission_repo* repository to your local system
9. Copy just the renamed .json file to the *submission_repo* and push to the main branch
10. Your example code has now been submitted to run on the Coachbot Swarm Testbed (Note: when the testbed is running, the submission is immediately loaded locally and deleted from the repository)
11. Users can expect to receive up to 3 emails from the system per submission, one confirming validity, one for the start of the experiment, and the last being a notification of completion.
12. The results of the experiment will be found on a new branch in the user's private repository with the appropriate time stamp.

## Writing Code for the Coachbot Swarm
### Experiment Code (usr_code.py)
The experiment code must be written in a particular format to run properly on the swarm and every robot in the experiment will run the same user code. A skeleton reference of the this usr_code file (usr_code.py) is provided in the repository, as well as a file showing example usage of the provided API calls (usr_code_api_examples.py). These files contain the proper format to begin writing an algorithm for the robots. More information can be found in the User Guide: ***[https://coachbotswarm.github.io/User-Guide/#available-robot-functions](https://coachbotswarm.github.io/User-Guide/#user-code)***

#### Robot API Functions
Functions are available for a user to access the robot's capabilities and perform tasks such as motion, messaging, and localization. Read about these functions and their usage in the User Guide: ***https://coachbotswarm.github.io/User-Guide/#available-robot-functions***

Check out our API Overview tutorial here for a quick introduction: [https://youtu.be/KC8QtUyUukE](https://youtu.be/Z8qkd0gtyGM)

### Initial Swarm Positions (init_pose.csv)
This file specifies the starting position of each robot needed in the experiment. The values specified must follow the rules listed in the User Guide at ***https://coachbotswarm.github.io/User-Guide/#initial-positions***

If the init_pose.csv file does not abide by the rules above, users will receive an email and an error file specifying the issues. 

## Acessing and Running Experiments on the Coachbot Swarm Simulator
Our testbed features a corresponding simulator that is compatible with Windows, Mac, and Linux machines. This tool is publicly located through Github and can be used to test algorithms at faster speeds and larger swarm sizes before being run on the physical testbed (***https://github.com/michelleezhang/swarm_simulation/tree/master***). Exact instructions on using this simulator are located in the README of its repository. Once the results on the simulator match the expectations of the user, it is then ready to be run on the physical testbed.

## Submitting Code to be Run on the Physical Coachbot Swarm System

To submit an experiment to run on our Coachbtos system, users will upload a *.json* file specifying the files involved in their experiment to the submission_repo repository in the organization. Every submission to our system must specify three files and be named as the github username being submitted from as shown in the *github_username.json* file in the user's private repository. This guide will refer these three files by their default names but are not required to match. The files specified in the *.json* submission are the ones that will be run by the platform. The first is a .txt file called email.txt which simply contains the email address that should be contacted about the submitted code. The second file specifies the initial positions of the robots before the user code is run. Specifications of that file’s format and restrictions on robot positions are outlined above and in the User Guide. The third mandatory file is the code that will be uploaded to all active robots. This file, usr_code.py, must be written in python and formatted in the way outlined above and in the User Guide. After pushing these 3 completed, required files into the main branch of the user's private repositoy, fill out the *github_username.json* with the appropriate files names and rename this *.json* file to the github username of the private repository. This *.json* file then needs to be copied and pushed to the *submission_repo* repository to be submitted to our platform and run on the Coachbot robots. See the Github section above or in the User Guide for a refresher on how to contribute code to a repository. Once the *.json* has been pushed to the *submission_repo* repository, the experiment has been successfully submitted to the testbed! Sit back and eagerly await the experiment results!

An example submission with these three mandatory files are located in the main branch of the private repository. These files will showcase various robot functionalities and are a good place to start getting familiar with our platform and robot capabilities. To begin experimenting with the platform, we recommend taking a look at these files and editing them to create a first submission. Try changing the initial positions and number of robots in the init_pose.csv file or edit parameters to change behaviors such as how long the robots drive for or their LED color to understand how the API calls work. Be sure to change the email in the email.txt appropriately.

Check the User Guide for more details on the guidelines of these input files.

## What to Expect from Running an Experiment on the Physical Coachbot Swarm System

Assuming the submission was valid and passed our verification, users will receive an email alerting them that their experiment's results are ready. The results of the algorithm will be pushed to a seperate branch in the private repo. This branch will be named with the time stamp of when the results were uploaded to the private repository. 
An explaination of the returned files can be found in the User Guide: ***https://coachbotswarm.github.io/User-Guide/#getting-the-results***
