import os
import datetime


def get_table():
    raw_arp_table = str(input(os.system("arp -a > tmp.txt")))
    arp_file = open("tmp.txt", "w+")
    arp_file.write(raw_arp_table)
    print(arp_file)
    arp_file.close()

def organize_table():
    arp_file = open("tmp.txt", "r")
    print(arp_file.readline(10))
    #single_line = print(arp_file.readline(10))
    #print(arp_file.readline())
    #print(single_line)
    #type(single_line)
    arp_file.close()
    #for arp_line in arp_file:
    #if clean_arp_file[0] = "I":


  #  arp_file = print(clean_arp_file)
 #   arp_file.close()
    #print(clean_arp_file)
    #type(clean_arp_file)



#    arp_table_lines = raw_arp_table.split(" ")
 #   for lines in arp_table_lines:
        #print(file.readline())
        #print(arp_table_lines)
        #print(raw_arp_table)
  #      break



if __name__ == "__main__":
    try:
        get_table()
        #organize_table()
        print("Scan completed successfully.")
    except Exception as e:
        print(e)
