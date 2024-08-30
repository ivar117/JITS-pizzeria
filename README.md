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

## Installation of TypeScript system
The TypeScript code used for our product is pre-compiled and ready to be run on the website.
However, when wanting to compile and run new TypeScript code, a TypeScript compiler is needed to compile TypeScript code into JavaScript code. This can be installed via npm, which requires nodejs version 20.17.0 to be installed on the computer (https://nodejs.org/en). Then install the TypeScript compiler through running:

    $ npm install typescript --save-dev

Now the compiler is installed and ready to be used. To compile TypeScript code, run the following command:

    $ npx tsc

This will compile all TypeScript files in the **src** directory to JavaScript files that are outputted in the **build** directory. The file **tsconfig.json** describes the configuration of the compilation system.