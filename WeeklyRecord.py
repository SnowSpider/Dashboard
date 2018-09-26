#!/usr/bin/env python

import csv
import re 
import fileinput
import sys

from datetime import datetime
from datetime import timedelta

class WeeklyRecord(object):
  def __init__(self):
    
    self.week = datetime(2017, 12, 4)

    self.proc_Ind_cmp = 0 # Number of Symphony BO processing for Individual Completed sheet
    self.proc_Ind_run = 0 # Number of Symphony BO processing for Individual Running sheet
    self.proc_Rng_cmp = 0 # Number of Symphony BO processing for Range Completed sheet
    self.proc_Rng_run = 0 # Number of Symphony BO processing for Range Running sheet
    self.proc_Ser_cmp = 0
    self.proc_Ser_run = 0
    self.proc_Bat_cmp = 0
    self.proc_Bat_run = 0
    self.proc_IndMod_cmp = 0
    self.proc_IndMod_run = 0
    self.proc_NoBO = 0
    self.proc_Parser_cmp = 0
    self.proc_Parser_run = 0

    self.proc_Ind_cmp_bad = 0
    self.proc_Ind_run_bad = 0
    self.proc_Rng_cmp_bad = 0
    self.proc_Rng_run_bad = 0
    self.proc_Ser_cmp_bad = 0
    self.proc_Ser_run_bad = 0
    self.proc_Bat_cmp_bad = 0
    self.proc_Bat_run_bad = 0
    self.proc_IndMod_cmp_bad = 0
    self.proc_IndMod_run_bad = 0
    self.proc_NoBO_bad = 0
    self.proc_Parser_cmp_bad = 0
    self.proc_Parser_run_bad = 0

    self.sum_proc = 0
    self.sum_proc_bad = 0
    self.acc_proc = 0

    self.pa1_Ind_cmp = 0
    self.pa1_Ind_run = 0
    self.pa1_Rng_cmp = 0
    self.pa1_Rng_run = 0
    self.pa1_Ser_cmp = 0
    self.pa1_Ser_run = 0
    self.pa1_Bat_cmp = 0
    self.pa1_Bat_run = 0
    self.pa1_IndMod_cmp = 0
    self.pa1_IndMod_run = 0
    self.pa1_NoBO = 0
    self.pa1_Parser_cmp = 0
    self.pa1_Parser_run = 0

    self.pa1_Ind_cmp_bad = 0
    self.pa1_Ind_run_bad = 0
    self.pa1_Rng_cmp_bad = 0
    self.pa1_Rng_run_bad = 0
    self.pa1_Ser_cmp_bad = 0
    self.pa1_Ser_run_bad = 0
    self.pa1_Bat_cmp_bad = 0
    self.pa1_Bat_run_bad = 0
    self.pa1_IndMod_cmp_bad = 0
    self.pa1_IndMod_run_bad = 0

    self.sum_pa1 = 0
    self.sum_pa1_bad = 0
    self.acc_pa1 = 0

    self.pa2_Ind_cmp = 0
    self.pa2_Ind_run = 0
    self.pa2_Rng_cmp = 0
    self.pa2_Rng_run = 0
    self.pa2_Bat_cmp = 0
    self.pa2_Bat_run = 0

    self.sum_pa2 = 0

    self.ing_Ind_cmp = 0
    self.ing_Ind_run = 0
    self.ing_Rng_cmp = 0
    self.ing_Rng_run = 0
    self.ing_Ser_cmp = 0
    self.ing_Ser_run = 0
    self.ing_Bat_cmp = 0
    self.ing_Bat_run = 0
    self.ing_IndMod_cmp = 0
    self.ing_IndMod_run = 0
    self.ing_Parser_cmp = 0
    self.ing_Parser_run = 0
    self.ing_Parser_ing = 0

    self.ing_Ind_cmp_bad = 0
    self.ing_Ind_run_bad = 0
    self.ing_Rng_cmp_bad = 0
    self.ing_Rng_run_bad = 0
    self.ing_Ser_cmp_bad = 0
    self.ing_Ser_run_bad = 0
    self.ing_Bat_cmp_bad = 0
    self.ing_Bat_run_bad = 0
    self.ing_IndMod_cmp_bad = 0
    self.ing_IndMod_run_bad = 0
    self.ing_Parser_cmp_bad = 0
    self.ing_Parser_run_bad = 0
    self.ing_Parser_ing_bad = 0

    self.sum_ing = 0
    self.sum_ing_bad = 0
    self.acc_ing = 0

    self.ia1_Ind_cmp = 0
    self.ia1_Ind_run = 0
    self.ia1_Rng_cmp = 0
    self.ia1_Rng_run = 0
    self.ia1_Ser_cmp = 0
    self.ia1_Ser_run = 0
    self.ia1_Bat_cmp = 0
    self.ia1_Bat_run = 0
    self.ia1_IndMod_cmp = 0
    self.ia1_IndMod_run = 0
    self.ia1_Parser_cmp = 0
    self.ia1_Parser_run = 0
    self.ia1_Parser_ing = 0

    self.ia1_Ind_cmp_bad = 0
    self.ia1_Ind_run_bad = 0
    self.ia1_Parser_ing_bad = 0

    self.sum_ia1 = 0
    self.sum_ia1_bad = 0
    self.acc_ia1 = 0

    self.ia2_Ind_cmp = 0
    self.ia2_Ind_run = 0
    self.ia2_Parser_ing = 0

    self.sum_ia2 = 0

    self.aps_Stack_cmp = 0 # audit processed sheet
    self.aps_Stack_run = 0 # audit processed sheet
    
    self.sum_aps = 0

    self.sum_mail = 0
    
    self.BO_Parser_cmp = 0
    self.BO_Parser_run = 0
    
    self.sum_BO = 0
    
    self.sum_task = 0
    
    self.sum_task_bad = 0

    self.acc_overall = 0
    












