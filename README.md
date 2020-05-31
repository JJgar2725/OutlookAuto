# OutlookAuto - automating emails

Hello! This is OutlookAuto.

This project idea mainly came from the desire to learn what Python automation is like. With the usage of basic Python modules, such as the **os** an **sys** modules, along with **Selenium**, a webscraping module, this project came to life. **Selenium** is was allowed the project to truly work out, allowing the program to navigate the browser and send inputs where needed.

Below details the basic functionality of the program, as well as installation and usage commands.

## **_Installation_**

First clone the Github repository and move into the created directory to install the needed Python modules from the requirements.txt and create the .env file with your login credentials.

```
git clone "https://github.com/JJgar2725/OutlookAuto.git"
cd OutlookAuto
pip install -r requirements.txt
touch .env
```

Inside the .env file, your login credentials should be in the following format:

```
USER-NAME=your username goes here
PASSWORD=your password goes here
```

Make sure to have chromedriver installed and added to PATH before continuing.

From here, depending on the operating system, you have a few different steps of making you life a bit easier in using this project.

### *_Windows_*

On Windows, you can alleviate the process of navigating to the project directory by creating a shortcut to the batch file that comes with this project.

### *_Mac_*

On Mac, the steps to automating the process is somewhat longer than the Windows method. I'll be assuming that you've never created a custom bash command before in order to explain the process effectively.

1. The .my_commands file that is provided in this Github repository is a file that should be placed in your home directory, and this could be navigated to by typing ```cd``` into your terminal. Edit this file according to where you want to place the OutlookAuto project, and make it so it navigates to that path automatically before executing the python script.

2. Next, you should set the file permissions in order to allow this command to run in the terminal. In order to do this, run the following command in a terminal session: ```chmod +x .my_commands.sh```.

3. Finally, you should find the .bashrc/.zshrc and add the following line to the end of the file: ```source ~/.my_commands.sh```. This will allow for the command to be run from any terminal.

## **_Windows Usage_**

When running the program, the command prompt should first ask you for an email and subject line to add to your email. Enter your information, and hit enter to begin the execution of the script.

```
Email: exampleemail@gmail.com
Subject: Question on Example Subject
```

## **_Mac Usage_**

When running the program through terminal, the command should be called with two parameters, as shown below.

```outlook exampleemail@gmail.com Question on Example Subject```

If the command is run without parameters, your installed chromedriver will open a chrome window and pause until an email and subject is provided through the terminal. If no email or subject is to be desired, just hit enter again. The input is similar to the Windows usage explanation. 