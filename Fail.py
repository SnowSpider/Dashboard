#!/usr/bin/env python

import csv
import re 
import fileinput
import sys


class Fail(object):

  def __init__(self, timestamp, scope, type_task, link_mail, link_sheet, link_bpa, owner, auditor, reason):
    self.timestamp = timestamp
    self.scope = scope
    self.type_task = type_task
    self.link_mail = link_mail
    self.link_sheet = link_sheet
    self.link_bpa = link_bpa
    self.owner = owner
    self.auditor = auditor
    self.reason = reason

  def get_timestamp(self):
    return self.timestamp;

  def get_scope(self):
    return self.scope

  def get_type_task(self):
    return self.type_task

  def get_link_mail(self):
    return self.link_mail

  def get_link_sheet(self):
    return self.link_sheet

  def get_link_bpa(self):
    return self.link_bpa

  def get_owner(self):
    return self.owner
    
  def get_auditor(self):
    return self.auditor

  def get_reason(self):
    return self.reason
