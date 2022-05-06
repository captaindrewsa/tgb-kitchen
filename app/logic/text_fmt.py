'''
TODO: Сделать потом функции форматирования текста
'''

def recype_fmt(data:list):
    data_for_one_mess = ""
    for elem in data:
        data_for_one_mess = "{0}. {1}. ".format(elem[0],elem[1])
        data_for_one_mess += (elem[2]*'\U00002B50')+'\n'
        data_for_one_mess += elem[3]
        return data_for_one_mess

