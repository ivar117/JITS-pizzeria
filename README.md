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
* `ssh root@37.123.128.130 -p 30234`
* `yes` when prompted about connecting
* `<root password>`
* `cd /var/www/html`

If there is nothing in the folder:
* `git clone https://github.com/NTIG-Uppsala/JITS-pizzeria .`
* `git checkout <tag>` *tag is the name of the latest release in the git repository

If there is a problem, check that nginx and git are installed:
* `apt install nginx git`

## Publish a new version of the website:

Access the hosting system

In the hosting system's var/www/html directory, type:
* `git fetch`
* `git checkout <tag>` *tag is the name of the new version that you have named in your git repository (to be named according to semantic versioning)

## Add user and add ssh public key for user

When logged in as root, enter:

* `useradd -m <username>`
* `passwd <username>`
* Enter desired password when prompted
* Re-enter desired password when prompted

Open a new command prompt locally on your computer:
* `ssh <username>@37.123.128.130 -p 30234`
* Enter password when prompted
* `mkdir .ssh`
* Open windows powershell locally on your computer and enter the following:
* `ssh-keygen`
* Follow the prompts, a passphrase adds extra security but is not necessary
* `cat ~/.ssh/id_rsa.pub | ssh <username>@37.123.128.130 -p 30234 "cat >> ~/.ssh/authorized_keys"`
* `ssh root@37.123.128.130 -p 30234`
* Enter the root password.
* `usermod -aG :wheel <username>`

Ensure that the contents of the directory belong to wheel by running
* `ls /var/www/html -al`

Output should be:
```
drwxr-xr-x 6 root wheel 4096 Sep  5 07:21 .
drwxr-xr-x 3 root root  4096 Sep  4 09:38 ..
drwxr-xr-x 8 root wheel 4096 Sep  5 08:30 .git
-rw-r--r-- 1 root wheel   81 Sep  5 07:21 .gitignore
-rw-r--r-- 1 root wheel  945 Sep  5 07:21 README.md
drwxr-xr-x 3 root wheel 4096 Sep  5 07:21 images
-rw-r--r-- 1 root wheel 6799 Sep  5 07:21 index.html
-rw-r--r-- 1 root wheel   58 Sep  5 07:21 package.json
-rw-r--r-- 1 root wheel  767 Sep  5 07:21 products.json
drwxr-xr-x 2 root wheel 4096 Sep  5 07:21 styles
drwxr-xr-x 2 root wheel 4096 Sep  5 07:21 tests
```

Type the following to be able to execute git commands
* `git config --global --add safe.directory /var/www/html`

Type the following to check that everything works
* `git log`

## Create a new group and give it permissions to edit /var/www/html

* `groupadd wheel`
* `chown -R :wheel /var/www/html`
* `chmod -R 775 /var/www/html`