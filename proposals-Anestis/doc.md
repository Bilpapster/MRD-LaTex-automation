# Instructions
## How to insert your data
  - Put your text data into the data.xlsx file that is located in the data directory
  - In the column 'committeeID' put the id of the committee in the form of a number (for example 1)
  - In the column 'committeeName' put the name of the committee
  - In the column 'topicName' put the name of the topic
  - In the column 'speakerCountry' put the name of the speaker country
  - In the column 'supporters' put the supporting countries. Be very careful because the format you must follow is very specific: Supporter1, Supporter2, Supporter3, ... Every supporter is separated from the next one with a ',' and a blank space.The first supporter does not have a blank space in front of her and the last supporter does not have neither a ',' nor a blank space after her
  - In the column 'basedOn' put the bases. Again be very careful with the format: Base1$ Base2$ Base3$ ... Every base is separated from the next one with a '$' and a blank space.The first base does not have a blank space in front of her and the last base does not have neither a '$' nor a blank space after her
  - In the column 'proposals' put the proposals.Again follow the format that you followed when putting data to the 'basedOn' column: Proposal1$ Proposal2$ Proposal3$ ...
  - In the column 'boldWordsOnProposals' put a sequence of numbers. The indexes of the numbers in the sequence correspond to the indexes of the proposals.The numbers of the sequence determine how many words will be bolded in the corresponding proposal, starting at the begining of the proposal.For example if you write the sequence 2, 1, 5 you mean that the first proposal will have the first 2 words bolded, the second proposal will have the first word bolded and the third proposal will have the first 5 words bolded.Again be very careful with the format: Number1, Number2, Number3, ... Every number is separated from the next one with a ',' and a blank space.The first number does not have a blank space before and the last number does not have neither a ',' nor a blank space after.Also be careful so as the number of elements in the sequence is equal to the number of the proposals

## Extra notes
  - Never use single quotes ( ' ), only use double quotes ( " ) inside your content
  - Never use the ' $ ' symbol inside your bases and proposals content
  - If you want to use an english word/term inside your content, do so by writing: \textlatin{your_english_text}
  - Check the starting data.xlsx file if you have questions about how to insert the data
  - After you insert the data to the csv and run the main.py file ,a file (or files) is created in the outputs directory with the name: 'committee id_name_of_topic_ΓΝΩΜΗ.txt. By copy-pasting the file's content in overleaf you will get the final pdf
  - When compiling the file in overleaf be sure to create a directory that is called 'images' and inside have the mrd_logo.png