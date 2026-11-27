
# OPERATION PHANTOM SWIPE
## Digital Forensic Investigation Report

**Assignment:** Assignment 1 – Unit 1: Foundations of Digital Forensics  
**Investigation Type:** ATM Skimming and Online Credit Card Fraud  
**Case ID:** OPS-001  
**Prepared by:** [Your Name]  
**Course:** B.Tech CSE (AI-ML)  
**Date:** 27 November 2026  

---

# 1. Executive Summary

Operation Phantom Swipe is a simulated digital forensic investigation involving an alleged cross-border ATM skimming and online credit card fraud operation.

The purpose of this investigation is to demonstrate foundational digital forensic techniques, including cybercrime classification, evidence acquisition, evidence preservation, forensic searching, cryptographic analysis and legal considerations.

Two suspect devices were considered in the simulation: an ATM skimming device and a mobile phone containing suspicious applications and communication records.

Synthetic evidence files were created to represent card data, communication logs, GPS coordinates, transaction records and email communications.

Python scripts were developed to calculate SHA-256 hashes, search digital evidence and simulate a dictionary-based password attack.

This investigation demonstrates the importance of maintaining evidence integrity, documenting forensic procedures and following appropriate legal and ethical principles.

# 2. Incident Description and Cybercrime Classification

## 2.1 Incident Overview

The simulated incident involves a group suspected of collecting payment card information through an ATM skimming device and subsequently using the collected information for unauthorized online transactions.

The investigation focuses on three major activities:

- ATM skimming
- Credit card cloning
- Online financial fraud

The activities may involve multiple individuals and digital devices operating across geographical boundaries.

## 2.2 Cybercrime Classification

### ATM Skimming

ATM skimming involves the unauthorized capture of payment card information using a device attached to or placed near an ATM.

Classification:
- Financial cybercrime
- Unauthorized data collection
- Payment card information theft

### Credit Card Cloning

Credit card cloning involves reproducing payment card information for fraudulent use.

Classification:
- Identity theft
- Financial fraud
- Payment card fraud

### Online Credit Card Fraud

Online credit card fraud involves using payment information without authorization to conduct digital transactions.

Classification:
- Computer-related fraud
- Financial cybercrime
- Identity misuse

# 3. Legal Framework

## 3.1 Information Technology Act, 2000

The following provisions may be relevant depending on the facts and available evidence:

| Section | Description |
|---|---|
| 43 | Unauthorized access, downloading or copying data |
| 66 | Computer-related offences |
| 66B | Dishonestly receiving stolen computer resources or communication devices |
| 66C | Identity theft |
| 66D | Cheating by personation using computer resources |

## 3.2 Indian Penal Code, 1860

The assignment requires mapping the incident to IPC provisions.

| Section | Description |
|---|---|
| 379 | Theft |
| 420 | Cheating and dishonestly inducing delivery of property |
| 463 | Forgery |
| 468 | Forgery for the purpose of cheating |
| 471 | Using forged documents or electronic records as genuine |

These are potential provisions for academic analysis. The applicability of each provision depends on the facts and evidence.

Note: The Bharatiya Nyaya Sanhita (BNS), 2023 replaced the IPC from 1 July 2024. Current investigations must consider the applicable BNS provisions and transitional rules.

## 3.3 Budapest Convention

The Budapest Convention provides an international framework for addressing cybercrime.

Relevant provisions include:

- Article 2: Illegal access
- Article 3: Illegal interception
- Article 4: Data interference
- Article 7: Computer-related forgery
- Article 8: Computer-related fraud
- Article 23: International cooperation

India is not a party to the Budapest Convention. It is discussed here as a comparative international framework.

# 4. Electronic Evidence Collection

## 4.1 Simulated Evidence Acquisition

Two suspect devices were considered:

**Device 1: ATM Skimmer**
- Simulated card information
- Device-related records
- Synthetic data files

**Device 2: Mobile Phone**
- Simulated communication records
- Suspicious application-related information
- Transaction-related records

Synthetic evidence files were created in the GitHub repository.

The evidence includes:

1. card_data.txt
2. communication.log
3. gps_data.txt
4. transactions.csv
5. email_evidence.txt

## 4.2 Evidence Preservation

Digital evidence must be handled carefully to prevent modification or contamination.

The following forensic principles were considered:

- Evidence should be documented before examination.
- Original storage media should be preserved.
- Write blockers should be used when acquiring physical storage media, wherever applicable.
- Forensic copies should be created for examination.
- Cryptographic hashes should be calculated to verify integrity.
- Every evidence transfer should be documented.

## 4.3 Chain of Custody

A Chain of Custody form was created in CSV format.

It records:

