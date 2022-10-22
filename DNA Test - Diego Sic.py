#Diego Sic
#Project 2 - DNA Identification
# This program will use a data base to c

def breaking_data_base(Doc):
    '''This function will break the lines of a document,
    and separate the elements using "," as the parameter.
    Each line will be saved in a list, and all llines will be
    saved in individual lists.
    Parameter:
        A document cvs'''
    List_with_good_elem = []
    for line in Doc:
        List_with_good_elem.append((line.strip()).split(","))
    return List_with_good_elem
    
def ordering_elem(list_with_good_elem):
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

