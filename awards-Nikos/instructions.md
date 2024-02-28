1. Set up LaTeX to work (compile) documents locally. I suggest using Linux (or Windows Subsystem for Linux - WSL) and VSCode (I have tried this and works: https://nevalsar.hashnode.dev/compiling-latex-with-ubuntu-and-visual-studio-code).

2. Study the 13th and 14th slide of the `example.pptx` file. That is the template we want to create in `.tex` format.

3. You can assume that the data are contained (one student per row) in a `data.csv` file and images are contained in a directory `images/`

3. Create a `.tex` file with placeholder text that is identical with the 13th (or 14th) slide in terms of formatting.

4. Assuming that there is a `data.csv` file with schema of your choice (create it and fill it with dummy data), use python and (personal recommendation [Jinja templates](https://realpython.com/primer-on-jinja-templating/)).

5. Use Python to create one document for every Committe-row and compile it with latex.

The final goal is to be able to run a single script (e.g. `python3 create_awards.py`) and generate a `.pdf` file with one slide containing the awards and the students' info.
