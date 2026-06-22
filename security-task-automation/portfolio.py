#!/usr/bin/env python
# coding: utf-8

# # Algorithm for file updates in Python
# 
# ## Project description
# The scenario for this project was as follows:
# A medical organization has limited access to patient files containing sensitive personal data. Access is only possible from approved IP addresses stored in a separate file.
# 
# There is also a list of IP addresses that need to be removed from the allowed list
# 
# This project taught me how to use file contents in Python, manipulate these contents, and overwrite files using data obtained during code execution.
# 
# ## Open the file that contains the allow list
# To open a file and subsequently use its contents most correctly and safely, you will need the following operators: 
# 1. `with` closes the file immediately after opening, so that further work with it can be performed correctly. 
# 2. `open(import_file,’r’)` prepares the file (first parameter) for further reading (`‘r’`), writing (`‘w’`), or appending (`‘a’`), depending on the value of the second argument. In this case, it is for reading (`‘r’`). 
# 3. Assigns the `file` a variable name (`as`).
# A colon `:` must be placed at the end of this line
# 
# ## Read the file contents
# 
# To read the file further, you need to use the function `.read()`  inside a `with` statement
# It converts the file contents into a string. 
# For more convenient use, this string can be saved in a new variable like `users_info` in the example
# 
# 

# In[1]:


# Assign 'import_file' variable to the name of the file

import_file = 'textfile.txt'

# Assing 'remove_list' to a list of IP addresses that are no longer allowed to access restricted information

remove_list = ["192.168.25.60", "192.168.168.144", "192.168.214.49","192.168.148.80"]

# First line of 'with' statement

with open(import_file,'r') as file:

    # Use '.read()' to read the imported file amd store it in avariable named 'users_info'

    users_info = file.read()
# Checking that the code is written correctly
print(f'Verify the file contents were read correctly \n\n{users_info}\n\n\n')


# ## Convert the string into a list
# It's often more convenient to use a list format for working with data. In this example, for further manipulation of IP addresses, it's necessary to convert the string into a list format so that you can easily search and delete the desired ones. This is necessary for working with, for example, a `for loops`. To convert a string to a list format, you need to use the function `.split()` . By default, splitting occurs on all whitespace characters (spaces, tabs, line breaks).In this example it is line breaks.
# 

# In[2]:


# Use '.split()' to convert 'uses_info' from string to list

users_info_list_lines = users_info.split()

# Disply 'users_info_list_lines'

print(f'Disply users_info_list_lines\n\n{users_info_list_lines}\n\n\n')



# ## Convert list of lines to list of lists
# 
# We have big amount of data we don't need. To extract only IP adresses we need to create list of lists where in every sublist IP adress wil be on the same place. 
# For this porpose we use
# 1. `for loop` - go through every element of the list
# 2. `range()` function - say to `for loop` how many times it shuold performe
# 3. `len()` function - give total number of elements in the list
# 4. `.split(',')` function - split every element of `users_info_list_lines` to sublist on `,`
# 5. `.append()` function - append every new subllist to the end of the main list
# 

# In[3]:


# Crating new empty list 'users_info_list_of_lists'

users_info_list_of_lists = []

# Using for loop to convert each element of 'users_info_list_lines' list to new list

for i in range(len(users_info_list_lines)):

    # For '.split()' use ',' like argument to spliting on ','

    sublist = users_info_list_lines[i].split(',')

    # Use '.append()' to add new 'sublist' to the main list

    users_info_list_of_lists.append(sublist)

# Display 'users_info_list_of_lists' after 'for loop'

print(f'Display users_info_list_of_lists after for loop\n\n{users_info_list_of_lists}\n\n\n')


# ## Extracting IP adress from sublists
# 
# Now we can work with every line like with separate list and extract only IP adresses:
# 1. `for loop` - go through every sublist of the list
# 2. `range(1, len(users_info_list_of_lists)`
#    - `range()` says to `for loop` how many times it shuold performe
#    - `1` says from wich element `for loop` will start - second one in our case, because in the first one only headers
#    - `len()` - give total number of elements in the list

# In[4]:


# Crating new empty list 'ip_adresses'
ip_adresses = []

# Using for loop to extract every sublist and take only IP adress
for i in range(1, len(users_info_list_of_lists)):

    # Take sublist number `i`
    sublist = users_info_list_of_lists[i]

    # Append second element of `sublist` to `ip_adress`
    ip_adresses.append(sublist[1])

# Display 'ip_adresses' list
print(f'Display ip_adresses list\n\n{ip_adresses}\n\n\n')




# ## Remove IP addresses that are on the remove list
# To remove IP addresses from the `ip_addresses`  using IP addresses from the `remove_list`, we need to:
# 1. Extract each IP address from the `ip_addresses` list using a `for loop`. 
# 2. Check if the IP address extracted from the  `ip_addresses` list is in the `remove_list` list using an `if statement` that includes the `in` comparison operator. 
# 3. If the IP address from the `ip_addresses` list is in the `remove_list` list, remove it using a `.remove()` function that takes the `element` variable as an argument. 
# 
# The output shows a comparison between the original list and the list  from which IP addresses matching the values in the list of IP addresses to be removed were removed.
# 

# In[5]:


# Display 'ip_adresses' list before removing of IP adresses
print(f'Display ip_adresses list before removing of IP adresses\n\n{ip_adresses}\n\n\n')

for element in ip_adresses:

    # Build conditional statement
    # If current element is in `remove_list`

    if element in remove_list:

        # then current element should be removed from `ip_adresses
        ip_adresses.remove(element)

# Display 'ip_adresses' list after removing of IP adresses
print(f'Display ip_adresses list after removing of IP adresses\n\n{ip_adresses}\n\n\n')


# ## Update the file with the revised list of IP addresses 
# To save changes to a file: 
# 1. Use a `.join()` to convert the list to a string. In this example `‘\n’.joint(ip_addresses)` is applied to the delimiter line break, and the list `ip_addresses`  is passed as an argument. 
# 2. Next, using the `with`, `open()`, argument `‘w’` and assigning a name (as described above), we enable write access to the file. 
# 3. Using the `.write()` function, which takes a variable containing the new string `ip_addresses` as a parameter, we write the updated information to the file.

# In[6]:


# Convert `ip_adresses` back to the string

ip_adresses = "\n".join(ip_adresses)

# Build `with` statement to rewrite the original file
with open(import_file, 'w') as file:

# Rewrite the file, replacing its content with `ip_adresses
    file.write(ip_adresses)


# Build `with` statement to check the new file

with open(import_file,'r') as file:

    # Use '.read()' to read the imported file and store it in avariable named 'alowed_ip'

    allowed_ip = file.read()
# Checking the new file
print(f'Verify the new file is correct \n\n{allowed_ip}')