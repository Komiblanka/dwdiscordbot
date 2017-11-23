from discordbot import *
from configparser import SafeConfigParser
import argparse

# Argument parsing.
parser = argparse.ArgumentParser(description='Welcome to dw discord bot') 
parser.add_argument('configFile', help='Config file for loading all parameters')
args = parser.parse_args()

# Using config file for parameters
parser = SafeConfigParser()
parser.read(args.configFile)

token = parser.get('discord', 'token') 

mybot = discordbot(token)
