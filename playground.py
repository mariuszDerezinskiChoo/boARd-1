#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:29:59 2019

@author: Mariusz
"""

import requests as req

response = req.get("https://board1331.herokuapp.com/ROOM")
print(response.json())