#!/usr/bin/env python3
from src import Contact
from terminaltables import AsciiTable

def main():
    contactList = []
    c1 = Contact("FristName1","LastName1","Street1","509435","City1")
    contactList.append(c1)
    c2 = Contact("FristName2","LastName2","Street2","509435","City2")
    contactList.append(c2)
    table_data=[]
    for c in contactList:
        table_data.append(['First name', 'Last name', 'City', 'ZipCode', 'City'])
        table_data.append([c.fname,c.lname,c.street,c.zipcode,c.city])
    table = AsciiTable(table_data)
    print(table.table)
if __name__ =="__main__" : main()
