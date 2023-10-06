#Shows Day
print("Day 1")
#Accesses Text File
the_file = open("um-deliveries-day-1.txt")
#Loops Through Each Line In File
for line in the_file:
    #Strips Lines Of Empty Spaces
    line = line.rstrip()
    #Seperates Indexes
    words = line.split('|')
    #Sets Variables For Each Index
    melon = words[0]
    count = words[1]
    amount = words[2]
    #Prints Variables And Text
    print(f"Delivered {count} {melon}s for total of ${amount}")
#Exits Out Of File    
the_file.close()

#Shows Day
print("Day 2")
#Accesses Text File
the_file = open("um-deliveries-day-2.txt")
#Loops Through Each Line In File
for line in the_file:
    #Strips Lines Of Empty Spaces
    line = line.rstrip()
    #Seperates Indexes
    words = line.split('|')
    #Sets Variables For Each Index
    melon = words[0]
    count = words[1]
    amount = words[2]
    #Prints Variables And Text
    print(f"Delivered {count} {melon}s for total of ${amount}")
#Exits Out Of File
the_file.close()

#Shows Day
print("Day 3")
#Accesses Text File
the_file = open("um-deliveries-day-3.txt")
#Loops Through Each Line In File
for line in the_file:
    #Strips Lines Of Empty Spaces
    line = line.rstrip()
    #Seperates Indexes
    words = line.split('|')
    #Sets Variables For Each Index
    melon = words[0]
    count = words[1]
    amount = words[2]
    #Prints Variables And Text
    print(f"Delivered {count} {melon}s for total of ${amount}")
#Exits Out Of File    
the_file.close()
