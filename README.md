# FILEINTEGRITY CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: BHARATH B M

*INTERN ID*: CTIS6523

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

DESCRIPTION:
  The File Integrity Checker is a cybersecurity-based tool developed using Python to ensure the safety and consistency of digital files. The primary purpose of this task is to detect any unauthorized or accidental changes made to a file by comparing its current state with its original state. In today’s digital world, maintaining data integrity is extremely important, especially when dealing with sensitive information such as documents, software files, and system configurations. Even a small modification in a file can lead to security risks, data corruption, or system failure.

This project uses cryptographic hashing techniques to verify file integrity. A hash function is a mathematical algorithm that converts input data into a fixed-length string known as a hash value or digest. In this task, the SHA-256 hashing algorithm is used through Python’s hashlib library. SHA-256 generates a unique and consistent hash value for each file based on its content. Even a minor change in the file, such as adding a single character, results in a completely different hash value, making it highly reliable for detecting modifications.

The working of the File Integrity Checker begins by selecting a file that needs to be monitored. The program reads the file in binary format and processes it in small chunks to efficiently handle large files. It then generates the hash value using the SHA-256 algorithm. This initial hash value is stored in a separate file, which acts as a reference for future comparisons.

When the integrity check is performed again, the program recalculates the hash value of the same file and compares it with the previously stored hash. If both hash values are identical, the program confirms that the file has not been modified and remains intact. However, if there is any difference between the two hash values, the program alerts the user that the file has been altered. This helps in identifying unauthorized access, malware infection, or accidental changes.

This tool has several practical applications in real-world scenarios. It can be used by system administrators to monitor important system files, by developers to verify software distribution, and by users to ensure that downloaded files have not been tampered with. It is also useful in digital forensics and cybersecurity operations where data authenticity is critical.

The File Integrity Checker is simple yet effective and demonstrates the practical implementation of cryptographic concepts in Python. It also enhances understanding of file handling, data security, and hashing techniques. Overall, this task provides valuable insight into how integrity verification mechanisms work and highlights their importance in protecting digital assets from potential threats.


OUTPUT:
  Enter file path to monitor: test.txt
Hash saved successfully!
