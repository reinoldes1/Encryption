<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">File Encryption Tool</h3>

  <p align="center">
    A personal cybersecurity and cryptography learning project that demonstrates secure file encryption and decryption using Python. Built to deepen knowledge in cryptographic principles and strengthen Python programming skills.
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#how-to-run">How to Run</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project

This is a personal learning project focused on understanding cryptographic concepts and strengthening cybersecurity fundamentals through practical implementation in Python.

### Project Overview

The File Encryption Tool provides a command-line interface for secure file encryption and decryption using the Fernet (AES-128) algorithm. The project demonstrates:

- **Cryptographic Key Management**: Generation and storage of encryption keys
- **File-based Encryption**: Secure encryption of files using symmetric cryptography
- **Practical Security Implementation**: Real-world application of cryptographic principles
- **User-Friendly Interface**: Interactive command-line prompts for ease of use

### Key Features

- Generate and manage encryption keys securely
- Encrypt files with AES-128 (Fernet) algorithm
- Decrypt previously encrypted files
- Simple and intuitive CLI interface
- Error handling for file operations  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Cryptography][Cryptography]][Cryptography-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started with the File Encryption Tool, clone the repository:

```sh
git clone https://github.com/reinoldes1/Encryption.git
cd Encryption
```

### Prerequisites

Python 3.8 or higher is required. Install the dependencies using:

```sh
pip install -r requirements.txt
```

### Installation

### How to Run

```sh
python run.py
```

The application will guide you through key generation and file encryption/decryption options.

### How to Use

1. **Start the application**: Run `python run.py`
2. **Key Management**: 
   - Choose to generate a new key or use an existing one
   - Keys are stored in `chave.key`
3. **Encrypt files**: Select option (1) and provide the file path
   - Encrypted files are saved with `_encrypted` suffix
4. **Decrypt files**: Select option (2) and provide the encrypted file path
   - Decrypted files are saved with `_decrypted` suffix

**⚠️ Important**: Keep your encryption key (`chave.key`) safe and secure. Without it, encrypted files cannot be recovered.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] **User Authentication System**: Implement username and password-based access control
- [ ] **Database Integration**: Store encryption metadata and user credentials securely
- [ ] **Web Frontend**: Build a user-friendly web interface for file management
- [ ] **Key Derivation Function (KDF)**: Implement PBKDF2 or Argon2 for password-based key derivation
- [ ] **File Integrity Verification**: Add HMAC-based integrity checking for encrypted files
- [ ] **Batch File Processing**: Support encryption/decryption of multiple files simultaneously
- [ ] **RSA Hybrid Encryption**: Combine symmetric and asymmetric encryption for enhanced security
- [ ] **Secure File Deletion**: Implement secure deletion of original files after encryption

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are very welcome, feel free to make yours.

If you have any suggestions, fork the project and make a pull request!

1. Fork the project
2. Create your contribution branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top Contributors:

<a href="https://github.com/reinoldes1/Encryption/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=reinoldes1/Encryption" />
</a>

<!-- Made with [contrib.rocks](https://contrib.rocks). -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

For questions or suggestions about this project, please feel free to reach out:

- **GitHub**: [reinoldes1](https://github.com/reinoldes1)
- **Project Repository**: [Encryption](https://github.com/reinoldes1/Encryption)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/reinoldes1/Encryption.svg?style=for-the-badge
[contributors-url]: https://github.com/reinoldes1/Encryption/graphs/contributors

[stars-shield]: https://img.shields.io/github/stars/reinoldes1/Encryption.svg?style=for-the-badge
[stars-url]: https://github.com/reinoldes1/Encryption/stargazers

[issues-shield]: https://img.shields.io/github/issues/reinoldes1/Encryption.svg?style=for-the-badge
[issues-url]: https://github.com/reinoldes1/Encryption/issues

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[Cryptography]: https://img.shields.io/badge/cryptography-3776AB?style=for-the-badge&logo=security&logoColor=white
[Cryptography-url]: https://cryptography.io/