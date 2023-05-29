# Vote System

Vote System is a secure voting application that implements zero-knowledge proof and ECDH encryption and decryption. It provides a client-server architecture where clients can participate in polls while maintaining the confidentiality and integrity of the votes. The voting data is stored in Excel sheets.

## Authors

- Itzik Rahamim
- Gil Ben Hamo
- Yovel Aloni

## Description

Vote System is a secure voting application that implements zero-knowledge proof and ECDH encryption and decryption. It provides a client-server architecture where clients can participate in polls while maintaining the confidentiality and integrity of the votes. The voting data is stored in Excel sheets.

## Features

- Key exchange with ECDH:
  - Generates private and public keys for both sides.
  - Each side sends its public key to the other to establish a shared key.
- Encryption with AES:
  - The client sends text to the server.
  - The server encrypts the text and sends it back to the client.
  - The client can decrypt the message.
- Zero knowledge proof:
  - Every vote generates a unique token.
  - You can verify the validity of the token by entering it to the Committee.

## Requirements

- Python 3.9 (or above)
- Make sure you have installed all the packages listed in "requirements.txt"

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/eizikr/VoteSystem.git
   
2. Install the required packages::
   ```shell
   pip install -r requirements.txt
   
3. Start the server:
   ```shell
   python server.py

4. Start the client:
   ```shell
   python client.py

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Commit your changes.

4. Push your changes to your forked repository.

5. Submit a pull request explaining your changes.

## Contact
- Name: Itzik Rahamim
- LinkedIn: [Itzik Rahamim](https://www.linkedin.com/in/itzik-rahamim-developer)
- Email: eizikr@icloud.com
