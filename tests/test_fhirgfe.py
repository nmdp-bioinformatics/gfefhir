#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    fhirgfe fhirGFE.
#    Copyright (c) 2018 Be The Match operated by National Marrow Donor Program. All Rights Reserved.
#
#    This library is free software; you can redistribute it and/or modify it
#    under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 3 of the License, or (at
#    your option) any later version.
#
#    This library is distributed in the hope that it will be useful, but WITHOUT
#    ANY WARRANTY; with out even the implied warranty of MERCHANTABILITY or
#    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
#    License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this library;  if not, write to the Free Software Foundation,
#    Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.
#
#    > http://www.fsf.org/licensing/licenses/lgpl.html
#    > http://www.opensource.org/licenses/lgpl-license.php
#



"""
test_fhirgfe
----------------------------------

Tests for `fhirgfe` module.
"""


import sys
import unittest
from fhirclient.client import FHIRClient
from gfefhir import GfeFHIR
from fhirclient import client
from fhirclient import server


class TestFhirgfe(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        settings = {
            'app_id': 'my_web_app',
            'api_base': 'http://fhirtest.b12x.org/r3'
        }
        smart = client.FHIRClient(settings=settings)
        gfefhir = GfeFHIR(smart=smart)
        self.assertIsInstance(gfefhir, GfeFHIR)
        gfefhir.annotate('6289')
        #for ids in ['6227','6228','6229','6234','6235','6236','6241','6242','6243',]:
        #    gfefhir.annotate(ids)
        #    print("--------------")
        pass





