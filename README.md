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

License

Copyright (c) 2014 Justin Glover

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.