# Password Generator and Cracker

## Description
Developed in 2023, "Password Generator and Cracker" is a university project made during the fourth course of Computer Engineering at UC3M in collaboration with @juliassanchez.

It was made for the subject "Cybersecurity Engineering" and corresponds to one of the practices of this course. The main goal of the project is to learn how to crack passwords using **John the Ripper in Kali Linux**. To do so, a script to generate the passwords is written first.

**NOTE:** The code and comments are in spanish.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Content of the Repository](#content-of-the-repository)
- [License](#license)
- [Contact](#contact)

## Installation
The script to generate the passwords needs the following library to work:
```sh
pip install passlib
```

To try the examples given to crack passwords, Kali Linux is needed as well.

## Usage
To generate the passwords just use the following command:
```sh
python3 generador_contraseñas.py
```
**NOTE:** This operation will take a while.

John The Ripper's commands must be put in a Kali Linux terminal.

## Content of the Repository
This repository includes **2 main elements**:

- **generador_contraseñas.py:** A script to generate datasets of passwords with varying lengths and complexity. Upon execution, it will create four main directories: "contraseñas_1" and "contraseñas_2" containing plaintext passwords to be encrypted using MD5 and SHA512, respectively, and "datasets_1" and "datasets_2" containing the MD5 and SHA512 encrypted versions of these passwords for cracking.

- **john-commands.md**: A file with example commands demonstrating how to use John the Ripper with various cracking strategies.

## License
This project is licensed under the **MIT License**. This means you are free to use, modify, and distribute the software, but you must include the original license and copyright notice in any copies or substantial portions of the software.

## Contact
If necessary, contact the owner of this repository.
