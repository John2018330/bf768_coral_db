#!/usr/bin/env python3

import cgi
import pymysql
import cgitb
import json
import ast
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
    year = form.getlist("year_array")
    ecological_vol = form.getvalue("eco_vol_val")
    ln_ecological_vol = form.getvalue("ln_eco_vol_val")
    allele_freq = form.getvalue("allele_freq")
    length = form.getvalue("length_val")
    width = form.getvalue("width_val")
    height = form.getvalue("height_val")
    counts = form.getvalue("count")
    averages = form.getvalue("average")
    groupbys = form.getvalue("groupby")
    vcf = form.getvalue("vcf")
    
    # Data Modifications
    # Year, Location, ... (checkbox filters) come in as a string 
    # separated by colons, turn this into a python list to iterate over
    year = year[0].split(':')


    # Construct the SQL query based on form data
    query = "SELECT * FROM y2015 LIMIT 10"
    # tagid, location, notes, alive_status, length_cm, width_cm, height_cm, eco_volume, ln_eco_volume, volume_cylinder, tip_number, old_tag

    yquery = ""
    yquery = "SELECT tagid, location, notes, alive_status, length_cm, width_cm, height_cm, eco_volume, ln_eco_volume, volume_cylinder, tip_number, old_tag FROM id_table "

    for i in year:
        yquery += "LEFT JOIN y" + i + " on y" + i + ".tagid = id_table." + i + "_id "
    #yquery = yquery[:-5]
    # if len(location) > 0:
    #     yquery += "AND "
    #     for i in location:
    #         yquery += "location = " + "'" + i + "'" + " OR "
    #     yquery = yquery[:-3]


    # if len(mortality) > 0:
    #     yquery += "AND "
    #     for i in mortality:
    #         print(i)
    #         yquery += "alive_status = " + "'" + i + "'" + " OR "
    #         yquery = yquery[:-3]

    #fakeyear = ["2016","2017"]
    zquery = ""
    for i in year: 

        zquery += "SELECT *, '" + i + "' as year FROM y" + i 
        #if vcf = "Yes":
            #zquery += " JOIN vcf"
        
        if len(location) > 0 or len(mortality) > 0:
            zquery += " WHERE "
        
        # if tagid != "":
        #     zquery += "tagid = '" + tagid + "'"
        #     if len(location) > 0 or len(mortality):
        #         zquery += " AND "
               
        
        # if scaffold > 0:
        #     zquery += "CHROM = " + scaffold
        #     if len(location) > 0 or len(mortality):
        #         zquery += " AND "

        if len(location) > 0:
            zquery += "location in ("
            
            for j in location:
                zquery +="'" + j + "', "

            zquery = zquery[:-2]
            zquery += ")"
            if len(mortality) > 0:
                zquery += " AND "

        if len(mortality) > 0:
            zquery += "alive_status in ("
            for k in mortality:
                zquery +="'" + k + "', "
            zquery = zquery[:-2]
            zquery += ")"

        
        zquery += " UNION "
    zquery = zquery[:-6]
    


    try:
        # Execute the query
        results = execute_query(cursor, zquery)
        print('')
        print(json.dumps(results))
        
    except pymysql.Error as e:
        error_message = f'<p style="color:red;">Error executing query: {e}</p>'

cursor.close() 
connection.close()



# Print HTML content including query results
print(vcf_table)
