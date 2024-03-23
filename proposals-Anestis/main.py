import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os


"""
Creates and returns a list that contains 1's with the size 'size' that is given as input.
"""


def create_list_of_ones(size):
    list_of_ones = []
    for _ in range(size):
        list_of_ones.append(1)
    return list_of_ones


"""
   Takes two inputs, a list of strings (list_of_sentences) and a list of numbers (num_of_words).Each number in the 
   list of numbers corresponds to the string in the list of strings that has the same index and indicates how many words
   we want to take from the start of that string. For example assuming that the list of numbers is the following:
   [2,1,1] means that from the first string we will take the first 2 words, from the second and third string we will
   take the first word. The function creates and returns a list (temp_list) with the desired words taken from each
   string following the principle of the index that was mentioned before (temp_list[0] contains the words taken from
   list_of_sentences[0] etc.).
"""


def take_first_words(list_of_sentences, num_of_words):
    temp_list = []
    for num_of_sentence, sentence in enumerate(list_of_sentences):
        temp_string = ''
        words = sentence.split()
        for i in range(int(num_of_words[num_of_sentence])):
            temp_string = temp_string + words[i] + ' '
        temp_string = temp_string.strip()
        temp_list.append(temp_string)
    return temp_list                           # list of words


"""
   Takes two inputs, a list of strings (list_of_sentences) and a list of numbers (num_of_words_taken).Each number in the 
   list of numbers corresponds to the string in the list of strings that has the same index and indicates how many words
   we have taken from the start of that string. For example assuming that the list of numbers is the following:
   [2,1,1] means that from the first string we have taken the first 2 words, from the second and third string we have
   taken the first word. The function creates and returns a list (temp_list) with all the words that were not taken
   from each string following the principle of the index that was mentioned before (temp_list[0] contains the words not
   taken from the list_of_sentences[0] etc.).
"""


def take_remaining(list_of_sentences, num_of_words_taken):
    temp_list = []
    for num_of_sentence, sentence in enumerate(list_of_sentences):
        temp_string = ''
        words = sentence.split()
        for i in range(int(num_of_words_taken[num_of_sentence]), len(words)):
            temp_string = temp_string + words[i] + ' '
        temp_string = temp_string.strip()
        temp_list.append(temp_string)
    return temp_list                           # list of words


df = pd.read_excel('./data/data.xlsx')
num_of_files = len(df)                              # num_of_files to be generated
data = df.to_dict()

environment = Environment(loader=FileSystemLoader('templates/'), variable_start_string="{jnj", variable_end_string="jnj}")
template = environment.get_template('latex_template.txt')

for file in range(num_of_files):
    file_data_dict = {                                              # will be given as input in the .render() method
        'committee_id': data['committeeID'][file],
        'name_of_committee': data['committeeName'][file],
        'name_of_topic': data['topicName'][file],
        'speaker_country': data['speakerCountry'][file],
        'supporters': data['supporters'][file].split(', '),
        'based_on': data['basedOn'][file].split('$ '),
        'proposals': data['proposals'][file].split('$ '),
        'bold_words_on_proposals': data['boldWordsOnProposals'][file].split(', '),
    }

    # bases
    first_word_of_bases = take_first_words(file_data_dict['based_on'], create_list_of_ones(len(file_data_dict['based_on'])))
    remaining_bases = take_remaining(file_data_dict['based_on'], create_list_of_ones(len(file_data_dict['based_on'])))
    zipped_data_bases = zip(first_word_of_bases, remaining_bases)

    # proposals
    first_word_of_proposals = take_first_words(file_data_dict['proposals'], file_data_dict['bold_words_on_proposals'])
    remaining_proposals = take_remaining(file_data_dict['proposals'], file_data_dict['bold_words_on_proposals'])
    zipped_data_proposals = zip(first_word_of_proposals, remaining_proposals)

    content = template.render(
        file_data_dict,
        supporters=file_data_dict['supporters'],
        zipped_bases=zipped_data_bases,
        zipped_proposals=zipped_data_proposals,
    )

    filename = str(file_data_dict['committee_id']) + ') ' + file_data_dict['name_of_topic'] + '-ΓΝΩΜΗ'
    output_directory = './outputs/'
    filepath = os.path.join(output_directory, filename)
    with open(filepath, mode="w", encoding="utf-8") as temp_file:
        temp_file.write(content)
        print(f"... wrote {filename}")
























