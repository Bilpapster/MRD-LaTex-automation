The code creates a tex file with the required content. The tools are conveniently placed in the content-maker folder.

Instructions:
* Place the images of the five people in the content-input folder.
* Fill in the information of the five people in content_file.csv For each person there should be a line with the following information:
  studentID,StudentSurname,StudentName,gender,Country,AwardName,CommitteeName,PhotoFilePath
  The studentID is an increasing whole number, the gender gets a value from {male, female} and the AwardName gets a value from {best_delegate, future_diplomat, citation}.
  If the photo file path is not empty then the code makes the image round. Otherwise it uses a placeholder image, which corresponds to the gender of the person.
* Run the make_content.py script.
* In the resulting_slides folder build the slides.tex latex file.
* The final presentation slide is ready. It waits to be opened in resulting_slides/slides.pdf

Notes:
- The script places each information piece of the csv file in the appropriate spot in the tex file, while the processed image (after it gets round) is placed with a unique name in the resulting_slides/images folder.
- The template-folder contains only an example of the latex and the pdf files with placeholder text and images. It has nothing to do with the code.
