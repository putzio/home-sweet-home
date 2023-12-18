# Home server

## Requirements:
You need to install:
- git
- python3
- mysql

## Prepare enviroment 

On linux simply run the startup.sh script. it will set up virtual enviroment (reccomended) and download all of the necessary packages. 

## Setup MySQL

### On linux (apt based e.g. mint)

Follow this tutorial: https://linuxhint.com/install-mysql-linux-mint-ubuntu/

## Using precommit

### Instalation
If you haven't runned the `startup.sh`:
0. Install python3
1. Install precommit using `pip install pre-commit`
2. Instal git hook scripts: `pre-commit install`

### Usage
In our case it will simply check if the change files are properly formatted (using flake8) and format it if neccesary (using black) every time you commit changes. 

You can also always check all of the project files by running `pre-commit run --all-files`.

For more info check out https://pre-commit.com/


### Flake8 config
The flake8 configuration is stored in `.flake8` file
### Black Formatter config
The black formatter config are stored in `pyproject.toml` file