# Network Indicator Triage Tool

A lightweight, automated Python utility designed for cybersecurity analysts to fast-track the investigation of network Indicators of Compromise (IoCs). This tool ingests a list of raw IP addresses, enriches them with live geographic and organizational data via a live threat intelligence API, and exports a structured, horizontal report to a spreadsheet format.

By automating the lookup pipeline, this tool reduces manual investigation workflows (copying/pasting indicators into web browsers) from minutes to seconds.

---

## Features

- **Automated API Enrichment:** Queries live geolocation and infrastructure data without requiring hardcoded API credentials.
- **Memory-Efficient File Streaming:** Streams input data line-by-line using Python context managers, allowing processing of large log exports without memory exhaustion.
- **Advanced Data Unpacking:** Implements high-performance dictionary slicing via `operator.itemgetter` to isolate core metrics in a single processing step.
- **Defensive Error Handling:** Employs explicit exception boundaries (`try/except`) to log malformed indicators or server failures without disrupting the execution pipeline.
- **Relational CSV Export:** Converts hierarchical data (JSON payloads) into a flat, horizontal relational format optimized for analytical sorting and filtering in Excel or SIEM platforms.

---

## Technical Architecture (ETL Pipeline)

The script operates as a localized Extract, Transform, Load (ETL) architecture:

1. **Extract:** Ingests raw network indicators from a local plaintext source file (`ip_data.txt`).
2. **Transform:** Sanitizes character streams using `.strip()`, handles the HTTP Request/Response lifecycle via the `requests` library, and deserializes JSON text blobs into managed Python dictionaries.
3. **Load:** Formats fields horizontally against a structured header matrix and commits the data to a permanent spreadsheet (`output.csv`).

---

## Getting Started

### Prerequisites

This project utilizes the industry-standard `requests` library for synchronous HTTP network operations. Ensure you have it installed:

```bash
pip install requests
```

### File Layout

Ensure your project folder contains the following three files in the same directory:

```text
├── triage.py      # The primary Python application script
├── ip_data.txt    # Input file containing raw IP addresses (one per line)
└── README.md      # Project documentation
```

### Usage

1. Populate `ip_data.txt` with target IP addresses you wish to investigate. Example:
   ```text
   8.8.8.8
   1.1.1.1
   9.9.9.9
   ```

2. Execute the triage script from your terminal:
   ```bash
   python triage.py
   ```

3. The console will display real-time tracking logs. Once processing completes, open the newly generated `output.csv` file in your preferred text or spreadsheet editor to review the structured intelligence report.
