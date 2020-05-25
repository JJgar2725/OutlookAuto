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

From here, depending on your operating system, you may want to make a shortcut to the outlook.bat file, or edit your my_commands.sh file to add the command to PATH.

## **_Usage_**

When running the program, the command prompt should first ask you for an email and subject line to add to your email. Enter your information, and hit enter to begin the execution of the script.

```
Email: exampleemail@gmail.com
Subject: Question on Example Subject
```
