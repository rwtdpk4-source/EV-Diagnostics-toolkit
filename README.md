# EV Diagnostics Toolkit
 Python scripts for analyzing electric vehicle battery and diagnostic data,
built by a Tesla High Voltage Technician learning to bridge hands-on EV
hardware experience with software/data skills.
 
## Background
 I work as a High Voltage Technician at Tesla, diagnosing and repairing
EV electrical and battery systems. This repo documents my journey
learning Python to analyze the kind of data I work with every day —
cell voltages, fault thresholds, and battery health metrics.
 
## Projects
 ### 1. Voltage Analyzer (`FirstProgram.py`)
A basic script that takes a list of battery cell voltages and:
- Finds the highest and lowest voltage in the pack
- Calculates the average voltage
- Flags a warning if any cell drops below a safe threshold (388.0V)
 
This mimics a simplified version of what a Battery Management System (BMS)
does in real time — monitoring cell balance and triggering alerts on
abnormal readings.
 
**Example output:**
The highest voltage is: 395.2
The lowest voltage is: 385.3
The average voltage is: 390.65
Warning: Low cell voltage detected
 
## Goals
 This repo will grow to include:
- OBD-II / CAN bus data logging and analysis
- EV battery health (SOH) prediction using ML
- Embedded CAN logger projects (ESP32 + MCP2515)
 
## Tech Stack
- Python 3
- VS Code
 
