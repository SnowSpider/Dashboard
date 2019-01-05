#!/usr/bin/env python

import csv
import re 
import fileinput
import sys


class Blackout(object):

  def __init__(self, timestamp, scope, link_mail, link_sheet, link_bpa, title, date_start, date_end, time_start, time_end, boType, station, owner_proc, owner_1stProcAud, owner_2ndProcAud, owner_ing, owner_1stIngAud, owner_2ndIngAud, reason_1stProcAud, reason_2ndProcAud, reason_1stIngAud, reason_2ndIngAud):
    self.timestamp = timestamp
    self.scope = scope
    self.link_mail = link_mail
    self.link_sheet = link_sheet
    self.link_bpa = link_bpa
    self.title = title
    self.date_start = date_start
    self.date_end = date_end
    self.time_start = time_start
    self.time_end = time_end
    self.boType = boType
    self.station = station
    self.owner_proc = owner_proc
    self.owner_1stProcAud = owner_1stProcAud
    self.owner_2ndProcAud = owner_2ndProcAud
    self.owner_ing = owner_ing
    self.owner_1stIngAud = owner_1stIngAud
    self.owner_2ndIngAud = owner_2ndIngAud
    self.reason_1stProcAud = reason_1stProcAud
    self.reason_2ndProcAud = reason_2ndProcAud
    self.reason_1stIngAud = reason_1stIngAud
    self.reason_2ndIngAud = reason_2ndIngAud

  def get_timestamp(self):
    return self.timestamp;

  def get_scope(self):
    return self.scope

  def get_link_mail(self):
    return self.link_mail

  def get_link_sheet(self):
    return self.link_sheet

  def get_link_bpa(self):
    return self.link_bpa

  def get_title(self):
    return self.title

  def get_date_start(self):
    return self.date_start

  def get_date_end(self):
    return self.date_end

  def get_time_start(self):
    return self.time_start

  def get_time_end(self):
    return self.time_end

  def get_boType(self):
    return self.boType

  def get_station(self):
    return self.station

  def get_owner_proc(self):
    return self.owner_proc

  def get_owner_1stProcAud(self):
    return self.owner_1stProcAud

  def get_owner_2ndProcAud(self):
    return self.owner_2ndProcAud

  def get_owner_ing(self):
    return self.owner_ing

  def get_owner_1stIngAud(self):
    return self.owner_1stIngAud

  def get_owner_2ndIngAud(self):
    return self.owner_2ndIngAud

  def get_reason_1stProcAud(self):
    return self.reason_1stProcAud

  def get_reason_2ndProcAud(self):
    return self.reason_2ndProcAud

  def get_reason_1stIngAud(self):
    return self.reason_1stIngAud

  def get_reason_2ndIngAud(self):
    return self.reason_2ndIngAud
