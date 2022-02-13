import os
import datetime

raw_arp_table = []
def main():
    global raw_arp_table
    raw_arp_table = str(input(os.system("arp -a")))
    arp_table_lines = raw_arp_table.split(" ")
    for lines in arp_table_lines.
        print(lines)
    #print(arp_table_lines)
    #print(raw_arp_table)



if __name__ == "__main__":
    try:
        main()
        print("Scan completed successfully.")
    except Exception as e:
        print(e)
