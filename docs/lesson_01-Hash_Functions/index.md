## Lesson 1 - Hash Functions

**Expected Duration:** 2 weeks


**Plan:**
* Read Chapters 0-2 of [RWC](https://www.manning.com/books/real-world-cryptography?a_aid=Realworldcrypto&a_bid=ad500e09)
  * Understand core concepts (🎉 send pull requests with definitions/documentation updates 🎉)
* Complete 
  * Challenge Exercises 
* Meet-up: 1x Q&A, explainers & challenge response reviews

** Supplementary Papers **
* [Cryptographic Hash-Function Basics](https://www.iacr.org/archive/fse2004/30170373/30170373.pdf)

### Todo ###
* Add sources here that were shared in exercise code / answers / pull requests
* Prepare links/glossary of definitions and resources for all core concepts

---

## Hash Functions

### Core Concepts

#### Security Properties
- Pre-image resistance
- Second pre-image resistance
- Collision resistance

#### Hash Functions
- Obsolete: MD5, SHA1 
- Common: SHA-2, Preferred: SHA-3
- Passwords: Argon2

#### Construction Algorithms
- Merkle–Damgård
- Sponge
- TupleHash

#### Compression Functions
- Block Cipher (eg, Davies-Meyer)
- Fixed-length
- XOF - Extendable Output Function ("zoff") 

#### Related Concepts
- Hexidecimal Notation
- Random Oracle
- The Birthday Bound
- Exclusive OR operation (XOR)
- keccak-f
- Rate and Capacity (sponge)
- Shake/cShake
- Customization String
- Salts
- Domain separation
- Signature
- Serialize / Deserialize

#### Usecases
- Commitments
- Subresourece Integrity
- Distributed File Systems (eg, BitTorrent)
- Anonymous networks (eg, Tor)
- Password storage / retrieval

#### Vulnerabilities
- Length Extension Attack (eg, SHA-2)

---

**Challenge Exercises**

a. Explain your answers in English, such that anyone reading the answer for the first time can follow-along.
b. Prepare 1 or more implementations in 1 or more languages of your choice; for example: Python, Rust, Javascript.

---

1) MD5 is said to be ‘insecure/broken’. Which security properties are vulnerable? Prove it. 

2) Calculate the total theoretical number of attempts it would take to brute force various hashes digests (MD5, SHA-1, SHA256).

3) Find a digest collision of the first 4/6 bits of any two input string MD5 hash digests.

6) Explain and demonstrate how to calculates the Hamming Distance between two strings.

7) What is the Hamming Distance between any bytestring hashes where i1 (unmodified) and i2 has 1 bit flipped.

8) Explain and demonstrate the difference b/w Second Pre-Image Resistance and Collision Resistence.

9) Explain and demonstrate the calculation of 'The Birthday Bound' Paradox.

10) Find an input string which results in a SHA256 hash with 1/2/X 0's (zero)

11) Find X (look up, don't over think it): md5(X).digest() > d41d8cd98f00b204e9800998ecf8427e

12) Prepare an exercise related to XOR bitwise operations (compress/uncompress)

13) Prepare an exercise related to serialization / deserialization

14) Explain and demonstrate the difference between cryptographic hash functions and `checksum` functions (CRC32)

---

