This is a reference checker that I created to help ensure that all in-text citations in my dissertation also appear on the references page and vice-versa.  It uses regular expressions to search for the relevant information.

In order to use the reference checker, you will need two plain text files.  The first file is the actual paper, article, dissertation, etc. and the second file is the references page.

Make sure that 'my_path' on line 5 points the the directory for these two files.

'my_text_file' and 'my_reference_file' (on lines 6 and 7) should contain the names of your document and reference files, respectively.

You can test the program with the included 'text_test.txt' and 'references_test.txt' files.  

The program largely works, but there are some issues I have encountered when running the program with other files.  These include:
- Doesn't correct possessive citations (e.g., Robinson's (2001)...)
- Pulls last name and first name if full first name is given in references
   	e.g., Lombardi, Linda. (1990).  
	(note: this pattern deviates from the APA standard)
- Does not parse author's name in the refernce section if two initials are given
	e.g., Clements, G.N. & E.Hume. (1995).

Tightening up the regular expressions should correct these issues.  This is my current to-do with the reference checker.