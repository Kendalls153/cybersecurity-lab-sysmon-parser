import csv

input_file = './sysmon_sample.csv' #path for initial sysmon file

output_files = { #path for new log outputs
    '1': './logs_output/sysmon_event_1.csv', 
    '3': './logs_output/sysmon_event_3.csv',
    '10': './logs_output/sysmon_event_10.csv'
}



filtered_data = {    #storage area for the data being filtered, which are Event ID's in this case
    '1': [], #process creation
    '3': [], #network connections
    '10': [] #process access
}



with open('./sysmon_sample.csv', 'r', newline='', encoding='utf-8') as f:  #Reads the CSV file and includes encoding for unexpected characters.
    next(f)  #skips the first line of metadata shown on a sysmon log
    log_reader = csv.DictReader(f)  #reads rows in a CSV file as a dictionary.
    log_header = log_reader.fieldnames #saves the names of each column


    for row in log_reader:  #filter rows by EventID
        event_id = row.get('Id')
        if event_id in filtered_data:
            filtered_data[event_id].append(row)




for event_id, rows in filtered_data.items(): #writes events to new files
    with open(output_files[event_id], 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=log_header)
        writer.writeheader()
        writer.writerows(rows)



