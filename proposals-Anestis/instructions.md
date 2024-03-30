1. Set up LaTeX to work (compile) documents locally. I suggest using Linux (or Windows Subsystem for Linux - WSL) and VSCode (I have tried this and works:   https://nevalsar.hashnode.dev/compiling-latex-with-ubuntu-and-visual-studio-code).

2. Extract the `examples.zip` file and study the formatting of the documents contained.

3. Create a `.tex` file with placeholder text that is identical with the `.doc` template in terms of formatting.

4. Assuming that there is a `data.csv` file with schema of your choice (create it and fill it with dummy data), use python and (personal recommendation [Jinja templates](https://realpython.com/primer-on-jinja-templating/)).

5. Use Python to create one document for every Committe-row and compile it with latex.

The final goal is to be able to run a single script (e.g. `python3 create_proposals.py`) and generate all `.pdf` files in a separated folder :)
