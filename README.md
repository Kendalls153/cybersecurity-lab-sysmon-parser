# Cybersecurity Lab Environment and Sysmon Event Parser

This repository contains my cybersecurity lab environment setup, including multiple VMs, Sysmon configuration, and a Python script to parse Sysmon event logs.

---

## Lab Setup Overview

- VMs included: Kali Linux, Windows 10 Enterprise, Windows Server 2022  
- Network topology where Kali can communicate with Windows VMs; Windows VMs can communicate with each other  
- Windows Server 2022 configured as Domain Controller  
- Sysmon installed and configured on Windows 10 Enterprise to collect detailed system event logs  

---

## Python Event Parser Script

- Parses Sysmon CSV event logs and filters Event IDs 1, 3, and 10 into separate CSV files. (These ID's can be changed or altered depending on the data needed.)  
- Helps analyze specific event types for security investigations  

---

## Screenshots

Screenshots are provided in the `/docs/` folder and demonstrate:  

- **Network Topology Diagram**: Visualizes VM communication paths showing Kali attacking Windows machines, Windows machines communicating between themselves, and the Windows Server as the domain controller.
- **Sysmon Service Running**: Shows Sysmon running on Windows 10 Enterprise, confirming proper installation and configuration using the SwiftOnSecurity config.
- **Sysmon Event Logs**: Displays event logs of sysmon before parsing takes place.   
- **Python Script Execution**: Terminal screenshot of the parser script running, showing the command prompt, open CSV output files, and folder structure with generated files.  
- **Sample CSV Output**: Displays filtered Event ID CSV files open to demonstrate the kind of data extracted for analysis.  
