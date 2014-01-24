Reference checker
=========

Written in Python 2.7.6.

This is a reference checker that I created to help ensure that all in-text citations in my dissertation also appear on the references page and vice-versa.  It uses regular expressions to search for the relevant information.

In order to use the reference checker, you will need two plain text files.  The first file is the actual paper, article, dissertation, etc. and the second file is the references page.

Make sure that 'my_path' on line 5 points the the directory for these two files.

'my_text_file' and 'my_reference_file' (on lines 6 and 7) should contain the names of your document and reference files, respectively.

You can test the program with the included 'text_test.txt' and 'references_test.txt' files.  

The program largely works, but there is one outstanding issue that I am aware of.  Based on the way that the in-text search function is written, the checker will not find a citation with a single author if it occurs on the same line as a citation with multiple authors.  So, if this situation occurs, and the single author citation is the only citation for that author in the text, the checker will erronously believe that this particular author is not cited in the text.  The function create_text_references(citation_list) needs to be re-written to address this.

Tightening up the regular expressions should correct these issues.  This is my current to-do with the reference checker.

License
=========

Copyright (c) 2014 Justin Glover

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
