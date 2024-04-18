#!/usr/bin/env python3

import cgi
import pymysql
import cgitb
import json
from string import Template

# Print content type
print("Content-type: text/html\n\n")



cgitb.enable()
form = cgi.FieldStorage()

def connect_database(database, username, password):
    connection = pymysql.connect(
        host='bioed.bu.edu',
        user=username,
        password=password,
        db=database,
        port=4253
    )
    cursor = connection.cursor()
    return connection, cursor

def execute_query(cursor, query):
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except pymysql.Error as e:
        print(f"Error executing query: {query}")
        print(f"Error message: {e}")
        results = None
    return results

connection, cursor = connect_database("Team_7", "saumyapo", "saumyapo")

vcf_table = ""

if form:
    # Retrieve form data
    tagid = form.getvalue("tagid")
    scaffoldid = form.getvalue("scaffoldid")
    location = form.getlist("location")
    mortality = form.getlist("mortality")
    year = form.getlist("year")
    ecological_vol = form.getvalue("eco_vol_val")
    ln_ecological_vol = form.getvalue("ln_eco_vol_val")
    allele_freq = form.getvalue("allele_freq")
    length = form.getvalue("length_val")
    width = form.getvalue("width_val")
    height = form.getvalue("height_val")

 
    # Construct the SQL query based on form data
    query = "SELECT * FROM y2015 LIMIT 10"

    yquery = ""
    yquery = "SELECT * FROM "
    for i in year:
        yquery += i + " JOIN "
    yquery = yquery[:-5]

    


    if len(location) > 0:
        yquery += "AND "
        for i in location:
            yquery += "location = " + "'" + i + "'" + " OR "
        yquery = yquery[:-3]


    if len(mortality) > 0:
        yquery += "AND "
        for i in mortality:
            print(i)
            yquery += "alive_status = " + "'" + i + "'" + " OR "
            yquery = yquery[:-3]



    #if allele_freq:
    #    query += f"AF <= {allele_freq}"

    try:
        # Execute the query
        #print(query)
        results = execute_query(cursor, query)
        print('')
        print(json.dumps(results))
        
    except pymysql.Error as e:
        error_message = f'<p style="color:red;">Error executing query: {e}</p>'

cursor.close()
connection.close()



# Print HTML content including query results
print(vcf_table)
