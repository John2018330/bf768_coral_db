#!/usr/bin/env python3

import cgi
import pymysql
import cgitb
from string import Template

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

def execute_query(cursor, query, gene, score):
	try:
		cursor.execute(query, (score, gene))
		results = cursor.fetchall()
	except pymysql.Error as e:
		print(f"Error executing query: {query}")
		print(f"Error message: {e}")
		results = None
	return results

connection, cursor = connect_database("Team_7", "saumyapo", "saumyapo")

intro_html = """
"""
error_message = ""
table_html = ""
summary_html = ""

if form:
	tagid = form.getvalue("tagid")
	location = form.getvalue("location")
    status = form.getvalue("status")
    length = form.getvalue("length")
    width = form.getvalue("width")
    height = form.getvalue("height")
    ecological_vol = form.getvalue("eco_vol")
    ln_ecological_vol = form.getvalue("ln_eco_vol")
    volume_cylinder = form.getvalue("vol_cylinder")
    tipid = form.getvalue("tipid")
    
    
    coralid = form.getvalue("coralid")
    quality = form.getvalue("quality")
	allele_freq = form.getvalue("allele_freq")
    
	if gene:  
		query_gene_check = "SELECT * FROM gene WHERE name = %s"
        try:
            cursor.execute(query_gene_check, (gene,))
            gene_check_result = cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error message: {e}")
            gene_check_result = None
        
	if gene_check_result:
		query = "SELECT mid, m.name, score FROM miRNA m JOIN targets t USING(mid) JOIN gene g USING (gid) WHERE t.score <= %s and g.name = %s ORDER BY t.score ;"
		try:
			results = execute_query(cursor, query, gene, score)
		except Exception as e:
			print(f"Error message: {e}")
			results = None

		if results:
			phenotype_table = Template(
			"""
			<table>
				<thead>
					<tr>
						<th>TagID</th>
						<th>Location</th>
						<th>Alive status</th>
                        <th>Length (cm)</th>
                        <th>Width (cm)</th>
                        <th>Height (cm)</th>
                        <th>Ecological Volume(cm3)</th>
                        <th>ln(ecovolume)</th>
                        <th>Volume_Cylinder</th>
                        <th>TipID</th>

					</tr>
				</thead>
				<tbody>
					${table_rows}
				</tbody>
			</table>
			"""
		)

            # now create the rows
            table_rows = ""
            for row in results:
                table_rows += """
                <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                </tr>
                """ % (row[0], row[1], row[2])

                # add rows to table_html
            table_html = phenotype_table.safe_substitute(table_rows=table_rows)
            count = len(results)
            summary_html = f"<span class='summary'>Summary:</span> Gene {gene} is targeted by {count} miRNAs with scores ≤ {score}"

		else:
			error_message = '<p style="color:red;">No data found for the score =< {} for {}</p>'.format(score,gene)
			count = 0
            summary_html = f"<span class='summary'>Summary:</span> Gene {gene} is targeted by {count} miRNAs with scores ≤ {score}"
    else:
        error_message = '<p style="color:red;">{} does not exist in the miRNA database or is spelt incorrectly.</p>'.format(gene)
    else:
        error_message = '<p style="color:red;">You didn\'t submit any data!</p>'  

print("Content-type: text/html\n")
print(error_message)
print(intro_html)
print(summary_html)
print("<br>")

if(table_html):
    print("<br>")
    print("<span class='query-output'>Query Output:</span><br>")
    print(table_html)

cursor.close()
connection.close()
