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

def cn2(type_BO,type_task):
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

date_start = datetime(2017, 12, 4)
date_end = datetime(2018, 12, 31)

arr_WR = []
arr_WR.append(WeeklyRecord())

date_intermediate = date_start

counter = 1

while date_intermediate < date_end:
  arr_WR.append(WeeklyRecord())
  arr_WR[counter].week = date_intermediate
  #print(arr_WR[counter].week)
  counter += 1
  date_intermediate += timedelta(days = 7)

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
      s.st_proc = row[cn(source,'st_proc')] # What if the index is -1? It's ok. The sheets always have empty columns. If that sounds risky, add if statements later. This is a big problem....
      s.proc = row[cn(source,'proc')]
      s.st_pa1 = row[cn(source,'st_pa1')]
      s.pa1 = row[cn(source,'pa1')]
      s.fd_proc = row[cn(source,'fd_proc')]
      s.st_pa2 = row[cn(source,'st_pa2')]
      s.pa2 = row[cn(source,'pa2')]
      s.fd_pa1 = row[cn(source,'fd_pa1')]
      cn2(source,'fd_pa1')
      s.st_ing = row[cn(source,'st_ing')]
      s.ing = row[cn(source,'ing')]
      s.st_ia1 = row[cn(source,'st_ia1')]
      s.ia1 = row[cn(source,'ia1')]
      s.fd_ing = row[cn(source,'fd_ing')]
      s.st_ia2 = row[cn(source,'st_ia2')]
      s.ia2 = row[cn(source,'ia2')]
      s.fd_ia1 = row[cn(source,'fd_ia1')]
      s.title = row[cn(source,'title')]
      s.bpa = row[cn(source,'bpa')]
      arr_Stack.append(s)
  return arr_Stack

IndMod_cmp = arr_Stack('IndMod_cmp')




#sys.stdout.write('.')
#sys.stdout.flush()









