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
    ecological_vol = form.getvalue("eco_vol")
    ln_ecological_vol = form.getvalue("ln_eco_vol")
    allele_freq = form.getvalue("allele_freq")
 
    # Construct the SQL query based on form data
    query = "SELECT * FROM vcf WHERE AF > " + str(allele_freq)

    yquery = ""
    yquery = "SELECT * FROM "
    for i in year:
        yquery += i + " JOIN "
    yquery = yquery[:-5]

    query += "WHERE ln_ecological_vol > " + str(ln_ecological_vol) + " "


    if len(location) > 0:
        yquery += "AND "
        for i in location:
            yquery += "location = " + "'" + i + "'" + " OR "
        yquery = yquery[:-3]


    if len(mortality) > 0:
        yquery += "AND "
        for i in mortality:
            print(i)
            yquery += "mortality = " + "'" + i + "'" + " OR "
            yquery = yquery[:-3]





    if allele_freq:
        query += f"AF <= {allele_freq}"

    try:
        # Execute the query
        results = execute_query(cursor, query)

        if results:
            # Generate HTML table for query results
            vcf_table_template = Template(
            """
            <table>
            <thead>
            <tr>
            <th>CORAL_ID</th><th>BAM_ID</th><th>CHROM</th><th>POS</th><th>ID</th><th>REF</th><th>ALT</th><th>QUAL</th><th>FILTER</th><th>NS</th><th>INFO_DP</th><th>AF</th><th>GT</th><th>FORMAT_DP</th><th>GL</th><th>PL</th><th>GP</th>
            </tr>
            </thead>
            <tbody>
            ${table_rows}
            </tbody>
            </table>
            """
            )
            table_rows = ""
            for row in results:
                table_rows += """
                <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                </tr>
                """ % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])
            vcf_table = vcf_table_template.safe_substitute(table_rows=table_rows)
        else:
            error_message = '<p style="color:red;">No data found for applied filters</p>'
    except pymysql.Error as e:
        error_message = f'<p style="color:red;">Error executing query: {e}</p>'

cursor.close()
connection.close()

# Print content type
print("Content-type: text/html\n")

# Print HTML content including query results
print(vcf_table)
