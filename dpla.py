#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import requests
import datetime

now = datetime.datetime.now()

con = None
dp_api_key = os.environ['DP_API_KEY']

try:
    # Connect to database
    con = lite.connect('dpla.sqlite3')

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLite version: %s" % data

    cur.execute('SELECT * FROM `dpla`;')
    rows = cur.fetchall()

    # Create csv file based on current time
    file_name = "dpla_results_" + now.strftime("%m-%d-%y") + ".csv"

    # Open csv file for writing and create header row
    # App uses `sep=@` to tell Excel to use '@' as a row seperator,
    # in case incoming information contains commas.
    file = open(file_name, 'w')
    file.write("sep=@\n")
    file.write("ID@ Name@ Creator (MWDL)@ Creator (DPLA)@ Subject (MWDL)@ Subject (DPLA)\n")

    for row in rows:
      mlid = row[1]
      name = row[2]

      # Creator - MWDL
      mwdl_cr_req = "http://api.dp.la/v2/items?api_key=%s&provider.@id=http://dp.la/api/contributor/mwdl&sourceResource.creator=%s&page_size=0" % (dp_api_key, name)

      # Creator - DPLA
      dpla_cr_req = "http://api.dp.la/v2/items?api_key=%s&sourceResource.creator=%s&page_size=0" % (dp_api_key, name)

      # Subject - MWDL
      mwdl_sub_req = "http://api.dp.la/v2/items?api_key=%s&provider.@id=http://dp.la/api/contributor/mwdl&sourceResource.subject=%s&page_size=0" % (dp_api_key, name)

      # Subject - DPLA
      dpla_sub_req = "http://api.dp.la/v2/items?api_key=%s&sourceResource.subject=%s&page_size=0" % (dp_api_key, name)

      req = "http://api.dp.la/v2/items?api_key=%s&sourceResource.subject=%s&page_size=0" % (dp_api_key, name)

      mwdl_cr_resp  = requests.get(mwdl_cr_req)
      dpla_cr_resp  = requests.get(dpla_cr_req)
      mwdl_sub_resp = requests.get(mwdl_sub_req)
      dpla_sub_resp = requests.get(dpla_sub_req)

      mwdl_cr_resp_json  = mwdl_cr_resp.json()
      dpla_cr_resp_json  = dpla_cr_resp.json()
      mwdl_sub_resp_json = mwdl_sub_resp.json()
      dpla_sub_resp_json = dpla_sub_resp.json()

      output_results = "%s@ %s@ %s@ %s@ %s@ %s" % (mlid, name, mwdl_cr_resp_json["count"], dpla_cr_resp_json["count"], mwdl_sub_resp_json["count"], dpla_sub_resp_json["count"])
      print output_results
      file.write("%s\n" % (output_results.encode('utf-8')))

    file.close()

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
