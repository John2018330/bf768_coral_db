#!/usr/bin/env python3

import cgi
import pymysql
import cgitb
import json
from decimal import Decimal
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

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Type not serializable")



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
    allele_freq = form.getvalue("allele_freq_val")
    length = form.getvalue("length_val")
    width = form.getvalue("width_val")
    height = form.getvalue("height_val")
    counts = form.getvalue("count")
    averages = form.getvalue("average")
    groupbys = form.getvalue("groupby")
    vcf = form.getvalue("vcf")
    
    # For graphs
    scaffold_graph = form.getvalue("scaffold_graph")
    geno_graph = form.getvalue("geno_graph")

    # Data Modifications
    # Year, Location, ... (checkbox filters) come in as a string 
    # separated by colons, turn this into a python list to iterate over
    if year:
        year = year[0].split(':')
    
    if location:
        location = location[0].split(':')
    
    if mortality:
        mortality = mortality[0].split(':')


    # If form is for graph
    bar_query = ""
    if scaffold_graph:
        bar_query += "SELECT location, count(GT) FROM vcf join y2018 on vcf.CORAL_id = y2018.tagid WHERE CHROM = '" + scaffold_graph + "' AND GT "
        if geno_graph == "Homozygous Alt":
            bar_query += "= '1/1' "
        if geno_graph == "Homozygous Ref":
            bar_query += "= '0/0' "
        if geno_graph == "Heterozygous":
            bar_query += "= '0/1' "
        
        bar_query += " GROUP BY location"


        try:
            # Execute the query
            results = execute_query(cursor, bar_query)
            print('')

            
            plot_data = [list(item) for item in results]
            y_axis = 'Number of ' + str(geno_graph) + ' Individuals'
            plot_data.insert(0,['Location',y_axis])
            plot_data_tuple = tuple(plot_data)

            print(json.dumps(plot_data_tuple))
            
        except pymysql.Error as e:
            error_message = f'<p style="color:red;">Error executing query: {e}</p>'



    else:
        ####Shortcomings of the query - the groupby doesnt specify the alive and dead within the groupby mortality
        zquery = ""
        for i in year: 
        #select statement
            zquery += "SELECT *, '" + i + "' as year FROM y" + i 
            
            #conditional for joining vcf
            if vcf == "Yes":
                zquery += " JOIN vcf on vcf.CORAL_ID = y" + i + ".tagid"
            
            #sliders are always added to query
            zquery += " WHERE eco_volume < " + str(ecological_vol) + " AND length_cm < " + str(length) +  " AND width_cm < " + str(width) + " AND height_cm < " + str(height)


            #only uses vcf slider if vcf is yes to not create error
            if vcf == "Yes":
                zquery += " AND AF < " + allele_freq
            
            #filters
            #if tagid != "":
            if tagid:
                zquery += " AND tagid = '" + tagid + "'"

            #if scaffoldid != "":
            if scaffoldid:
                zquery += " AND CHROM = " + scaffoldid

            if len(location) > 0:
                zquery += " AND location in ("
                for j in location:
                    zquery +="'" + j + "', "
                zquery = zquery[:-2]
                zquery += ")"

            if len(mortality) > 0:
                zquery += " AND alive_status in ("
                for k in mortality:
                    zquery +="'" + k + "', "
                zquery = zquery[:-2]
                zquery += ")"

            #groupby filters
            
            # if len(groupbys) > 0:
            #     zquery += " GROUP BY " 
            #     for i in groupbys:
            #         zquery += i + ", "
            #     zquery = zquery[:-2]
                #for i in counts:
                #    zquery = zquery[:10] + "count(" + i + '), ' + zquery[10:]
                #for i in averages:
                #    zquery = zquery[:10] + "avg(" + i + '), ' + zquery[10:]
        
            zquery += " UNION "
        zquery = zquery[:-6]


        try:
            # Execute the query
            results = execute_query(cursor, zquery)
            print('')
            print(json.dumps(results, default=decimal_serializer))
            
        except pymysql.Error as e:
            error_message = f'<p style="color:red;">Error executing query: {e}</p>'

cursor.close() 
connection.close()



# Print HTML content including query results
# print(vcf_table)


###avg volume by year and location could select the specific location instead of having it all in once
#line graph?
"""
SELECT avg(eco_volume), year, location
FROM(
SELECT *, 2015 as year
From y2015 
UNION
SELECT *, 2016 as year
From y2016 
UNION
SELECT *, 2017 as year
From y2017
UNION
SELECT *, 2018 as year
From y2018
) as y
group by year,location
"""

#sample queries that show counts of variants by location
#bar chart
# user would select scaffold and Ref or alt 
"""

SELECT count(GT), location 
FROM vcf join y2018 on vcf.CORAL_id = y2018.tagid
WHERE CHROM = "Sc0000211" AND GT = "1/1"
GROUP BY location


SELECT count(GT), location 
FROM vcf join y2018 on vcf.CORAL_id = y2018.tagid
WHERE CHROM = "Sc0000211" or GT in ("1/0", "0/0", "0/1")
GROUP BY location


"""
#scaffold_graph = "SC0000123"
#genotype = "Major"

# bar_query = ""
# if scaffold_graph:
#     bar_query += "SELECT location, count(GT) FROM vcf join y2018 on vcf.CORAL_id = y2018.tagid WHERE CHROM = '" + scaffold_graph + "' AND GT "
#     if geno_graph == "Homozygous Alt":
#         bar_query += "= '1/1' "
#     if geno_graph == "Homozygous Ref":
#         bar_query += "= '1/1' "
#     if geno_graph == "Heterozygous":
#         bar_query += "= '0/1' "
    
#     bar_query += " GROUP BY location"


#     try:
#         # Execute the query
#         results = execute_query(cursor, bar_query)
#         print('')

        
#         plot_data = [list(item) for item in results]
#         y_axis = 'Number of ' + geno_graph + ' Individuals'
#         plot_data.insert(0,['Location',y_axis])
#         plot_data_tuple = tuple(plot_data)

#         print(json.dumps(plot_data_tuple))
        
#     except pymysql.Error as e:
#         error_message = f'<p style="color:red;">Error executing query: {e}</p>'

