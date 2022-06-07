## Lesson 1 - Hash Functions

**Expected Duration:** 2 weeks


**Plan:**
* Read Chapters 1-2 of [RWC](https://www.manning.com/books/real-world-cryptography?a_aid=Realworldcrypto&a_bid=ad500e09)
  * Understand core concepts
* Complete 
  * Challenge Exercises 
  * Explainer Questions
* Meet-up: Q&A, explainers & challenge response reviews

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

**Explain**

1) MD5 is said to be ‘insecure/broken’. Under what example scenarios might it still be a valid / usable solution?

2) What is the theoretical number of attempts it would take to brute force a MD5 hash digest of 1bit? 12bits? 24bits?

3) What is and how to calculate the Hamming Distance measure between two arbitrary strings.

**Challenge Exercises**

Complete in 1+ lang of your choice; for example, Python | Rust | Javascript

1) Compute one insecure (< 128 bit) and one secure (≥ 128) hash digest of the following

- STRING: “The secret to a successful life - never stop learning!”
- JPG: (will add to github)
- WEBPAGE: will include a link

2) Brute force attack on a MD5 hash digest of 8bits.

3) Prepare a function which calculates the Hamming Distance between two strings

4) Given an unmodified hash value of any arbitrary string and the hash value of that same string with after flipping 1bit, output the Hamming Distance measure between the two outputs.

### Supplementary Resources

Papers
* [Cryptographic Hash-Function Basics](https://www.iacr.org/archive/fse2004/30170373/30170373.pdf)
