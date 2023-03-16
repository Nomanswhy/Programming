# creating and opening a file for a purpose of re-writing
file_out = open("file.txt", "w")
file_out.write("This is the first line.\n")
file_out.write("This is the second line.\n")
file_out.close()

# Create and open a file for the purpose of appending (adding to existing content)
file_out_a = open("file_append.txt", "a")
file_out_a.write("This is a newley added (appended) line. \n")
file_out_a.write("This is a newley added (appended) line. \n")
file_out_a.close()

# Open an existing file for the purpose of reading
file_in = open("file.txt", "r")
print(file_in.read())
file_in.close()

phonebook_file_in = open("phonebook.txt", "r")
phonebook_dictionary = {}

for line in phonebook_file_in:
    name, phone = line.split(" ")
    phonebook_dictionary[name] = phone.rstrip()

phonebook_file_in.close()
print(phonebook_dictionary)

# Get a phone number

print("\n", phonebook_dictionary["Holly"])

for name, phone in phonebook_dictionary.items():
    print("\nName > ", name, "\nPhone > ", phone)
