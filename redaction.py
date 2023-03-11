#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

import configparser
import pathlib

import pandas

from gdoc_down.core import GDocDown

from oauth2client.service_account import ServiceAccountCredentials


config = configparser.ConfigParser()
nom_config = pathlib.Path('~/.config/menu_planck/pv_planck.config')\
    .expanduser()
config.read(nom_config)

fichier = '/Users/emilejetzer/Library/CloudStorage/GoogleDrive-emile.jetzer@gmail.com/.shortcut-targets-by-id/1ci74AlAYlkdlqJPATyKxztaOdBnNHic8/Planck/Affaires\ légales/Procès\ verbaux/CA/A22/Novembre/22.gdoc'

# Tiré de https://stackoverflow.com/a/18296318
scope = ['https://spreadsheets.google.com/feeds',
         'https://docs.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    config['google']['credentials'],
    scope)

gestionnaire = GDocDown()
#credentials = gestionnaire.get_credentials()
resource = gestionnaire.authenticate(credentials)
gestionnaire.download(fichier, 'latex')
