import re
import os


my_path = ""
my_text_file = os.path.join(my_path, "text_test.txt")
my_reference_file = os.path.join(my_path, "references_test.txt")


# searches the text for a citation with a single author
one_author_txt = re.compile("""([A-Za-z]+)        # last name first author as group1
                            .?                    # zero or one commas                                                
                            \s+                   # any whitespace
                            .?                    # zero or one parentheses                           
                            ([0-9]{4}[a-z]?)      # date as group2""", re.X)

# searches the text for a citation with multiple authors
multiple_authors_txt = re.compile("""([A-Za-z]+)  # first author as group1
                            [,]?                  # optional comma
                            \s+                   # whitespace
                            (&|and)               # joins both authors as group2
                            \s+                   # optional whitespace
                            ([A-Za-z]+)           # second author as group3
                            [,]?                  # optional comma
                            \s+                   # whitespace
                            [(]?                  # optional parenthesis
                            ([0-9]{4}[a-z]?)      # date as group4""", re.X)

# searches the references for an entry with a single author                   
one_author_refs = re.compile("""^([A-Za-z]+)       # last name first author as group1                                                
                            .+                     # any other names and symbols                               
                            [(]                    # opening brace for date
                            ([0-9]{4}[a-z]?)       # date as group2
                            [)]                    # closing brace for date""", re.X)

# searches the references for an entry with more than one author
two_authors_refs = re.compile("""^([A-Za-z]+) # first author
                            .+                     # any other names and symbols
                            \s+                    # one or more whitespaces
                            ([A-Za-z]{2,})[.]      # second author as group2
                            \s+                    # one or more whitespaces
                            [(]                    # opening brace for date
                            ([0-9]{4}[a-z]?)       # date as group3
                            [)]                    # closing brace for date""", re.X)

# searches the references for an entry with more than two authors
multiple_authors_refs = re.compile("""^.+          # any characters
                            \s+                    # whitespace
                            ([A-Za-z]{2,})         # second to last author as group2
                            .?                     # optional comma
                            \s+                    # whitespace
                            (&|and)                # joins both authors as group2
                            .+                     # any characters
                            \s+                    # whitespace
                            ([A-Za-z]{2,})         # last author as group2
                            .?                     # optional period
                            \s+                    # optional whitespace
                            [(]                    # optional parenthesis                            
                            ([0-9]{4}[a-z]?)       # date as group3""", re.X)

# searches the references for entries that otherwise can't be matched
misc_pattern_refs = re.compile("""^(.+)            # anything as group1
                            [(]                    # opening brace for date
                            ([0-9]{4}[a-z]?)       # date as group2
                            [)]                    # closing brace for date""", re.X)


def has_pattern(pattern, text):
    """Return True if a pattern is found on a line."""
    return re.search(pattern, text)

def has_one_citation(citation):
    """Return True if an in-text citation only references one work."""
    return len(citation) == 1

def get_author_txt(pattern, text):
    """Return all in-text citations that have a single author from a given line."""
    output = re.findall(pattern, text)
    return output

def get_many_authors_txt(pattern, text):
    """Return all in-text citations that have multiple authors from a given line."""
    output = re.findall(pattern, text)
    authors = [output[0][0], output[0][2]]
    year = output[0][3]
    return [' '.join(authors), year] 

def append_one(citation, citation_list):
    """Append in-text citations with a single author to a reference list."""
    author = citation[0][0]
    year = citation[0][1]
    new_entry = [author, year]
    citation_list.append(new_entry)
    return citation_list

def append_many(citation, citation_list):
    """Append in-text citations with multiple authors to a reference list."""
    idx = -1
    for each in citation:                        
        idx += 1                        
        author = citation[idx][0]
        year = citation[idx][1]
        new_entry = [author, year]
        citation_list.append(new_entry)
    return citation_list

def add_author(citation, citation_list):
    """Check to see if an index in the reference list has multiple single
    author citations.  If so, append each one individually to the list."""
    if has_one_citation(citation):
        append_one(citation, citation_list)
    else:
        append_many(citation, citation_list)
    return citation_list

def create_text_references(citation_list):
    """Create a citation list of all in-text citations from the text
    document."""
    with open(my_text_file, "rb") as my_document:        
        for line in my_document.readlines():
            if has_pattern(multiple_authors_txt, line):
                entry = get_many_authors_txt(multiple_authors_txt, line)
                citation_list.append(entry)
            elif has_pattern(one_author_txt, line):
                entry = get_author_txt(one_author_txt, line)
                add_author(entry, citation_list)
    return citation_list

def get_author_refs(pattern, text):
    """Return the citation information from the references page for a work 
    with a single author."""
    output = re.search(pattern, text)
    return [output.group(1), output.group(2)] 

def get_two_authors_refs(pattern, text):
    """Returns the citation information from the references page for a work 
    with two authors."""
    output = re.search(pattern, text)
    authors = [output.group(1), output.group(2)]                              
    return [' '.join(authors), output.group(3)]    

def get_multiple_authors_refs(pattern, text):
    """Returns the citation information from the references page for a work 
    with multiple authors."""
    output = re.search(pattern, text)
    authors = [output.group(1), output.group(3)]                              
    return [' '.join(authors), output.group(4)] 

def create_refpage_references(reference_list):
    """Create a references list for all works found in the references page."""
    with open(my_reference_file, "rb") as my_document:        
        for line in my_document.readlines():
            if has_pattern(multiple_authors_refs, line):
                entry = get_multiple_authors_refs(multiple_authors_refs, line)
                reference_list.append(entry)
            elif has_pattern(two_authors_refs, line):
                entry = get_two_authors_refs(two_authors_refs, line)
                reference_list.append(entry)
            elif has_pattern(one_author_refs, line):
                entry = get_author_refs(one_author_refs, line)
                reference_list.append(entry)
            elif has_pattern(misc_pattern_refs, line):
                entry = get_author_refs(misc_pattern_refs, line)                
                reference_list.append(entry)
    return reference_list

def fill_incomplete(reference_list):
    """Search the references page reference list for ommitted author
    names.  Fill in the ommitted names based on the previous author in the 
    list."""
    idx = -1
    for entry in reference_list:
        idx += 1
        if not entry[0][0].isalpha():
            entry[0] = reference_list[idx-1][0]
    return reference_list

def print_references(reference_list):
    """Print each entry from a references list."""
    for entry in reference_list:
        print entry

def references_not_in_text(reference_list, citation_list):
    """Print all references from the reference page that are not cited
    in the text."""
    reference_not_in_text = ([reference for reference in reference_list
                              if reference not in citation_list])    
    if len(reference_not_in_text) > 0: 
        print "These references are not cited in the text: \n"       
        for reference in reference_not_in_text:
            print reference[0], reference[1]
        print
    else:
        print "All references are cited in the text. \n"

def citations_not_in_refs(reference_list, citation_list):
    """Print all citations from the text if they are ont found 
    in the references page."""
    citation_not_in_refs = ([citation for citation in citation_list
                             if citation not in reference_list])    
    if len(citation_not_in_refs) > 0:
        print "These in-text citations are not in the references page: \n"
        for citation in citation_not_in_refs:
            print citation[0], citation[1]
        print
    else:
        print "All in-text citations are also in the references page. \n"

def cross_check_references():
    text_references = []
    refpage_references = []
    create_text_references(text_references)
    create_refpage_references(refpage_references)
    fill_incomplete(refpage_references)
    references_not_in_text(refpage_references, text_references)
    citations_not_in_refs(refpage_references, text_references)

cross_check_references()