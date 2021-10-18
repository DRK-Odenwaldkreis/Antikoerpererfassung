#!/usr/bin/python3
# coding=utf-8

# This file is part of DRK Antikoerpererfassung.


import os
import sys
import configparser

def read_config(section,variable):
    config = configparser.ConfigParser(interpolation=None)
    config.read('../config.ini')
    return config.get(section,variable)
