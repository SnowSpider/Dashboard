#!/usr/bin/env python

from Fail import *
import csv
import re 
import fileinput
import sys


"""
file_output = open("Output.txt","w")

file_output.write("Hello World\n") 
file_output.write("This is our new text file\n") 
file_output.write("and this is another line.\n") 
file_output.write("Why? Because we can.\n") 

file_output.close() 

print("This line will be printed.")

"""

# Identify ATX team members

def collectAgents(source,arr):
  with open(source) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
      arr.append(row[0])
      #print(row[0])

list_ATX = []
collectAgents('Source/Agents.csv', list_ATX)


# Create a list of Blackout class objects

list_fail = []
list_fail.append(Fail("Timestamp", "Scope", "Task Type", "Correspondence Link", "Sheet Link", "BPA Link", "Owner", "Failed by",  "Reason"))

# Read and parse Ind_cmp sheet

with open("Source/Ind_cmp.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('B')-65]
    scope = "Individual"
    link_mail = row[ord('K')-65]
    link_sheet = row[ord('L')-65]
    link_bpa = row[ord('M')-65]
    owner_proc = row[ord('N')-65]
    owner_1stProcAud = row[ord('T')-65]
    owner_2ndProcAud = row[ord('W')-65]
    owner_ing = row[ord('Q')-65]
    owner_1stIngAud = row[ord('Z')-65]
    owner_2ndIngAud = row[ord('Z')-65+3]
    reason_1stProcAud = row[ord('U')-65]
    reason_2ndProcAud = row[ord('X')-65]
    reason_1stIngAud = row[ord('Z')-65+1]
    reason_2ndIngAud = row[ord('Z')-65+4]


    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud,reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Ind_run sheet

with open("Source/Ind_run.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('B')-66]
    scope = "Individual"
    link_mail = row[ord('K')-66]
    link_sheet = row[ord('L')-66]
    link_bpa = row[ord('M')-66]
    owner_proc = row[ord('N')-66]
    owner_1stProcAud = row[ord('T')-66]
    owner_2ndProcAud = row[ord('W')-66]
    owner_ing = row[ord('Q')-66]
    owner_1stIngAud = row[ord('Z')-66]
    owner_2ndIngAud = row[ord('Z')-66+3]
    reason_1stProcAud = row[ord('U')-66]
    reason_2ndProcAud = row[ord('X')-66]
    reason_1stIngAud = row[ord('Z')-66+1]
    reason_2ndIngAud = row[ord('Z')-66+4]

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Rng_cmp sheet

with open("Source/Rng_cmp.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Range"
    link_mail = row[ord('N')-65]
    link_sheet = row[ord('P')-65]
    link_bpa = row[ord('O')-65]
    owner_proc = row[ord('Q')-65]
    owner_1stProcAud = row[ord('V')-65]
    owner_2ndProcAud = row[ord('Y')-65]
    owner_ing = row[ord('T')-65]
    owner_1stIngAud = row[ord('Z')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = row[ord('W')-65]
    reason_2ndProcAud = row[ord('X')-65]
    reason_1stIngAud = row[ord('Z')-65+1]
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")\

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Rng_run sheet

with open("Source/Rng_run.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Range"
    link_mail = row[ord('N')-65]
    link_sheet = row[ord('P')-65]
    link_bpa = row[ord('O')-65]
    owner_proc = row[ord('Q')-65]
    owner_1stProcAud = row[ord('V')-65]
    owner_2ndProcAud = row[ord('Y')-65]
    owner_ing = row[ord('T')-65]
    owner_1stIngAud = row[ord('Z')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = row[ord('W')-65]
    reason_2ndProcAud = row[ord('X')-65]
    reason_1stIngAud = row[ord('Z')-65+1]
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Ser_cmp sheet

with open("Source/Ser_cmp.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('B')-65]
    scope = "Series"
    link_mail = row[ord('M')-65]
    link_sheet = row[ord('N')-65]
    link_bpa = row[ord('O')-65]
    owner_proc = row[ord('P')-65]
    owner_1stProcAud = row[ord('Q')-65]
    owner_2ndProcAud = ""
    owner_ing = row[ord('U')-65]
    owner_1stIngAud = row[ord('S')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = ""
    reason_2ndProcAud = ""
    reason_1stIngAud = ""
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Ser_run sheet

with open("Source/Ser_run.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Series"
    link_mail = ""
    link_sheet = ""
    link_bpa = row[ord('O')-65]
    owner_proc = row[ord('J')-65]
    owner_1stProcAud = row[ord('L')-65]
    owner_2ndProcAud = ""
    owner_ing = row[ord('K')-65]
    owner_1stIngAud = ""
    owner_2ndIngAud = ""
    reason_1stProcAud = ""
    reason_2ndProcAud = ""
    reason_1stIngAud = ""
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Bat_cmp sheet

with open("Source/Bat_cmp.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Batch"
    link_mail = row[ord('L')-65]
    link_sheet = row[ord('M')-65]
    link_bpa = row[ord('N')-65]
    owner_proc = row[ord('O')-65]
    owner_1stProcAud = row[ord('P')-65]
    owner_2ndProcAud = row[ord('R')-65]
    owner_ing = row[ord('T')-65]
    owner_1stIngAud = row[ord('V')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = row[ord('Q')-65]
    reason_2ndProcAud = row[ord('S')-65]
    reason_1stIngAud = row[ord('W')-65]
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse Bat_run sheet

with open("Source/Bat_run.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Batch"
    link_mail = row[ord('L')-65]
    link_sheet = row[ord('M')-65]
    link_bpa = row[ord('N')-65]
    owner_proc = row[ord('O')-65]
    owner_1stProcAud = row[ord('P')-65]
    owner_2ndProcAud = row[ord('R')-65]
    owner_ing = row[ord('T')-65]
    owner_1stIngAud = row[ord('V')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = row[ord('Q')-65]
    reason_2ndProcAud = row[ord('S')-65]
    reason_1stIngAud = row[ord('W')-65]
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse IndMod_cmp sheet

with open("Source/IndMod_cmp.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Individual Modification"
    link_mail = row[ord('J')-65]
    link_sheet = row[ord('K')-65]
    link_bpa = row[ord('L')-65]
    owner_proc = row[ord('M')-65]
    owner_1stProcAud = row[ord('Q')-65]
    owner_2ndProcAud = ""
    owner_ing = row[ord('P')-65]
    owner_1stIngAud = row[ord('S')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = row[ord('R')-65]
    reason_2ndProcAud = ""
    reason_1stIngAud = row[ord('T')-65]
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))

# Read and parse IndMod_run sheet

with open("Source/IndMod_run.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter = ",")
  next(readCSV)
  for row in readCSV:
    timestamp = row[ord('A')-65]
    scope = "Individual Modification"
    link_mail = row[ord('J')-65]
    link_sheet = row[ord('K')-65]
    link_bpa = row[ord('L')-65]
    owner_proc = row[ord('M')-65]
    owner_1stProcAud = row[ord('Q')-65]
    owner_2ndProcAud = ""
    owner_ing = row[ord('P')-65]
    owner_1stIngAud = row[ord('S')-65]
    owner_2ndIngAud = ""
    reason_1stProcAud = row[ord('R')-65]
    reason_2ndProcAud = ""
    reason_1stIngAud = row[ord('T')-65]
    reason_2ndIngAud = ""

    link_mail = link_mail.replace("(", "")
    link_sheet = link_sheet.replace("(", "")
    link_bpa = link_bpa.replace("(", "")

    link_mail = link_mail.replace(")", "")
    link_sheet = link_sheet.replace(")", "")
    link_bpa = link_bpa.replace(")", "")

    link_mail = link_mail.replace("[Link]", "")
    link_sheet = link_sheet.replace("[Link]", "")
    link_bpa = link_bpa.replace("[Link]", "")

    link_mail = link_mail.replace(",", " ")
    link_sheet = link_sheet.replace(",", " ")
    link_bpa = link_bpa.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace(",", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(",", " ")
    reason_1stIngAud = reason_1stIngAud.replace(",", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(",", " ")

    reason_1stProcAud = reason_1stProcAud.replace("\n", " ")
    reason_2ndProcAud = reason_2ndProcAud.replace("\n", " ")
    reason_1stIngAud = reason_1stIngAud.replace("\n", " ")
    reason_2ndIngAud = reason_2ndIngAud.replace("\n", " ")
    
    reason_1stProcAud = reason_1stProcAud.replace(chr(34), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(34), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(34), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(34), " ")

    reason_1stProcAud = reason_1stProcAud.replace(chr(39), " ")
    reason_2ndProcAud = reason_2ndProcAud.replace(chr(39), " ")
    reason_1stIngAud = reason_1stIngAud.replace(chr(39), " ")
    reason_2ndIngAud = reason_2ndIngAud.replace(chr(39), " ")

    if reason_1stProcAud != "" and reason_1stProcAud != "null" and owner_proc in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Processing", link_mail, link_sheet, link_bpa, owner_proc, owner_1stProcAud, reason_1stProcAud))
    if reason_2ndProcAud != "" and reason_2ndProcAud != "null" and owner_1stProcAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Processing Audit", link_mail, link_sheet, link_bpa, owner_1stProcAud, owner_2ndProcAud, reason_2ndProcAud))
    if reason_1stIngAud != "" and reason_1stIngAud != "null" and owner_ing in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "Hades Ingestion", link_mail, link_sheet, link_bpa, owner_ing, owner_1stIngAud, reason_1stIngAud))
    if reason_2ndIngAud != "" and reason_2ndIngAud != "null" and owner_1stIngAud in list_ATX: 
      list_fail.append(Fail(timestamp, scope, "1st Ingestion Audit", link_mail, link_sheet, link_bpa, owner_1stIngAud, owner_2ndIngAud, reason_2ndIngAud))


"""
#file_NoBO = open("Source/NoBO.txt","r")
"""

print ("Total fail: "+str(len(list_fail)))

csvfile = open("Output/Report_error.csv","w")
d = ","
for fail in list_fail:
  line = fail.timestamp +d+ fail.scope +d+ fail.type_task +d+ fail.link_mail +d+ fail.link_sheet +d+ fail.link_bpa +d+ fail.owner +d+ fail.auditor +d+ fail.reason +"\n"
  csvfile.write(line)








