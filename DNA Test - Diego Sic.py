#Diego Sic
#Project 2 - DNA Identification
# This program will use a data base to check DNA sequence matches. 

def breaking_data_base(Doc):
    '''This function will break the lines of a document,
    and separate the elements using "," as the parameter.
    Each line will be saved in a list, and all llines will be
    saved in individual lists.
    Parameter:
        A document cvs with names, DNA-Type, and quanity of DNA-Type
    Return:
        A list with each line of the data base in a list'''
    List_with_good_elem = []
    for line in Doc:
        List_with_good_elem.append((line.strip()).split(","))
    return List_with_good_elem
    
def ordering_elem(list_with_good_elem):
    '''This function is going to re-order the data base
    creating 3 lists with and save them in another list
    The list will storage the name of the person, and how
    many quantities of DNA-type it has
    Parameter:
        A list separated by lines
    Return
        A list with lists with the format:
        [DNA-type,Quantity, DNA-type,Quantity, DNA-type,Quantity , Name]'''
    multiply_elem = []
    i_range = len(list_with_good_elem[0])
        
    for i in range(i_range-1):
        elem_to_compare = list_with_good_elem[0]
        elem_to_work = list_with_good_elem[i+1]
        temp_list = []
        j_range = len(elem_to_work)
        
        for j in range(j_range-1):
            temp_list.append(elem_to_compare[j+1])
            temp_list.append(elem_to_work[j+1])
            
        temp_list.insert(len(temp_list),elem_to_work[0])
        temp_list.insert(len(temp_list)-1,elem_to_compare[0])
        multiply_elem.append(temp_list) 
    return multiply_elem

def check_sequence(lines_2, str_to_check):
    '''This function will count how many consecutives matches
    a sequence of DNA has with the DNA-type, and return the max
    amount of times a DNA type it's repeated
    parameter:
        A string with the DNA sequence, and the String in the
        data base we're checking
    Return:
        An integer describing the  max amount of times a DNA 
        type it's repeated'''
    counter = 0
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
            
    return max(list_of_counters)

def check_data_base(list_with_order_elem, lines_2):
    '''This function will check the number of matches a
    sequence has with the information in the data base
    if everything matches returns the name of the person 
    in the data base
    parameter:
        A list with the information of all the candidates in
        the data base
    return:
        A string with the name of the candidate who matches or
        "no matches" if there's no matches'''  
    name_of_person = "No match"
    for i in range(len(list_with_order_elem)):
        l_person_to_check = list_with_order_elem[i]
        num_of_matches = 0
        
        for j in range(0, len(l_person_to_check)-2,2):
            dna_coincidences = check_sequence(lines_2, l_person_to_check[j])
            if (j +1 < len(l_person_to_check)
                and int(dna_coincidences) == int(l_person_to_check[j+1])):
                num_of_matches +=1          
        if num_of_matches == 3:
            name_of_person = l_person_to_check[len(l_person_to_check)-1]
            return name_of_person

    return name_of_person
    
def main():
    #Open the document
    Doc_name = ""
    Doc = open("Data_base.txt", "r")    
    list_with_good_elem = breaking_data_base(Doc)
    #Ordering the data in something a list with the format:
    #[[type, quantity],[type, quantity],[type, quantity], Name]
    list_with_order_elem = ordering_elem(list_with_good_elem)

    sequence = open("sequence1.txt", "r")
    lines_2 = sequence.read()
    name_coincidence = check_data_base(list_with_order_elem, lines_2)
    print(name_coincidence)

    sequence = open("sequence2.txt", "r")
    lines_2 = sequence.read()
    name_coincidence = check_data_base(list_with_order_elem, lines_2)
    print(name_coincidence)
    
    sequence = open("sequence3.txt", "r")
    lines_2 = sequence.read()
    name_coincidence = check_data_base(list_with_order_elem, lines_2)
    print(name_coincidence)
    
    sequence = open("sequence4.txt", "r")
    lines_2 = sequence.read()
    name_coincidence = check_data_base(list_with_order_elem, lines_2)
    print(name_coincidence)


if __name__ == "__main__":
    main()

