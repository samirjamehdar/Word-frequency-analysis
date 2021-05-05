# Samir Jamehdar 
# Word frequency analysis from a .txt file



import math


def read_file_to_freq_dict(filename):
    """
    Returns a dictionary with words and their occurrences from a text file.
    """


    file_open = open(f'{filename}.txt', 'r')
    infile = file_open.read()
    file_open.close()

    replace_newlines = infile.replace('\n', ' ')
    infile_list = replace_newlines.split(' ') 

    histogram_dict = {}

    for word in infile_list:
        if word == '':
            pass
        else:
            if word in histogram_dict:
                histogram_dict[word] += 1
            else:
                histogram_dict[word] = 1

    return histogram_dict


def ten_most_common(dictionary):
    """
    Finds the 10 highest values in a dictionary.
    Returns a list for the highest keys and another list for the highest value.
    The key:value lists are descending and have matching indexes.
    """

    histogram_dict = dictionary.copy()
    key_lst = []
    value_lst = []

    if len(histogram_dict) > 10:
        while len(key_lst) < 10:
            max_key = max(histogram_dict, key = histogram_dict.get)
            key_lst.append(max_key)
            value_lst.append(histogram_dict[max_key])
            histogram_dict.pop(max_key)

    else:
        while len(histogram_dict) != 0:
            max_key = max(histogram_dict, key = histogram_dict.get)
            key_lst.append(max_key)
            value_lst.append(histogram_dict[max_key])
            histogram_dict.pop(max_key)

    return key_lst, value_lst    


def total_amount_of_words(dictionary):
    """
    Returns the total amount of words from a dictionary.
    """


    histogram_dict = dictionary.copy()
    total_amount = 0

    for i in histogram_dict:
        total_amount += histogram_dict[i]

    return total_amount


def average(dictionary, total_word_amount):
    '''
    Returns the average word frequency and the words
    with that frequency
    '''


    all_words = total_word_amount
    unique_words = len(dictionary)
    histogram_dict = dictionary.copy()

    avg_word_freq = all_words / unique_words
    avg_word_freq = round(avg_word_freq)
 
    prox_dict = {}
    avg_words_lst = []
    

    for word in histogram_dict:
        prox_dict[word] = abs(histogram_dict[word] - avg_word_freq)

        if len(avg_words_lst) == 0:
            avg_words_lst.append(word) 

    # Proximity values/words if no word from dict matches the average word frequency.
        else:
            prox_val = abs(avg_word_freq - avg_word_freq)

            if prox_dict[word] < prox_val:
                avg_words_lst.clear()
                avg_words_lst.append(word)
            elif prox_dict[word] == prox_val:
                avg_words_lst.append(word)



    return avg_word_freq, avg_words_lst


def dict_median(dictionary):
    """
    Returns the median value and a list of the
    words with that value from a dictionary.
    """

    histogram_dict = dictionary.copy()
    histo_len = len(histogram_dict)

    value_lst = []
    prox_dict = {}
    median_words_lst = []


    for i in histogram_dict:
        value_lst.append(histogram_dict[i])

    value_lst.sort()
    residual = histo_len % 2


    if residual != 0:
        median_index = int((histo_len / 2) - 0.5)
        median = value_lst[median_index]
    else:
        left_half = int((histo_len / 2) - 1)
        right_half = int((histo_len / 2))
        median = (value_lst[left_half] + value_lst[right_half]) / 2


    # Proximity values/words if no words matches the median value.
    for word in dictionary:
        prox_dict[word] = abs(histogram_dict[word] - median)
        if len(median_words_lst) == 0:
            median_words_lst.append(word)
        else:
            prox_val = abs(histogram_dict[median_words_lst[0]] - median)

            if prox_dict[word] < prox_val:
                median_words_lst.clear()
                median_words_lst.append(word)
            elif prox_dict[word] == prox_val:
                median_words_lst.append(word)

    return round(median), median_words_lst


