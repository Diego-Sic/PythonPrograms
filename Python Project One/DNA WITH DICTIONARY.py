#Diego Sic
#Project 2 - DNA Identification

from optparse import Values
from tabnanny import check
from unicodedata import name


def breaking_data_base_in_dic(Doc):
    '''This function will break the lines of a document,
    and separate the elements using "," as the parameter.
    Each line will be saved in a list, and all llines will be
    saved in individual lists.
    Parameter:
        A document cvs
    Return:
        A dictonary with all the first columns as keys
        and the values are the rest of the values in the line of the
        respective key '''
    List_with_good_elem = []
    for line in Doc:
        List_with_good_elem.append((line.strip()).split(","))
  
    d = {}
    for elem in List_with_good_elem:
        d[elem[0]] = elem[1:]
    return d

def check_sequence(lines_2, d):
    '''This function will use a dictionary
    to determine the quantity of times a DNA
    type appers in a sequence storaged in a list.
    Parameter:
        A string describing a DNA sequence(lines_2)
        a dictionary with the names and DNA types
    Return:
        A list describing how many the DNA types
        apper'''
    counter = 0  
    results = []
    l_keys = list(d.keys())
    
    for str_to_check in d[l_keys[0]]:
        list_of_counters = []
        for i in range(len(lines_2)):
            variable_to_check = lines_2[i:i+4]
            if variable_to_check == str(str_to_check):
                counter += 1
                for j in range(i+4,len(lines_2),4):       
                    if lines_2[j:j+4] == variable_to_check:
                        counter += 1
                list_of_counters.append(counter)
                counter = 0    
        results.append(max(list_of_counters))
    return results

def check_data_base(d, lines_2):
    '''This function will check if the results of the function
    "check sequence" matches with the data in the dictionary
    Parameter:
        A string describing a DNA sequence(lines_2)
        a dictionary with the names and DNA types
    Return:
        A string with the name of the match if exist
        otherwise will return "no match"'''
    name = "No match"
    l_keys = list(d.keys())
    results = check_sequence(lines_2, d)

    for key in l_keys:
        if key != l_keys[0]:
            for i in range(len(d[key])):
                list_to_work = d[key]
                list_to_work[i] = int(list_to_work[i])
            if d[key] == results:
                name = key       
    return name

def main():
    #Open the document
    Doc = open("Data_base.txt", "r")
    dictionary = breaking_data_base_in_dic(Doc)  
    Doc.close()

    sequence = open("sequence1.txt", "r")
    lines_0 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_0)
    print(name_coincidence)

    sequence = open("sequence2.txt", "r")
    lines_1 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_1)
    print(name_coincidence)
    
    sequence = open("sequence3.txt", "r")
    lines_2 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_2)
    print(name_coincidence)
    
    sequence = open("sequence4.txt", "r")
    lines_3 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_3)
    print(name_coincidence)

if __name__ == "__main__":
    main()