- Evidence identification number
- Device description
- Collection date
- Investigator information
- Hash verification status
- Storage status

This record provides a structured method for documenting evidence handling.

# 5. SHA-256 Hashing and Evidence Integrity

SHA-256 is a cryptographic hashing algorithm that produces a 256-bit digest.

It helps verify whether digital evidence has changed.

A Python script named generate_hashes.py was developed.

The script:
1. Reads evidence files.
2. Calculates SHA-256 hashes.
3. Displays the hash values.
4. Saves the results in SHA256SUMS.txt.

The hash records are stored in the hashes folder.

If a file changes, its calculated hash will normally differ from its previously recorded hash.

This technique helps establish the integrity of acquired digital evidence.

# 6. Electronic Media Search and Analysis

A Python forensic analysis script was developed to search the simulated evidence files.

The script searches for:

- Email addresses
- Card-like number sequences
- GPS coordinates
- Suspicious keywords
- Communication-related information

The analysis output is saved as analysis_results.txt in the report folder.

The findings demonstrate how automated searches can help investigators identify potentially relevant digital artefacts.

All extracted information is synthetic and intended only for academic demonstration.

# 7. Cryptography and Password Analysis

## 7.1 Password-Protected Evidence

A simulated password hash was created to demonstrate password analysis techniques.

The investigation uses a sample MD5 hash and a small predefined dictionary.

## 7.2 Dictionary Attack Simulation

A Python script named password_cracking.py was developed.

The script:
1. Reads the simulated password hash.
2. Loads predefined candidate passwords.
3. Calculates the MD5 hash of each candidate.
4. Compares each calculated hash with the target hash.
5. Records whether a matching password is found.

The result is saved in password_cracking_results.txt.

This is a controlled educational simulation and does not involve accessing real accounts or devices.

## 7.3 Ethical Considerations

Password cracking can create serious privacy and security concerns.

It should only be performed with proper legal authorization and on systems or data that the investigator is permitted to examine.

Law enforcement should consider lawful decryption requests and applicable legal procedures before attempting access to protected information.

## 7.4 Password Strength

Weak and commonly used passwords are vulnerable to dictionary attacks.

Users should:
- Create long and unique passwords.
- Avoid common dictionary words.
- Enable multi-factor authentication.
- Use secure password managers.

Modern systems should use dedicated password hashing algorithms such as Argon2id rather than plain MD5.

# 8. Cross-Border Investigation Challenges

Cross-border cybercrime investigations involve several difficulties.

### Jurisdiction

Criminal activities may involve different countries, making it difficult to determine which authorities have jurisdiction.

### Evidence Access

Digital evidence may be stored on servers located outside the investigating country.

### International Cooperation

Investigators may require cooperation from foreign law enforcement agencies and service providers.

### Data Privacy

Different countries have different privacy laws and data protection requirements.

### Evidence Preservation

Digital evidence may be deleted, modified or become inaccessible if it is not preserved promptly.

International cooperation and standardized evidence handling procedures are therefore important.

# 9. Recommendations for Law Enforcement

The following improvements are recommended:

1. Establish standardized digital evidence acquisition procedures.
2. Train investigators in modern forensic tools and techniques.
3. Maintain detailed chain-of-custody documentation.
4. Use cryptographic hashing for evidence integrity verification.
5. Improve coordination between cybercrime investigation units.
6. Develop procedures for requesting international digital evidence.
7. Maintain secure evidence storage facilities.
8. Encourage public awareness of payment card security.

# 10. Tools and Technologies Used

| Tool | Purpose |
|---|---|
| GitHub | Project repository and version control |
| Python 3 | Forensic automation |
| hashlib | SHA-256 and MD5 calculations |
| pathlib | File handling |
| re | Pattern matching |
| GitHub Actions | Automated execution |
| CSV | Evidence documentation |

# 11. Conclusion

Operation Phantom Swipe demonstrates the basic principles of digital forensic investigation through a simulated ATM skimming and online financial fraud scenario.

The project covers cybercrime classification, evidence collection simulation, chain-of-custody documentation, cryptographic hashing, forensic file searching and password analysis.

Python scripts and GitHub Actions were used to automate important parts of the investigation.

The exercise highlights the importance of preserving digital evidence, maintaining integrity through cryptographic hashing and following legal and ethical procedures.

Digital forensics plays an important role in identifying cybercrime activities and supporting reliable investigations.

# 12. Authorship Declaration

I declare that this assignment is prepared for academic purposes using simulated digital evidence and educational forensic scripts.

The evidence records and investigation scenario are fictional. No real financial accounts, payment cards or private devices were accessed.

**Student Name:** vansh sharma

**Course:** B.Tech CSE (AI-ML)

**Signature:** __________________

**Date:** __________________
