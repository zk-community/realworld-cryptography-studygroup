## Lesson 1 - Hash Functions

**Expected Duration:** 2 weeks


**Plan:**
* Read Chapters 1-2 of [RWC](https://www.manning.com/books/real-world-cryptography?a_aid=Realworldcrypto&a_bid=ad500e09)
  * Understand core concepts
* Complete 
  * Challenge Exercises 
  * Explainer Questions
* Meet-up: 1x Q&A, explainers & challenge response reviews

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

2) Calculate the total theoretical number of attempts it would take to brute force a MD5 hash digest.

3) Brute force attack on a MD5 hash digest of 8bits.

4) Compute one insecure (< 128 bit) and one secure (≥ 128) hash digest of the following

- STRING: “The secret to a successful life - never stop learning!”
- JPG: (will add to github)
- WEBPAGE: will include a link

5) Explain and demonstrate how to calculates the Hamming Distance between two strings

6) What is the Hamming Distance between any bytestring hashes where i1 (unmodified) and i2 has 1 bit flipped.


### Supplementary Resources

Papers
* [Cryptographic Hash-Function Basics](https://www.iacr.org/archive/fse2004/30170373/30170373.pdf)
