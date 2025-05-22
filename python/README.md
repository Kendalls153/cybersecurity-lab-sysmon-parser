# Sysmon Event Log Parser

This folder contains the Python script used to parse Sysmon event logs (CSV format) and filter specific event IDs into separate files.

---

## Files

- `event_parser.py`: Python script to filter Sysmon logs  
- `sysmon_sample.csv`: Example input CSV log file   
- `/logs_output/`: Directory where filtered CSV files are saved  

---

## Usage

1. Place your Sysmon CSV log file (`sysmon_sample.csv`) here or update the script with your input path.  
2. Create the `/logs_output/` folder if it doesn’t exist.
3. Run the script with the correct paths inserted and it will extract requested event id data from the sysmon log and export it into a new event specific CSV. Events can be changed or added as needed.