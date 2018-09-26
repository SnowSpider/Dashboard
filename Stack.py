#!/usr/bin/env python

import csv
import re 
import fileinput
import sys


class Stack(object):
  def __init__(self):
    self.scope = ""
    self.st_proc = ""
    self.proc = ""
    self.st_pa1 = ""
    self.pa1 = ""
    self.fd_proc = ""
    self.st_pa2 = ""
    self.pa2 = ""
    self.fd_pa1 = ""
    self.st_ing = ""
    self.ing = ""
    self.st_ia1 = ""
    self.ia1 = ""
    self.fd_ing = ""
    self.st_ia2 = ""
    self.ia2 = ""
    self.fd_ia1 = ""
    self.title = ""
    self.bpa = ""

