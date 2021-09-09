import discord
import random
import asyncio
import os
import sys
import datetime
import platform
import json
import time
import aiohttp
import requests
import praw
import asyncpraw
from discord.ext import commands, tasks
from random import choice
from discord.ext.commands import clean_content
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from asyncio import sleep


colors = [0x680af5,0x2E10ED,0x8CF9C1,0xF88000,0xFCFF00,0xed129f,0xed3212,0x1ACFE7,0x0FD150,0xFE2D00]

def ownercheck(ctx):
    return ctx.message.author.id == 503314109643882529
