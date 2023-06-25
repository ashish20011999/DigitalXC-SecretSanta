# Secret Santa Game

The Secret Santa Game is a Python program that facilitates the generation of Secret Santa assignments. It ensures that each participant is assigned a different person to buy a gift for, while keeping the assignments a secret.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Secret Santa Game program is designed to automate the assignment generation process for a Secret Santa game. It takes a list of participants, previous assignment data (optional), and generates new assignments. The program ensures that each participant is assigned a different person and produces an output file containing the assignments.

## Installation
1. Clone the repository to your local machine.
2. Ensure that Python 3.x is installed on your system.
3. Install the required dependencies by running the following command:


## Usage
1. Prepare the participant list and previous assignment data (if available) in CSV format.
2. Update the necessary file paths in the `assignment.py` file.
3. Run the program by executing the following command:
   #python3 test_assignment.py //for running with test cases
   #python3 assignment.py  //for running without test cases

4. The program will generate the Secret Santa assignments and store them in the specified output file.

## File Structure
The file structure of the project is as follows:

Secret-Santa/
|-- assignment.py
|-- Employee-List.csv
|-- Secret-Santa-Game-Result-2023.csv
|-- secret_santa_assignments.csv
|-- test_assignment.py
|-- README.md
|-- requirements.txt


- `assignment.py`: Main Python script that generates Secret Santa assignments.
- `Employee-List.csv`: CSV file containing the list of participants.
- `Secret-Santa-Game-Result-2023.csv`: CSV file containing the previous assignment data (optional).
- `secret_santa_assignments.csv`: Output file where the new assignments will be stored.
- `test_assignment.py`: Unit tests for the assignment generation process.
- `README.md`: Documentation file describing the project.
- `requirements.txt`: List of Python dependencies required for the project.

## Contributing
Contributions to the Secret Santa Game project are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.

When contributing to this repository, please first discuss the change you wish to make via the issue tracker or email before making a change.

## License
This project is under private onwership under @Ashish Kumar Samal
