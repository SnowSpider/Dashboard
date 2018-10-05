#!/usr/bin/env python

from Stack import *
from WeeklyRecord import *

import csv
import re 
import fileinput
import sys

from datetime import datetime
from datetime import timedelta


def getTypes(): 
  arr = []
  with open('Source/Index.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    next(csvreader)
    next(csvreader)
    for row in csvreader:
      arr.append(row[0])
  return arr

arr_type_task = getTypes()

""" ............................................................................. """

def col_to_num(col_str):
  # Convert base26 column string to number.
  exponent = 0
  col_num = 0
  for char in reversed(col_str):
    col_num += (ord(char) - ord('A') + 1) * (26 ** exponent)
    exponent += 1
  col_num -= 1 # to be or not to be ...
  return col_num

""" ............................................................................. """

def range_to_arr(file_name, data_range): #incomplete!
  # both arguments should be provided in string
  # 'Source/Index.csv'
  # 'A1:B2'
  # First, we need to determine the height and width of the output array.
  pair = data_range.split(':')
  col_head = pair[0]
  return 0

""" ............................................................................. """

def cn(type_BO,type_task):
  with open('Source/Index.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    next(csvreader)
    columnNumber = 0
    i = 0
    row = next(csvreader)
    for c in row:
      if c == type_task:
        columnNumber = i
      i += 1
    for row in csvreader:
      if row[0] == type_BO:
        return col_to_num(row[columnNumber])

#print(str(cn('Ind_cmp','st_proc'))+'foo')
    
#print('format_Ser_run.ing = ' + str(format_Ser_run.ing))

# Identify ATX team members

def collectAgents(source,arr):
  with open(source) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
      arr.append(row[0])
      #print(row[0])

arr_agent = []
collectAgents('Source/Agents.csv', arr_agent)





""" ............................................................................. """

# 1. Initialize the WeeklyRecord array

date_start = datetime(2017, 12, 1)
date_end = datetime(2018, 12, 1)

arr_WR = []
arr_WR.append(WeeklyRecord())

date_intermediate = date_start

counter = 1
num_month = 1


while date_intermediate < date_end:
  arr_WR.append(WeeklyRecord())
  arr_WR[counter].week = date_intermediate
  #print(arr_WR[counter].week)
  counter += 1
  date_intermediate = datetime(2018, num_month, 1)
  num_month += 1
  

arr_WR[1].week = date_start

arr_WR[0].week = 'week'
arr_WR[0].proc_Ind_cmp = 'proc_Ind_cmp'
arr_WR[0].proc_Ind_run = 'proc_Ind_run'
arr_WR[0].proc_Rng_cmp = 'proc_Rng_cmp'
arr_WR[0].proc_Rng_run = 'proc_Rng_run'
arr_WR[0].proc_Ser_cmp = 'proc_Ser_cmp'
arr_WR[0].proc_Ser_run = 'proc_Ser_run'
arr_WR[0].proc_Bat_cmp = 'proc_Bat_cmp'
arr_WR[0].proc_Bat_run = 'proc_Bat_run'
arr_WR[0].proc_IndMod_cmp = 'proc_IndMod_cmp'
arr_WR[0].proc_IndMod_run = 'proc_IndMod_run'
arr_WR[0].proc_NoBO = 'proc_NoBO'
arr_WR[0].proc_Parser_cmp = 'proc_Parser_cmp'
arr_WR[0].proc_Parser_run = 'proc_Parser_run'

arr_WR[0].proc_Ind_cmp_bad = 'proc_Ind_cmp_bad'
arr_WR[0].proc_Ind_run_bad = 'proc_Ind_run_bad'
arr_WR[0].proc_Rng_cmp_bad = 'proc_Rng_cmp_bad'
arr_WR[0].proc_Rng_run_bad = 'proc_Rng_run_bad'
arr_WR[0].proc_Ser_cmp_bad = 'proc_Ser_cmp_bad'
arr_WR[0].proc_Ser_run_bad = 'proc_Ser_run_bad'
arr_WR[0].proc_Bat_cmp_bad = 'proc_Bat_cmp_bad'
arr_WR[0].proc_Bat_run_bad = 'proc_Bat_run_bad'
arr_WR[0].proc_IndMod_cmp_bad = 'proc_IndMod_cmp_bad'
arr_WR[0].proc_IndMod_run_bad = 'proc_IndMod_run_bad'
arr_WR[0].proc_NoBO_bad = 'proc_NoBO_bad'
arr_WR[0].proc_Parser_cmp_bad = 'proc_Parser_cmp_bad'
arr_WR[0].proc_Parser_run_bad = 'proc_Parser_run_bad'

arr_WR[0].sum_proc = 'sum_proc'
arr_WR[0].sum_proc_bad = 'sum_proc_bad'
arr_WR[0].acc_proc = 'acc_proc'

arr_WR[0].pa1_Ind_cmp = 'pa1_Ind_cmp'
arr_WR[0].pa1_Ind_run = 'pa1_Ind_run'
arr_WR[0].pa1_Rng_cmp = 'pa1_Rng_cmp'
arr_WR[0].pa1_Rng_run = 'pa1_Rng_run'
arr_WR[0].pa1_Ser_cmp = 'pa1_Ser_cmp'
arr_WR[0].pa1_Ser_run = 'pa1_Ser_run'
arr_WR[0].pa1_Bat_cmp = 'pa1_Bat_cmp'
arr_WR[0].pa1_Bat_run = 'pa1_Bat_run'
arr_WR[0].pa1_IndMod_cmp = 'pa1_IndMod_cmp'
arr_WR[0].pa1_IndMod_run = 'pa1_IndMod_run'
arr_WR[0].pa1_NoBO = 'pa1_NoBO'
arr_WR[0].pa1_Parser_cmp = 'pa1_Parser_cmp'
arr_WR[0].pa1_Parser_run = 'pa1_Parser_run'

arr_WR[0].pa1_Ind_cmp_bad = 'pa1_Ind_cmp_bad'
arr_WR[0].pa1_Ind_run_bad = 'pa1_Ind_run_bad'
arr_WR[0].pa1_Rng_cmp_bad = 'pa1_Rng_cmp_bad'
arr_WR[0].pa1_Rng_run_bad = 'pa1_Rng_run_bad'
arr_WR[0].pa1_Ser_cmp_bad = 'pa1_Ser_cmp_bad'
arr_WR[0].pa1_Ser_run_bad = 'pa1_Ser_run_bad'
arr_WR[0].pa1_Bat_cmp_bad = 'pa1_Bat_cmp_bad'
arr_WR[0].pa1_Bat_run_bad = 'pa1_Bat_run_bad'
arr_WR[0].pa1_IndMod_cmp_bad = 'pa1_IndMod_cmp_bad'
arr_WR[0].pa1_IndMod_run_bad = 'pa1_IndMod_run_bad'

arr_WR[0].sum_pa1 = 'sum_pa1'
arr_WR[0].sum_pa1_bad = 'sum_pa1_bad'
arr_WR[0].acc_pa1 = 'acc_pa1'

arr_WR[0].pa2_Ind_cmp = 'pa2_Ind_cmp'
arr_WR[0].pa2_Ind_run = 'pa2_Ind_run'
arr_WR[0].pa2_Rng_cmp = 'pa2_Rng_cmp'
arr_WR[0].pa2_Rng_run = 'pa2_Rng_run'
arr_WR[0].pa2_Bat_cmp = 'pa2_Bat_cmp'
arr_WR[0].pa2_Bat_run = 'pa2_Bat_run'

arr_WR[0].sum_pa2 = 'sum_pa2'

arr_WR[0].ing_Ind_cmp = 'ing_Ind_cmp'
arr_WR[0].ing_Ind_run = 'ing_Ind_run'
arr_WR[0].ing_Rng_cmp = 'ing_Rng_cmp'
arr_WR[0].ing_Rng_run = 'ing_Rng_run'
arr_WR[0].ing_Ser_cmp = 'ing_Ser_cmp'
arr_WR[0].ing_Ser_run = 'ing_Ser_run'
arr_WR[0].ing_Bat_cmp = 'ing_Bat_cmp'
arr_WR[0].ing_Bat_run = 'ing_Bat_run'
arr_WR[0].ing_IndMod_cmp = 'ing_IndMod_cmp'
arr_WR[0].ing_IndMod_run = 'ing_IndMod_run'
arr_WR[0].ing_Parser_cmp = 'ing_Parser_cmp'
arr_WR[0].ing_Parser_run = 'ing_Parser_run'
arr_WR[0].ing_Parser_ing = 'ing_Parser_ing'

arr_WR[0].ing_Ind_cmp_bad = 'ing_Ind_cmp_bad'
arr_WR[0].ing_Ind_run_bad = 'ing_Ind_run_bad'
arr_WR[0].ing_Rng_cmp_bad = 'ing_Rng_cmp_bad'
arr_WR[0].ing_Rng_run_bad = 'ing_Rng_run_bad'
arr_WR[0].ing_Ser_cmp_bad = 'ing_Ser_cmp_bad'
arr_WR[0].ing_Ser_run_bad = 'ing_Ser_run_bad'
arr_WR[0].ing_Bat_cmp_bad = 'ing_Bat_cmp_bad'
arr_WR[0].ing_Bat_run_bad = 'ing_Bat_run_bad'
arr_WR[0].ing_IndMod_cmp_bad = 'ing_IndMod_cmp_bad'
arr_WR[0].ing_IndMod_run_bad = 'ing_IndMod_run_bad'
arr_WR[0].ing_Parser_cmp_bad = 'ing_Parser_cmp_bad'
arr_WR[0].ing_Parser_run_bad = 'ing_Parser_run_bad'
arr_WR[0].ing_Parser_ing_bad = 'ing_Parser_ing_bad'

arr_WR[0].sum_ing = 'sum_ing'
arr_WR[0].sum_ing_bad = 'sum_ing_bad'
arr_WR[0].acc_ing = 'acc_ing'

arr_WR[0].ia1_Ind_cmp = 'ia1_Ind_cmp'
arr_WR[0].ia1_Ind_run = 'ia1_Ind_run'
arr_WR[0].ia1_Rng_cmp = 'ia1_Rng_cmp'
arr_WR[0].ia1_Rng_run = 'ia1_Rng_run'
arr_WR[0].ia1_Ser_cmp = 'ia1_Ser_cmp'
arr_WR[0].ia1_Ser_run = 'ia1_Ser_run'
arr_WR[0].ia1_Bat_cmp = 'ia1_Bat_cmp'
arr_WR[0].ia1_Bat_run = 'ia1_Bat_run'
arr_WR[0].ia1_IndMod_cmp = 'ia1_IndMod_cmp'
arr_WR[0].ia1_IndMod_run = 'ia1_IndMod_run'
arr_WR[0].ia1_Parser_cmp = 'ia1_Parser_cmp'
arr_WR[0].ia1_Parser_run = 'ia1_Parser_run'
arr_WR[0].ia1_Parser_ing = 'ia1_Parser_ing'

arr_WR[0].ia1_Ind_cmp_bad = 'ia1_Ind_cmp_bad'
arr_WR[0].ia1_Ind_run_bad = 'ia1_Ind_run_bad'
arr_WR[0].ia1_Parser_ing_bad = 'ia1_Parser_ing_bad'

arr_WR[0].sum_ia1 = 'sum_ia1'
arr_WR[0].sum_ia1_bad = 'sum_ia1_bad'
arr_WR[0].acc_ia1 = 'acc_ia1'

arr_WR[0].ia2_Ind_cmp = 'ia2_Ind_cmp'
arr_WR[0].ia2_Ind_run = 'ia2_Ind_run'
arr_WR[0].ia2_Parser_ing = 'ia2_Parser_ing'

arr_WR[0].sum_ia2 = 'sum_ia2'

arr_WR[0].aps_Stack_cmp = 'aps_Stack_cmp'
arr_WR[0].aps_Stack_run = 'aps_Stack_run'

arr_WR[0].sum_aps = 'sum_aps'

arr_WR[0].sum_mail = 'sum_mail'

arr_WR[0].sum_BO = 'sum_BO'

arr_WR[0].sum_task = 'sum_task'

arr_WR[0].sum_task_bad = 'sum_task_bad'

arr_WR[0].acc_overall = 'acc_overall'

""" ............................................................................. """

# 2. Read Source sheets and generate Stack objects

"""
print('str(ord('A')-65) = ' + str(ord('A')-65))
print('str(ord('B')-65) = ' + str(ord('B')-65))
print('str(ord('C')-65) = ' + str(ord('C')-65))
print('str(ord('Z')-65) = ' + str(ord('Z')-65))
print('str(col_to_num('"AA"')) = ' + str(col_to_num('AA')))
print('str(col_to_num('"AB"')) = ' + str(col_to_num('AB')))
print('str(col_to_num('"AC"')) = ' + str(col_to_num('AC')))
"""

#print(' format_Ind_cmp.proc = ' + str(format_Ind_cmp.proc))
#print(' format_Ind_cmp.proc = ' + str(ord(format_Ind_cmp.proc)-65))



def t(s):
  return datetime.strptime(s,'%Y-%m-%d %H:%M:%S.%f') # do not change this

# 3. Read source sheets and create arrays of Stack objects

def arr_Stack(source):
  arr_Stack = []
  with open('Source/'+source+'.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
      s = Stack()
      s.scope = source
      
      # column wrapping issue resolved.
      # Optimize using:
      # getattr(object, attrname)
      # setattr(object, attrname, value)
      
      # https://stackoverflow.com/questions/2612610/how-to-access-object-attribute-given-string-corresponding-to-name-of-that-attrib
      # https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python
      
      if cn(source, 'st_proc') == -1:
        s.st_proc = ''
      else:
        s.st_proc = row[cn(source,'st_proc')]
      
      if cn(source, 'proc') == -1:
        s.proc = ''
      else:
        s.proc = row[cn(source,'proc')]
      
      if cn(source, 'st_pa1') == -1:
        s.st_pa1 = ''
      else:
        s.st_pa1 = row[cn(source,'st_pa1')]
      
      if cn(source, 'pa1') == -1:
        s.pa1 = ''
      else:
        s.pa1 = row[cn(source,'pa1')]
      
      if cn(source, 'fd_proc') == -1:
        s.fd_proc = ''
      else:
        s.fd_proc = row[cn(source,'fd_proc')]
        
      if cn(source, 'st_pa2') == -1:
        s.st_pa2 = ''
      else:
        s.st_pa2 = row[cn(source,'st_pa2')]
      
      if cn(source, 'pa2') == -1:
        s.pa2 = ''
      else:
        s.pa2 = row[cn(source,'pa2')]
      
      if cn(source, 'fd_pa1') == -1:
        s.fd_pa1 = ''
      else:
        s.fd_pa1 = row[cn(source,'fd_pa1')]
      
      if cn(source, 'st_ing') == -1:
        s.st_ing = ''
      else:
        s.st_ing = row[cn(source,'st_ing')]
        
      if cn(source, 'ing') == -1:
        s.ing = ''
      else:
        s.ing = row[cn(source,'ing')]
        
      if cn(source, 'st_ia1') == -1:
        s.st_ia1 = ''
      else:
        s.st_ia1 = row[cn(source,'st_ia1')]
        
      if cn(source, 'ia1') == -1:
        s.ia1 = ''
      else:
        s.ia1 = row[cn(source,'ia1')]  
        
      if cn(source, 'fd_ing') == -1:
        s.fd_ing = ''
      else:
        s.fd_ing = row[cn(source,'fd_ing')]  
      
      if cn(source, 'st_ia2') == -1:
        s.st_ia2 = ''
      else:
        s.st_ia2 = row[cn(source,'st_ia2')]  
        
      if cn(source, 'ia2') == -1:
        s.ia2 = ''
      else:
        s.ia2 = row[cn(source,'ia2')]  
        
      if cn(source, 'fd_ia1') == -1:
        s.fd_ia1 = ''
      else:
        s.fd_ia1 = row[cn(source,'fd_ia1')]  
        
      if cn(source, 'title') == -1:
        s.title = ''
      else:
        s.title = row[cn(source,'title')]  
      
      if cn(source, 'bpa') == -1:
        s.bpa = ''
      else:
        s.bpa = row[cn(source,'bpa')]  
        
      arr_Stack.append(s)
  return arr_Stack

Ind_cmp = arr_Stack('Ind_cmp')
Ind_run = arr_Stack('Ind_run')
Rng_cmp = arr_Stack('Rng_cmp')
Rng_run = arr_Stack('Rng_run')
Ser_cmp = arr_Stack('Ser_cmp')
Ser_run = arr_Stack('Ser_run')
Bat_cmp = arr_Stack('Bat_cmp')
Bat_run = arr_Stack('Bat_run')
IndMod_cmp = arr_Stack('IndMod_cmp')
IndMod_run = arr_Stack('IndMod_run')
NoBO = arr_Stack('NoBO')
Parser_cmp = arr_Stack('Parser_cmp')
Parser_run = arr_Stack('Parser_run')
Stack_cmp = arr_Stack('Stack_cmp')
Stack_run = arr_Stack('Stack_run')
Parser_ing = arr_Stack('Parser_ing')

# Sort them
# unused... nvm

def partition(arr,low,high):
  i = ( low-1 )         # index of smaller element
  pivot = arr[high]     # pivot
  for j in range(low , high):
    # If current element is smaller than or
    # equal to pivot
    if   arr[j] <= pivot:        
      # increment index of smaller element
      i = i+1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
  if low < high:
 
    # pi is partitioning index, arr[p] is now
    # at right place
    pi = partition(arr,low,high)
 
    # Separately sort elements before
    # partition and after partition
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)


def dupe(arr, elem): # check if elem has multiple clones in arr
  counter = 0
  for e in arr:
    if e == elem:
      counter += 1
  if counter >= 2:
    return 1
  else:
    return 0
  


# remove duplicate elements 
# **** this

def Remove(duplicate): 
  final_list = [] 
  for num in duplicate: 
    if num not in final_list: 
      final_list.append(num) 
  return final_list  



# ok Rng and Ser need to be cleaned up

def unique_proc(arr):
  arr_final = []
  dupe = 0
  for s in arr: 
    if len(arr_final)>0:
      for t in arr_final: 
        if t.st_proc == s.st_proc:
          dupe = 1
    if dupe == 0:
      arr_final.append(s)
    dupe = 0
  return arr_final

def unique_ing(arr):
  arr_final = []
  dupe = 0
  for s in arr: 
    if len(arr_final)>0:
      for t in arr_final: 
        if t.st_ing == s.st_ing:
          dupe = 1
    if dupe == 0:
      arr_final.append(s)
    dupe = 0
  return arr_final

Rng_cmp_proc = unique_proc(Rng_cmp) # done
Rng_cmp_ing = unique_ing(Rng_cmp) # done

Rng_run_proc = unique_proc(Rng_run) # done
Rng_run_ing = unique_ing(Rng_run) # done

Ser_cmp_proc = unique_proc(Ser_cmp) # done
Ser_run_proc = unique_proc(Ser_run) # done

# failures should be backtracked. (NOT DONE)

# 4. Create WeeklyRecord objects

# Pie, Blackout Scope

total_Ind = 0
total_Rng = 0
total_Ser = 0
total_Bat = 0
total_Parser = 0
total_IndMod = 0
total_NoBO = 0

# Pie, Task Type

total_proc = 0
total_pa1 = 0
total_pa2 = 0
total_ing = 0
total_ia1 = 0
total_ia2 = 0
total_aps = 0

for i in xrange(1,len(arr_WR)-2):
  
  for s in Ser_cmp_proc: # Ser_cmp_proc
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Ser_cmp += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Ser_cmp_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Ser_cmp += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Ser_cmp += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Ser_cmp += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Ser_cmp += 1
  
  for s in Ser_run_proc: # Ser_run_proc
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Ser_run += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Ser_run_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Ser_run += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Ser_run += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Ser_run += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Ser_run += 1
  
  for s in Rng_cmp_proc: # Rng_cmp_proc
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Rng_cmp += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Rng_cmp_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Rng_cmp += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_Rng_cmp_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Rng_cmp += 1
  
  for s in Rng_cmp_ing: # Rng_cmp_ing
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Rng_cmp += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Rng_cmp_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Rng_cmp += 1
  
  for s in Rng_run_proc: # Rng_run_proc
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Rng_run += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Rng_run_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Rng_run += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_Rng_run_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Rng_run += 1
    
  for s in Rng_run_ing: # Rng_run_ing
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Rng_run += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Rng_run_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Rng_run += 1
  
  for s in Ind_cmp: # Ind_cmp
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Ind_cmp += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Ind_cmp_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Ind_cmp += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_Ind_cmp_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Ind_cmp += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Ind_cmp += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Ind_cmp_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Ind_cmp += 1
        fd = s.fd_ia1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ia1_Ind_cmp_bad += 1
    if s.st_ia2 != '':
      if t(s.st_ia2) >= arr_WR[i].week and t(s.st_ia2) < arr_WR[i+1].week and s.ia2 in arr_agent:
        arr_WR[i].ia2_Ind_cmp += 1
  
  for s in Ind_run: # Ind_run
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Ind_run += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Ind_run_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Ind_run += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_Ind_run_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Ind_run += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Ind_run += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Ind_run_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Ind_run += 1
        fd = s.fd_ia1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ia1_Ind_run_bad += 1
    if s.st_ia2 != '':
      if t(s.st_ia2) >= arr_WR[i].week and t(s.st_ia2) < arr_WR[i+1].week and s.ia2 in arr_agent:
        arr_WR[i].ia2_Ind_run += 1
  
  for s in Bat_cmp: # Bat_cmp
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Bat_cmp += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Bat_cmp_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Bat_cmp += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_Bat_cmp_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Bat_cmp += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Bat_cmp += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Bat_cmp_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Bat_cmp += 1
  
  for s in Bat_run: # Bat_run
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Bat_run += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Bat_run_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Bat_run += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_Bat_run_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_Bat_run += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Bat_run += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Bat_run_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Bat_run += 1
  
  for s in IndMod_cmp: # IndMod_cmp
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_IndMod_cmp += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_IndMod_cmp_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_IndMod_cmp += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_IndMod_cmp_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_IndMod_cmp += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_IndMod_cmp += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_IndMod_cmp_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_IndMod_cmp += 1
  
  for s in IndMod_run: #IndMod_run
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_IndMod_run += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_IndMod_run_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_IndMod_run += 1
        fd = s.fd_pa1 # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].pa1_IndMod_run_bad += 1
    if s.st_pa2 != '':
      if t(s.st_pa2) >= arr_WR[i].week and t(s.st_pa2) < arr_WR[i+1].week and s.pa2 in arr_agent:
        arr_WR[i].pa2_IndMod_run += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_IndMod_run += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_IndMod_run_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_IndMod_run += 1
  
  for s in NoBO: # NoBO
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_NoBO += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_NoBO += 1
  
  for s in Stack_cmp: # Stack_cmp
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].aps_Stack_cmp += 1

  for s in Stack_run: # Stack_run
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].aps_Stack_run += 1
  
  # Parser stuff
  
  for s in Parser_cmp: # Parser_cmp
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Parser_cmp += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Parser_cmp_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Parser_cmp += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Parser_cmp += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Parser_cmp_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Parser_cmp += 1
    
  for s in Parser_run: # Parser_run
    if s.st_proc != '':
      if t(s.st_proc) >= arr_WR[i].week and t(s.st_proc) < arr_WR[i+1].week and s.proc in arr_agent:
        arr_WR[i].proc_Parser_run += 1
        fd = s.fd_proc # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].proc_Parser_run_bad += 1
    if s.st_pa1 != '':
      if t(s.st_pa1) >= arr_WR[i].week and t(s.st_pa1) < arr_WR[i+1].week and s.pa1 in arr_agent:
        arr_WR[i].pa1_Parser_run += 1
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing in arr_agent:
        arr_WR[i].ing_Parser_run += 1
        fd = s.fd_ing # check failure detail
        if fd != '' and fd != 'null' and fd != '0' and fd != chr(39):
          arr_WR[i].ing_Parser_run_bad += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 in arr_agent:
        arr_WR[i].ia1_Parser_run += 1
  
  # Parser_ing special stuff (done, but failure details are omitted)
  
  for s in Parser_ing: # Parser_ing
    if s.st_ing != '':
      if t(s.st_ing) >= arr_WR[i].week and t(s.st_ing) < arr_WR[i+1].week and s.ing + '@google.com' in arr_agent:
        arr_WR[i].ing_Parser_ing += 1
    if s.st_ia1 != '':
      if t(s.st_ia1) >= arr_WR[i].week and t(s.st_ia1) < arr_WR[i+1].week and s.ia1 + '@google.com' in arr_agent:
        arr_WR[i].ia1_Parser_ing += 1
    if s.st_ia2 != '':
      if t(s.st_ia2) >= arr_WR[i].week and t(s.st_ia2) < arr_WR[i+1].week and s.ia2 + '@google.com' in arr_agent:
        arr_WR[i].ia2_Parser_ing += 1
  
  
  # sum figures (done)
  
  arr_WR[i].sum_proc = arr_WR[i].proc_Ind_cmp + arr_WR[i].proc_Ind_run + arr_WR[i].proc_Rng_cmp + arr_WR[i].proc_Rng_run + arr_WR[i].proc_Ser_cmp + arr_WR[i].proc_Ser_run + arr_WR[i].proc_Bat_cmp + arr_WR[i].proc_Bat_run + arr_WR[i].proc_IndMod_cmp + arr_WR[i].proc_IndMod_run + arr_WR[i].proc_NoBO + arr_WR[i].proc_Parser_cmp + arr_WR[i].proc_Parser_run
  arr_WR[i].sum_proc_bad = arr_WR[i].proc_Ind_cmp_bad + arr_WR[i].proc_Ind_run_bad + arr_WR[i].proc_Rng_cmp_bad + arr_WR[i].proc_Rng_run_bad + arr_WR[i].proc_Ser_cmp_bad + arr_WR[i].proc_Ser_run_bad + arr_WR[i].proc_Bat_cmp_bad + arr_WR[i].proc_Bat_run_bad + arr_WR[i].proc_IndMod_cmp_bad + arr_WR[i].proc_IndMod_run_bad + arr_WR[i].proc_NoBO_bad + arr_WR[i].proc_Parser_cmp_bad + arr_WR[i].proc_Parser_run
  if arr_WR[i].sum_proc > 0:
    arr_WR[i].acc_proc = (arr_WR[i].sum_proc - arr_WR[i].sum_proc_bad) / float(arr_WR[i].sum_proc)
  else:
    arr_WR[i].acc_proc = 1.0
  
  arr_WR[i].sum_pa1 = arr_WR[i].pa1_Ind_cmp + arr_WR[i].pa1_Ind_run + arr_WR[i].pa1_Rng_cmp + arr_WR[i].pa1_Rng_run + arr_WR[i].pa1_Ser_cmp + arr_WR[i].pa1_Ser_run + arr_WR[i].pa1_Bat_cmp + arr_WR[i].pa1_Bat_run + arr_WR[i].pa1_IndMod_cmp + arr_WR[i].pa1_IndMod_run + arr_WR[i].pa1_NoBO + arr_WR[i].pa1_Parser_cmp + arr_WR[i].pa1_Parser_run
  arr_WR[i].sum_pa1_bad = arr_WR[i].pa1_Ind_cmp_bad + arr_WR[i].pa1_Ind_run_bad + arr_WR[i].pa1_Rng_cmp_bad + arr_WR[i].pa1_Rng_run_bad + arr_WR[i].pa1_Ser_cmp_bad + arr_WR[i].pa1_Ser_run_bad + arr_WR[i].pa1_Bat_cmp_bad + arr_WR[i].pa1_Bat_run_bad + arr_WR[i].pa1_IndMod_cmp_bad + arr_WR[i].pa1_IndMod_run_bad
  if arr_WR[i].sum_pa1 > 0:
    arr_WR[i].acc_pa1 = (arr_WR[i].sum_pa1 - arr_WR[i].sum_pa1_bad) / float(arr_WR[i].sum_pa1)
  else:
    arr_WR[i].acc_pa1 = 1.0

  arr_WR[i].sum_pa2 = arr_WR[i].pa2_Ind_cmp + arr_WR[i].pa2_Ind_run + arr_WR[i].pa2_Rng_cmp + arr_WR[i].pa2_Rng_run + arr_WR[i].pa2_Bat_cmp + arr_WR[i].pa2_Bat_run
  
  arr_WR[i].sum_ing = arr_WR[i].ing_Ind_cmp + arr_WR[i].ing_Ind_run + arr_WR[i].ing_Rng_cmp + arr_WR[i].ing_Rng_run + arr_WR[i].ing_Ser_cmp + arr_WR[i].ing_Ser_run + arr_WR[i].ing_Bat_cmp + arr_WR[i].ing_Bat_run + arr_WR[i].ing_IndMod_cmp + arr_WR[i].ing_IndMod_run + arr_WR[i].ing_Parser_cmp + arr_WR[i].ing_Parser_run + arr_WR[i].ing_Parser_ing
  arr_WR[i].sum_ing_bad = arr_WR[i].ing_Ind_cmp_bad + arr_WR[i].ing_Ind_run_bad + arr_WR[i].ing_Rng_cmp_bad + arr_WR[i].ing_Rng_run_bad + arr_WR[i].ing_Ser_cmp_bad + arr_WR[i].ing_Ser_run_bad + arr_WR[i].ing_Bat_cmp_bad + arr_WR[i].ing_Bat_run_bad + arr_WR[i].ing_IndMod_cmp_bad + arr_WR[i].ing_IndMod_run_bad + arr_WR[i].ing_Parser_cmp_bad + arr_WR[i].ing_Parser_run_bad + arr_WR[i].ing_Parser_ing_bad
  if arr_WR[i].sum_ing > 0:
    arr_WR[i].acc_ing = (arr_WR[i].sum_ing - arr_WR[i].sum_ing_bad) / float(arr_WR[i].sum_ing)
  else:
    arr_WR[i].acc_ing = 1.0

  arr_WR[i].sum_ia1 = arr_WR[i].ia1_Ind_cmp + arr_WR[i].ia1_Ind_run + arr_WR[i].ia1_Rng_cmp + arr_WR[i].ia1_Rng_run + arr_WR[i].ia1_Ser_cmp + arr_WR[i].ia1_Ser_run + arr_WR[i].ia1_Bat_cmp + arr_WR[i].ia1_Bat_run + arr_WR[i].ia1_IndMod_cmp + arr_WR[i].ia1_IndMod_run + arr_WR[i].ia1_Parser_cmp + arr_WR[i].ia1_Parser_run + arr_WR[i].ia1_Parser_ing
  arr_WR[i].sum_ia1_bad = arr_WR[i].ia1_Ind_cmp_bad + arr_WR[i].ia1_Ind_run_bad + arr_WR[i].ia1_Parser_ing_bad
  if arr_WR[i].sum_ia1 > 0:
    arr_WR[i].acc_ia1 = (arr_WR[i].sum_ia1 - arr_WR[i].sum_ia1_bad) / float(arr_WR[i].sum_ia1)
  else:
    arr_WR[i].acc_ia1 = 1.0
  
  arr_WR[i].sum_ia2 = arr_WR[i].ia2_Ind_cmp + arr_WR[i].ia2_Ind_run + arr_WR[i].ia2_Parser_ing
  
  arr_WR[i].sum_aps = arr_WR[i].aps_Stack_cmp + arr_WR[i].aps_Stack_run
  
  # BO_Parser_cmp
  
  with open('Source/Parser_cmp.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
      if t(row[col_to_num('A')]) >= arr_WR[i].week and t(row[col_to_num('A')]) < arr_WR[i+1].week and row[col_to_num('G')] in arr_agent:
        arr_WR[i].BO_Parser_cmp += int(row[col_to_num('E')])
  
  # BO_Parser_run
  
  with open('Source/Parser_run.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
      if t(row[col_to_num('A')]) >= arr_WR[i].week and t(row[col_to_num('A')]) < arr_WR[i+1].week and row[col_to_num('G')] in arr_agent:
        arr_WR[i].BO_Parser_run += int(row[col_to_num('E')])
      
  
  arr_WR[i].sum_BO = arr_WR[i].proc_Ind_cmp + arr_WR[i].proc_Ind_run + arr_WR[i].proc_Rng_cmp + arr_WR[i].proc_Rng_run + arr_WR[i].proc_Ser_cmp + arr_WR[i].proc_Ser_run + arr_WR[i].proc_Bat_cmp + arr_WR[i].proc_Bat_run + arr_WR[i].proc_IndMod_cmp + arr_WR[i].proc_IndMod_run + arr_WR[i].proc_NoBO + arr_WR[i].BO_Parser_cmp + arr_WR[i].BO_Parser_run 
  
  arr_WR[i].sum_task = arr_WR[i].sum_proc + arr_WR[i].sum_pa1 + arr_WR[i].sum_pa2 + arr_WR[i].sum_ing + arr_WR[i].sum_ia1 + arr_WR[i].sum_ia2 + arr_WR[i].sum_aps
  arr_WR[i].sum_task_bad = arr_WR[i].sum_proc_bad + arr_WR[i].sum_pa1_bad + arr_WR[i].sum_ing_bad + arr_WR[i].sum_ia1_bad
  if arr_WR[i].sum_task > 0:
    arr_WR[i].acc_overall = (arr_WR[i].sum_task - arr_WR[i].sum_task_bad) / float(arr_WR[i].sum_task)
  else:
    arr_WR[i].acc_overall = 1.0
  
  total_Ind += arr_WR[i].proc_Ind_cmp + arr_WR[i].proc_Ind_run
  total_Rng += arr_WR[i].proc_Rng_cmp + arr_WR[i].proc_Rng_run
  total_Ser += arr_WR[i].proc_Ser_cmp + arr_WR[i].proc_Ser_run
  total_Bat += arr_WR[i].proc_Bat_cmp + arr_WR[i].proc_Bat_run
  total_Parser += arr_WR[i].BO_Parser_cmp + arr_WR[i].BO_Parser_run
  total_IndMod += arr_WR[i].proc_IndMod_cmp + arr_WR[i].proc_IndMod_run
  total_NoBO += arr_WR[i].proc_NoBO

  total_proc += arr_WR[i].sum_proc
  total_pa1 += arr_WR[i].sum_pa1
  total_pa2 += arr_WR[i].sum_pa2
  total_ing += arr_WR[i].sum_ing
  total_ia1 += arr_WR[i].sum_ia1
  total_ia2 += arr_WR[i].sum_ia2
  total_aps += arr_WR[i].sum_aps
  
# 5. Write WeeklyRecord objects into the output sheet (Dashboard.csv)

csvfile = open('Output/Dashboard2.csv','w')
d = ','
for WR in arr_WR: # This line really needs rewriting.
  line = str(WR.week)+d+str(WR.proc_Ind_cmp)+d+str(WR.proc_Ind_run)+d+str(WR.proc_Rng_cmp)+d+str(WR.proc_Rng_run)+d+str(WR.proc_Ser_cmp)+d+str(WR.proc_Ser_run)+d+str(WR.proc_Bat_cmp)+d+str(WR.proc_Bat_run)+d+str(WR.proc_IndMod_cmp)+d+str(WR.proc_IndMod_run)+d+str(WR.proc_NoBO)+d+str(WR.proc_Parser_cmp)+d+str(WR.proc_Parser_run)+d+str(WR.proc_Ind_cmp_bad)+d+str(WR.proc_Ind_run_bad)+d+str(WR.proc_Rng_cmp_bad)+d+str(WR.proc_Rng_run_bad)+d+str(WR.proc_Ser_cmp_bad)+d+str(WR.proc_Ser_run_bad)+d+str(WR.proc_Bat_cmp_bad)+d+str(WR.proc_Bat_run_bad)+d+str(WR.proc_IndMod_cmp_bad)+d+str(WR.proc_IndMod_run_bad)+d+str(WR.proc_NoBO_bad)+d+str(WR.proc_Parser_cmp_bad)+d+str(WR.proc_Parser_run_bad)+d+str(WR.sum_proc)+d+str(WR.sum_proc_bad)+d+str(WR.acc_proc)+d+str(WR.pa1_Ind_cmp)+d+str(WR.pa1_Ind_run)+d+str(WR.pa1_Rng_cmp)+d+str(WR.pa1_Rng_run)+d+str(WR.pa1_Ser_cmp)+d+str(WR.pa1_Ser_run)+d+str(WR.pa1_Bat_cmp)+d+str(WR.pa1_Bat_run)+d+str(WR.pa1_IndMod_cmp)+d+str(WR.pa1_IndMod_run)+d+str(WR.pa1_NoBO)+d+str(WR.pa1_Parser_cmp)+d+str(WR.pa1_Parser_run)+d+str(WR.pa1_Ind_cmp_bad)+d+str(WR.pa1_Ind_run_bad)+d+str(WR.pa1_Rng_cmp_bad)+d+str(WR.pa1_Rng_run_bad)+d+str(WR.pa1_Ser_cmp_bad)+d+str(WR.pa1_Ser_run_bad)+d+str(WR.pa1_Bat_cmp_bad)+d+str(WR.pa1_Bat_run_bad)+d+str(WR.pa1_IndMod_cmp_bad)+d+str(WR.pa1_IndMod_run_bad)+d+str(WR.sum_pa1)+d+str(WR.sum_pa1_bad)+d+str(WR.acc_pa1)+d+str(WR.pa2_Ind_cmp)+d+str(WR.pa2_Ind_run)+d+str(WR.pa2_Rng_cmp)+d+str(WR.pa2_Rng_run)+d+str(WR.pa2_Bat_cmp)+d+str(WR.pa2_Bat_run)+d+str(WR.sum_pa2)+d+str(WR.ing_Ind_cmp)+d+str(WR.ing_Ind_run)+d+str(WR.ing_Rng_cmp)+d+str(WR.ing_Rng_run)+d+str(WR.ing_Ser_cmp)+d+str(WR.ing_Ser_run)+d+str(WR.ing_Bat_cmp)+d+str(WR.ing_Bat_run)+d+str(WR.ing_IndMod_cmp)+d+str(WR.ing_IndMod_run)+d+str(WR.ing_Parser_cmp)+d+str(WR.ing_Parser_run)+d+str(WR.ing_Parser_ing)+d+str(WR.ing_Ind_cmp_bad)+d+str(WR.ing_Ind_run_bad)+d+str(WR.ing_Rng_cmp_bad)+d+str(WR.ing_Rng_run_bad)+d+str(WR.ing_Ser_cmp_bad)+d+str(WR.ing_Ser_run_bad)+d+str(WR.ing_Bat_cmp_bad)+d+str(WR.ing_Bat_run_bad)+d+str(WR.ing_IndMod_cmp_bad)+d+str(WR.ing_IndMod_run_bad)+d+str(WR.ing_Parser_cmp_bad)+d+str(WR.ing_Parser_run_bad)+d+str(WR.ing_Parser_ing_bad)+d+str(WR.sum_ing)+d+str(WR.sum_ing_bad)+d+str(WR.acc_ing)+d+str(WR.ia1_Ind_cmp)+d+str(WR.ia1_Ind_run)+d+str(WR.ia1_Rng_cmp)+d+str(WR.ia1_Rng_run)+d+str(WR.ia1_Ser_cmp)+d+str(WR.ia1_Ser_run)+d+str(WR.ia1_Bat_cmp)+d+str(WR.ia1_Bat_run)+d+str(WR.ia1_IndMod_cmp)+d+str(WR.ia1_IndMod_run)+d+str(WR.ia1_Parser_cmp)+d+str(WR.ia1_Parser_run)+d+str(WR.ia1_Parser_ing)+d+str(WR.ia1_Ind_cmp_bad)+d+str(WR.ia1_Ind_run_bad)+d+str(WR.ia1_Parser_ing_bad)+d+str(WR.sum_ia1)+d+str(WR.sum_ia1_bad)+d+str(WR.acc_ia1)+d+str(WR.ia2_Ind_cmp)+d+str(WR.ia2_Ind_run)+d+str(WR.ia2_Parser_ing)+d+str(WR.sum_ia2)+d+str(WR.aps_Stack_cmp)+d+str(WR.aps_Stack_run)+d+str(WR.sum_aps)+d+str(WR.sum_mail)+d+str(WR.sum_BO)+d+str(WR.sum_task)+d+str(WR.sum_task_bad)+d+str(WR.acc_overall)+'\n'

  csvfile.write(line)

#sys.stdout.write('.')
#sys.stdout.flush()









