""" rank webpage"""

def make_list(input_list):
    """ makes page and query list from input list"""
    listofP, listofQ = [], []
    for each in input_list:
        if each[0] == "P":
            listofP.append(each.split("P")[1])
        else:
            listofQ.append(each.split("Q")[1])
    return listofP , listofQ 

def make_dict(input_list):
    """ make dict from input list """
    page_list = []
    for each in input_list:
        each = dict([(item, (8 - index)) for index, item in enumerate(each.split(), start=0)])
        page_list.append(each)
    return page_list

def find_strength(q_dict, page_dict):
    """ calculate the strength of keywords"""
    strength_list = []
    for each in page_dict:
        keywords = list(set(q_dict.keys()).intersection(each.keys()))
        if keywords:
            value = [q_dict[i] * each[i] for i in keywords]
            strength_list.append(reduce(lambda q, p: p+q, value))
        else:
            strength_list.append(0)
    return strength_list

def order_page(strength_list):
    """Order the pages """
    page_list = []
    counter = 1
    for _ in strength_list:
        page_list.append("P"+str(counter))
        counter += 1
    value_dict = dict(zip(page_list, strength_list))
    orderedpage_list = [w for w in sorted(value_dict, key=value_dict.get, reverse=True)][0:5]
    return orderedpage_list


def main():
    """Get the webpage and query list from user"""
    input_list = []
    while True:
        line = raw_input(">")
        if line == "":
            break
        else:
            input_list.append(line)
    listofP, listofQ = make_list(input_list)
    page_dict, query_dict = make_dict(listofP), make_dict(listofQ)
    counter = 1
    for q_dict in query_dict:
        strength_list = find_strength(q_dict, page_dict)
        ordered_page_list = order_page(strength_list)
        print "Q" + str(counter)+ ":" + " ".join(ordered_page_list)
        counter += 1

if __name__ == "__main__":
    main()
