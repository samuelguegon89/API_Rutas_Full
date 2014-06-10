#!/usr/bin/python
# -*- coding: utf-8 -*-

import goslate

texto=raw_input('texto: ')
gs = goslate.Goslate()
print gs.translate(texto, 'es')
