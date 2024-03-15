import numpy as np
import pandas as pd
from collections import OrderedDict
import jinja2
import numpy as np
from PIL import Image, ImageDraw


def numerize_award_name(df):
    """
    Replaces the values of the awards column in a dataframe, specifically:
    'best_delegate' with 1, 'future_diplomat' with 2 and 'citation' with 3.
    To be used in the read_input_file function.

    :param df: the dataframe which contains an awards column with values 
        from the set {'best_delegate', 'future_diplomat', 'citation'}
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


def make_image_round(image_path, position):
    """
    First the function crops a square of the middle of the image, which square has 
    a side of the smallest of the two dimensions of the image. Then it crops a circle
    of the image with a diameter the same as the side of the square. The final image 
    is stored in the images folder of the resulting latex file. 

    :param image_path: the path of the image in the system
    :param postition: a number which denotes the position of the image in the template file
    """
    img = Image.open(image_path)
    h = img.height
    w = img.width
    
    # crops the image to make it square
    if h <= w:
        margin = (w-h)/2
        img = img.crop((margin, 0, w-margin, h))
        min_dimension = h
    else:
        margin = (h-w)/2
        img = img.crop((0, margin, w, h-margin))
        min_dimension = w

    # Open the input image as numpy array, convert to RGB
    img = img.convert("RGB")
    npImage = np.array(img)

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice(((0,0),(min_dimension,min_dimension)),0,360,fill=255) # create the circle

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save(f'resulting_slides/images/image{position}.png')


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

        award = df['AwardName'][i]
        if award == 1:
            content_dict["award"+pos] = 'Βραβείο Καλύτερου Εμπειρογνώμονα'
        elif award == 2:
            content_dict["award"+pos] = 'Βραβείο Μελλοντικού Διπλομάτη'
        else:
            content_dict["award"+pos] = 'Εύφυμος Μνεία'

        image = df['PhotoFilePath'][i]
        try: # checks if there is a problem with the image path and if it is empty
            make_image_round(image, pos)
        except:
            gender = df['gender'][i]
            if gender == 'female':
                img = Image.open('templates/images/female portrait image.png')
            else:
                img = Image.open('templates/images/male portrait image.png')
            img.save(f'resulting_slides/images/image{pos}.png')

    return content_dict


input_path = "content_input/content_file.csv"
content_dict = read_input_file(input_path)

environment = jinja2.Environment(
    loader=jinja2.PackageLoader("make_content"),
    autoescape=jinja2.select_autoescape()
)
template = environment.get_template("template.tex")
result = template.render(content_dict) # creates a latex file with content based on the template

with open('resulting_slides/slides.tex', 'w') as file:
    file.write(result)

