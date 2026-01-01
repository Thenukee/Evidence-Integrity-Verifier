# 🔍 Evidence Integrity Verifier

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Focus](https://img.shields.io/badge/Field-Digital%20Forensics-blue)

A lightweight, high-performance Python utility designed for forensic investigators to calculate and verify cryptographic hashes of digital evidence. 

## ⚖️ Forensic Significance
In the field of **Digital Forensics and Incident Response (DFIR)**, maintaining the **Chain of Custody** is paramount. Any digital evidence presented in a court of law must be proven to be identical to the original data at the time of seizure. 

This tool provides a reliable way to:
1. **Establish a Baseline:** Generate hashes immediately after acquisition.
2. **Verify Integrity:** Ensure evidence has not been altered during analysis or transit.
3. **Audit Readiness:** Provide timestamped hash values for forensic reports.

## ✨ Key Features
* **Multi-Algorithm Support:** Generates **MD5** and **SHA-256** hashes simultaneously.
* **Memory Efficient:** Uses **chunked reading** (4KB blocks) to process large forensic images (`.ad1`, `.E01`, `.raw`) without exhausting system RAM.
* **Portable:** Zero external dependencies—runs on any standard Python 3.x environment.
* **CLI Driven:** Designed for easy integration into automated forensic workflows.

## 🚀 Usage

### Requirements
* Python 3.x

### Running the Verifier
Clone the repository and run the script via **PowerShell** or Command Prompt:

```powershell
# Clone the repository
git clone [https://github.com/Thenukee/Evidence-Integrity-Verifier.git](https://github.com/Thenukee/Evidence-Integrity-Verifier.git)
cd Evidence-Integrity-Verifier

# Run against a file
python evidence_verifier.py "C:\Path\To\Evidence\sample_image.raw"
