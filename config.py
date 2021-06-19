import discord
import random
import asyncio
import os
import sys
import datetime
import giphy_client
import platform
import json
import time
from discord.ext import commands, tasks
from random import choice
from giphy_client.rest import ApiException
from discord.ext.commands import clean_content
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from asyncio import sleep

########################################################################################################################
BOT_PREFIX = '9'
TOKEN = "NzUwNzg5MjQ3ODkxNTM3OTcy.X0_o-Q.Ts3aldC0AhotqTqdH_QDEo_aAVg"
########################################################################################################################