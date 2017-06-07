# DATA WRANGLING USING PYTHON

### Brief Description
A region of interest from Open street Maps has been chosen-Vidyaranyapura,Bangalore   is initially cleaned and the data  available in OSM format has been extracted and converted to CSV for further analysis.Since the original file is bigger a sample file of the region (sample_Vpura.osm) is uploaded for testing the same.

### Order of Execution for the files
<ol>
<li>tagcount.py - To find the count of higher level tags in the OSM file like the nodes,ways,tags </li>
<li>Keyproblem.py -To identify problem characters(defined by 'problemchars') in the attribute values and to write the corrected output in a different file for further processing </li>
<li>streetname_audit.py - extract the street names and check if they conform to an expected standard else making the necessary correction</li>
<li>Pincode_audit.py - Correction of pincode for value and for additional charcters</li>
<li>OSM2CSV.py - (Python 2.7 used) -creation of relevant csv files(nodes,nodes_tags,ways,ways_tags,nodes_ways) from OSM </li>
<li>query.py - using SQL queries to access details from the database</li>
</ol>

<p>Note:After the CSV files are generated using OSM2CSV the files are placed into a database, in this case Vidyaranyapura.db using sqlite3 and then used in query.py
</p>

#### STEPS between 5 and 6:
<li>In windows open cmd and navigate to the folder where the database should be created.The sqlite3 application is to be present in the same folder.Syntax below for creating the db</li>
`sqlite3 Vidyaranyapura.db` 
<li>Relevant tables are created using the schema provided using the CREATE command</li>
<li>Values are inserted into the appropriate tables using the INSERT INTO command </li>
