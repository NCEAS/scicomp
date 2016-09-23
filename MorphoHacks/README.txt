Creator: Justin Kroes
Email: jkroes14@ucsbalum.com
orcID: orcid.org/0000-0003-3257-2321

Scripts:

	MainScript.R:

		The script with which users should interact. Sources 
		the second script, WriteUniqueFieldValues.R.

	WriteUniqueFieldValues.R:

		Loads the magrittr package and defines the function 
		that is this script’s namesake. The only reason to 			
		interact with this script is in the case of errors, 
		likely due to three possible problems: non-Mac
		platforms for which this script was not tested, older 
		versions of R (I used v3.3.1), or a different version 
		of the magrittr package (I use v1.5). 

MainScript.R Instructions:

	1. Change the path variables within the section entitled 
	“User-dependent variables”. Make sure to use absolute paths, 
	as specified in the comments in this section. Omit the trailing 
	separator (“/” for Mac OS X and “\\” for Windows). Surround
	the path with quotation marks. For example:

	“/Users/justin/Desktop/MorphoScript”

	2. Within the same script, choose whether to specify a 
	character value for custom_code, which designates any user-
	defined values for missing data. Otherwise, ignore the 
	variable.

	3. Source WriteUniqueFieldValues.R 

	4. Look for files named after your dataset’s field names. Any 
	junk columns will be named “X”, “X.1”, X.2”, and so on. If 
	your data is organized with variables as column headers and 
	subsequent rows representing values for each variable, and if 
	your data columns are contiguous, then “X” represents the
	first column after your last legitimate data column.

	5. Clear the contents of any junk “columns” you observe.
	(Your data may not be organized as described in step 4, so it 
	may take some observation to figure out what part of your 
	data is junk). 

Purpose of scripts:

	Many applications—Morpho and R included—will 
	read in junk “columns” if any column outside of the data has 
	any kind of user input. This includes white space. It is 
	often hard to spot these columns until they are read into an 
	application. I like to use Morpho’s Data Wizard’s automatic 
	data entry feature when inputting new data tables into a data 
	package. The problem is that Morpho will force you to input 
	metadata for these junk columns—I often have up to 20 of 
	these at a time—or 
	else quit the process and start over after deleting the junk 
	columns. This can hugely increase the time you have to spend 
	in Morpho, and nobody wants that. Another issue with Morpho 
	is that Morpho can’t parse really large datasets. 
        
	Normally the wizard will identify unique values within a data 
	field (i.e. a column in a .csv file, in my case), but failing 
	to parse the data means that it won’t identify every unique 
	value. For certain data types, you want to define your
	field’s values. There’s no way to look up the missing values 
	in Morpho. 
        
	Related to this is trying to determine the type of any
	numeric data you have (whole, natural, integer, or real). You 
	want to be able to sort all of these values to see whether 
	your data includes zeros, negative numbers, and/or fractions 
	and decimals. If the data isn’t parsed fully, there’s no way 
	to know for sure.

	Finally, the way Morpho sorts data isn’t helpful for 
	determining whether you have any missing values and what 
	their code may be (“NA”, a blank cell, etc.). 
        
        Running these scripts prior to using Morpho will allow you 
	to more easily identify junk columns (see “MainScript.R 
	Instructions”, above), to identify the type of any numeric 
	data, and to identify what kinds of codes in your data
	indicate missing values.
