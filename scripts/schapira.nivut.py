#!/usr/bin/python
# -*- coding: utf-8 -*-
import pywikibot
import pywikibot.pagegenerators
site = pywikibot.Site('he', 'wikisource')  # The site we want to run our bot on
page = pywikibot.Page(site, u"משתמשת:אור שפירא")
filterredir = False
for Page in  pywikibot.pagegenerators.AllpagesPageGenerator():
	print(Page.title())
print(page)
print(pywikibot.pagegenerators)