def write_outfile(
    filename,
    dictionary,
    total_word_amount,
    ten_most_common_key_list,
    ten_most_common_value_list,
    average_word_freq,
    average_word_list,
    median,
    median_words_list
    ):

    """
    Writes a new textfile
    """


    # Defining variables, shortening the names slightly
    histogram_dict = dictionary.copy() #dictionary
    ten_key_lst = ten_most_common_key_list
    ten_value_lst = ten_most_common_value_list 
    total_words = total_word_amount
    unique_words = len(histogram_dict)
    avg_word_freq = average_word_freq
    avg_words_lst = average_word_list

    # Börjar skriva på nya filen
    outfile = open(f'{filename}_report.txt', 'x')   # x - Will create a file, returns an error if the file exist.
    
    outfile.write(f'\nFilen {filename}.txt innehåller {total_words} ord varav {unique_words} är olika. \n\n\n')
    

    # 10 most common words
    outfile.write('De vanligaste orden är\n\n\nOrd\t\t\t\t\tAntal förekomster\n')
    outfile.write('-'*38 + '\n')
    
    for i in range(0, len(ten_key_lst)):
        outfile.write(ten_key_lst[i])
        space_length = 25 - len(ten_key_lst[i])
        outfile.write(' ' * space_length)
        outfile.write(f'{ten_value_lst[i]}\n')

    outfile.write('-'*87 + '\n')


    # Average words
    outfile.write(f'Medelordfrekvensen i texten är {avg_word_freq}, och den frekvensen har orden:\n')

    for j in range(0, len(avg_words_lst)):
        if j % 4 == 0 and j != 0:
            outfile.write('\n')
        
        outfile.write(avg_words_lst[j])
        space_lenght2 = 25 - len(avg_words_lst[j])
        outfile.write(' '*space_lenght2)



    # Median words
    outfile.write('\n' + '-'*87 + '\n')
    outfile.write(f'Medianordfrekvensen i texten är {median}, och den frekvensen har orden:\n')

    for k in range(0, len(median_words_list)):
        if k % 4 == 0 and k != 0: # ändrar till fyra
            outfile.write('\n')
        
        outfile.write(median_words_list[k])
        space_lenght3 = 25 - len(median_words_list[k])

        outfile.write(' '*space_lenght3)
    
    outfile.write('\n' + '-'*87 + '\n')


    highest_prop =  round((ten_value_lst[0] / total_word_amount) * 100, 2)


    outfile.write(f'Det vanligaste ordet är {ten_key_lst[0]}, och det utgör {highest_prop} av hela texten ')


def main():


    analyze = False

    while not analyze:
        ok = False

        while not ok:
            filename = input('Enter the name of a textfile (do not include .txt): ')
            try:
                histogram_dict = read_file_to_freq_dict(filename).copy()
            except FileNotFoundError:
                print('File does not exist, please try again!\n')
            else:
                # Kollar om textfilen är tom
                if len(histogram_dict) == 0:
                    print('Textfile is empty, please try again\n')
                else:
                    ok = True


        # Defining variables
        ten_key_lst, ten_value_lst = ten_most_common(histogram_dict)
        ttl_words = total_amount_of_words(histogram_dict)
        avg_word_freq, avg_words_lst = average(histogram_dict, ttl_words)
        median, median_words_list = dict_median(histogram_dict)



        # Try/except i detta fallet ger try again och filen redan finns, överskriver aldrig tack vare x i open('...', x)
        try:
            write_outfile(
                filename,
                histogram_dict,
                ttl_words,
                ten_key_lst,
                ten_value_lst,
                avg_word_freq,
                avg_words_lst,
                median,
                median_words_list)

        except FileExistsError:
            print(f'File {filename}_report.txt already exists, try again!\n')
            ok = False
        else:
            analyze = True

    return print('Analysis Successful!\n')


main()
