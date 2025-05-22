# Sysmon Configuration and Setup 
This folder contains configuration files and documentation for the Sysmon setup on the Windows 10 Enterprise VM.


--- 


## Sysmon Installation - Sysmon installed on Windows 10 Enterprise to collect detailed process, network, and system event logs. 
- Configured using the popular SwiftOnSecurity Sysmon config available at: [https://github.com/SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) 


--- 


## Files 
- `sysmon-config-swift.xml`: Sysmon configuration file used (based on SwiftOnSecurity config) 
- 


--- 


## Notes 
- Sysmon logs events relevant to security monitoring, including: 
    - Process creation (Event ID 1) 
    - Network connection (Event ID 3) 
    - Process access (Event ID 10) 

- Logs are exported to CSV for parsing by the Python script in `/python/`. 