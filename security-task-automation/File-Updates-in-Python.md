# Algorithm for File Updates in Python

## Project Description
In this project scenario, a medical organization restricts access to patient files containing sensitive personal data. Access is only permitted from authorized IP addresses stored in a designated allow-list file (`textfile.txt`). 

A separate list (`remove_list`) contains IP addresses of employees who have changed roles or left the organization. These addresses must be systematically identified and removed from the active allow-list.

This project demonstrates how to securely open, read, parse, manipulate, and overwrite files using basic Python structures, including loops, conditional statements, and string/list methods.

---
---

## Step-by-Step Implementation

### 1. Open the File Containing the Allow-List
To open and manage the file safely, I utilized Python's `with` statement alongside the `open()` function. 
* The `with` statement ensures the file is automatically closed immediately after the block executes, preventing memory leaks or file corruption.
* The `open(import_file, 'r')` function prepares the target file for reading (`'r'`).
* The `as file` clause assigns the file object to a variable name for reference.

```python
# Assign 'import_file' variable to the name of the file
import_file = 'textfile.txt'

# Assign 'remove_list' to a list of IP addresses that are no longer allowed access
remove_list = ["192.168.25.60", "192.168.168.144", "192.168.214.49", "192.168.148.80"]

# First line of 'with' statement for reading
with open(import_file, 'r') as file:
    # Use '.read()' to read the imported file and store it in a variable named 'users_info'
    users_info = file.read()

# Verify the file contents were read correctly
print(users_info)
```
Output of Input File (`users_info`):
```
username,ip_address,time,date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
... [truncated for readability] ...
jsoto,192.168.25.60,5:09:21,2022-05-09
```
---

### 2. Convert the String into a List of Lines
Working with data in a raw string format is inefficient for line-by-line validation. To manipulate specific elements, I converted the string into a list format using the `.split()` method. By default, `.split()` separates strings by whitespace, which effectively splits our text by line breaks (`\n`).

```python
# Use '.split()' to convert 'users_info' from string to a list of lines
users_info_list_lines = users_info.split()

# Display the converted list of lines
print(users_info_list_lines)
```
Ouput of `users_info_list_lines`:
```
['username,ip_address,time,date', 'tshah,192.168.92.147,15:26:08,2022-05-10', ... [truncated for readability] ... 'eraab,192.168.24.12,11:29:27,2022-05-11', 'jsoto,192.168.25.60,5:09:21,2022-05-09']
```
---

### 3. Parse Lines into Sublists (List of Lists)

The raw data contains parameters we don't currently need (`usernames`, `timestamps`, `dates`). To isolate and inspect only the IP addresses, I transformed the flat list of strings into a structured list of lists using a `for` loop, `range()`, and `len()`.
- `for loop` - go through every element of the list
- `range()` function - says to `for loop` how many times it shuold performe
- `len()` function - give total number of elements in the list
- `.split(',')` function - split every element of `users_info_list_lines` to sublist on `,`
- `.append()` function - append every new subllist to the end of the main list
```python
# Create an empty list to hold the parsed structures
users_info_list_of_lists = []

# Use a for loop to iterate through each row of the log data
for i in range(len(users_info_list_lines)):
    # Split each line by the comma delimiter to create a sublist
    sublist = users_info_list_lines[i].split(',')

    # Append the new sublist to the main repository list
    users_info_list_of_lists.append(sublist)

# Display the multi-dimensional list structure
print(users_info_list_of_lists)
```

Ouput of `users_info_list_of_lists`:
```
[['username', 'ip_address', 'time', 'date'], ['tshah', '192.168.92.147', '15:26:08', '2022-05-10'], ... [truncated for readability] ... ['eraab', '192.168.24.12', '11:29:27', '2022-05-11'], ['jsoto', '192.168.25.60', '5:09:21', '2022-05-09']]
```
---

### 4. Extract IP Addresses from Sublists

With the log rows split into indexed arrays, the IP addresses are now positioned consistently at index 1 inside every sublist. I used another `for loop` starting from index 1 (skipping index 0 because it contains CSV column headers) to extract the IPs.

```python
# Create an empty list to store isolated IP addresses
ip_addresses = []

# Iterate through sublists, skipping the header line (index 0)
for i in range(1, len(users_info_list_of_lists)):
    sublist = users_info_list_of_lists[i]

    # Append the second element (index 1 - the IP address) to our target list
    ip_addresses.append(sublist[1])

# Display the isolated IP addresses list
print(ip_addresses)
```
Output of `ip_adresses`
```
['192.168.92.147', '192.168.98.221', ... [truncated for readability] ... '192.168.24.12', '192.168.25.60']
```
---

### 5. Remove Unauthorized IP Addresses

To remove addresses found in the `remove_list` from the active `ip_addresses` allow-list, I built a conditional block:

- An outer `for loop` evaluates each element inside the `ip_addresses` list.
- An inner `if` statement applies the `in` comparison operator to check if that specific IP exists inside the `remove_list`.
- If a match is found, the `.remove(element)` method deletes it from the active list.

```python
# Evaluate active IP addresses against the revocation list
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# Display the revised allow-list after filtering
print(ip_addresses)
```

Output of `ip_addresses` **before** removing

```
['192.168.92.147', '192.168.98.221', '192.168.110.131', '192.168.168.144', '192.168.170.243', '192.168.238.42', '192.168.52.90', '192.168.58.217', '192.168.214.49', '192.168.247.153', '192.168.197.247', '192.168.46.207', '192.168.96.244', '192.168.131.147', '192.168.60.111', '192.168.148.80', '192.168.4.157', '192.168.210.228', '192.168.24.12', '192.168.25.60']
```

Output of `ip_addresses` **after** removing

```
['192.168.92.147', '192.168.98.221', '192.168.110.131', '192.168.170.243', '192.168.238.42', '192.168.52.90', '192.168.58.217', '192.168.247.153', '192.168.197.247', '192.168.46.207', '192.168.96.244', '192.168.131.147', '192.168.60.111', '192.168.4.157', '192.168.210.228', '192.168.24.12']
```

---

### 6. Update the File with the Revised Allow-List

Finally, the modified list needs to be written back to the file.

- First, the list is converted back into a string using the `"\n".join(ip_addresses)` method, placing each IP address on a new line.

- Then, a `with` statement opens the file using the write mode (`'w'`), allowing the script to completely overwrite the old log with the secure, updated data.

```python
# Convert the list of IPs back into a  string
ip_addresses_str = "\n".join(ip_addresses)

# Open the original file in write mode ('w') to replace obsolete records
with open(import_file, 'w') as file:
    # Overwrite the file content
    file.write(ip_addresses_str)
```

---
---
## Key Takeaways & SOC Relevance

- Automated Identity & Access Management (IAM): Manually checking logs or firewall lists of hundreds of employees introduces massive room for human error. This script demonstrates how Python can be leveraged to parse logs and automate access token audits.

- Core Scripting Competency: Successfully practiced essential automation concepts: managing file input/output (I/O) handles, complex string parsing, array-indexing logic, and safe write operations to production logs.

