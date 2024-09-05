## About
A website for a pizza restaurant named "Il Forno Magico".

## Development environment
* **OS:** Windows 11
* **Browser:** Chrome v.127.0.6533.120
* **Code editor:** Visual Studio Code (VS Code) v.1.92.2
* Python v.3.12.5

    * Selenium v.4.23.1 (needed for the [testing system](#installation-of-testing-system))

* nodejs v.20.17.0 (needed for the [TypeScript system](#installation-of-typescript-system))


## Installation of testing system
To get started with our testing system, follow these instructions:

1. Open the python file located at **tests/testMain.py** in VS Code. 
2. In the VS Code menu bar, navigate to **View -> Testing**.
3. Click on “Configure Python Tests”.
4. Click on “unittest”.
5. Click on “tests”.
6. Click on “test*.py”.
7. Restart VS Code.

## Generating screenshots of the website in different resolutions

1. Run "screenshots.py"
2. The screenshots will be saved in "/generatedScreenshots/"

## Deploy GitHub Page

1. Open a browser
2. Open github.com and log in
3. Open the repository "JITS Pizzeria"
4. In the repo, navigate to “Settings”
5. Under “Code and automation”, navigate to “Pages”
6. Under “Build and deployment”, set “Source” to “Deploy from a branch”
7. Under “Branch” select “Main” on the left and “/ (root)” on the right. Press “Save”.

## Font system

All used fonts are defined in "/styles/fonts.css". Fontfiles should be placed in "/styles/"

## Hosting system, how to access

In a command prompt, enter:
* “ssh root@37.123.128.130 -p 30234”
* “cd var/www/html”

If there is nothing in the folder:
* “git clone https://github.com/NTIG-Uppsala/JITS-pizzeria .”

If there is a problem, check that nginx and git are installed:
* “apt install nginx git”

## Publish a new version of the website:

In the hosting system's var/www/html directory, type:
* “git fetch”
* “git checkout {tag}” *tag is the name of the new version that you have named in your git repository (to be named according to semantic versioning)