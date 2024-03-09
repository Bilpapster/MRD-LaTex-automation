import numpy as np
import pandas as pd
from collections import OrderedDict
import jinja2


def numerize_award_name(df):
    """
    Replaces the values of the awards column in a dataframe, specifically:
    'best_delegate' with 1, 'future_diplomat' with 2 and 'citation' with 3.
    To be used in the read_input_file function.

    :param df: the dataframe which contains an awards column with values 
        from the set {'best_delegate',, 'future_diplomat', 'citation'}
    :return: the resulting dataframe
    """
    column = 'AwardName'

    for i in df.index:
        award = df[column][i] 

        if award=='best_delegate':
            df.loc[i, column] = 1
        elif award=='future_diplomat': 
            df.loc[i, column] = 2 
        else:
            df.loc[i, column] = 3

    return df


def read_input_file(path):
    """
    Reads the content of the specified .csv file, saves it in a pandas dataframe 
    and then prepares a dictionary which contains the content for the variables of the template file 
    to be used by the jinja rendering process. For the preparation it sorts the dataframe 
    according to the 'CommitteName' and 'AwardName' columns. The numerize_award_name function
    is used so that the values of the 'AwardName' column are sorted by "importance".  

    :param path: the relative path of the .csv file
    :return: the dictionary with the data for the template variables
    """
    df = pd.read_csv(path)
    df = numerize_award_name(df)
    df.sort_values(by=['CommitteeName', 'AwardName'], inplace=True, ignore_index=True)
    content_dict = dict() # a dictionary with the values of all the variables of the template

    content_dict['committee'] = df['CommitteeName'][0]
    for i in df.index:
        pos = str(i)

        content_dict["surname"+pos] = df['StudentSurname'][i]
        content_dict["name"+pos] = df['StudentName'][i]
        content_dict["country"+pos] = df['Country'][i] 
        content_dict["award"+pos] = df['AwardName'][i]
        content_dict["photo_file_path"+pos] = df['PhotoFilePath'][i]

    return content_dict


path = "content_input/content_file.csv"
content_dict = read_input_file(path)

environment = jinja2.Environment(
    loader=jinja2.PackageLoader("make_content"),
    autoescape=jinja2.select_autoescape()
)
template = environment.get_template("template.tex")
result = template.render(content_dict) # creates a latex file with content based on the template

with open('resulting_slides/slides.tex', 'w') as file:
    file.write(result)

