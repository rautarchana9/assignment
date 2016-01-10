""" Rank Webpage"""

def make_list(input_list):
    """ makes page and query list from user input list"""
    p_list, q_list = [], []
    for each in input_list:
        if each[0] == "P":
            p_list.append(each.split("P")[1])
        else:
            q_list.append(each.split("Q")[1])
    return p_list, q_list

def make_dict(input_list):
    """ maps the keywords to weights for a given page or query list """
    output_list = []
    for each in input_list:
        each = dict([(item, (8 - index)) for index, item in enumerate(each.split(), start=0)])
        output_list.append(each)
    return output_list

def find_strength(q_dict, page_dict):
    """ calculates the strength of all pages for given query """
    page_value_list = []
    for each in page_dict:
        common_keywords = list(set(q_dict.keys()).intersection(each.keys()))
        if common_keywords:
            value = [q_dict[i] * each[i] for i in common_keywords]
            page_value_list.append(reduce(lambda q, p: p+q, value))
        else:
            page_value_list.append(0)
    return page_value_list

def sort_page_list(page_value_list):
    """ sorts the pages according to their strengths
        zero strength pages not included, pages having same strength are ranked
        according to decreasing page number """
    page_list = []
    counter = 1
    for _ in page_value_list:
        page_list.append("P"+str(counter))
        counter += 1
    page_value_dict = dict(zip(page_list, page_value_list))
    page_value_dict = {k:v for k, v in page_value_dict.items() if v != 0}
    orderedpage_list = [w for w in sorted(page_value_dict, key=page_value_dict.get, reverse=True)][0:5]
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
    p_list, q_list = make_list(input_list)
    page_dict, query_dict = make_dict(p_list), make_dict(q_list)
    counter = 1
    for q_dict in query_dict:
        page_value_list = find_strength(q_dict, page_dict)
        ordered_page_list = sort_page_list(page_value_list)
        print "Q" + str(counter)+ ":" + " ".join(ordered_page_list)
        counter += 1

if __name__ == "__main__":
    main()
