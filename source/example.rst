Examples
=============

Installation/Usage:
*******************
For now, the suggested method is to put the file `pangram_classes.py` in the same directory as your source files and call ``from pangram_classes import PangramChecker`.

``string`` must also be installed and imported as shown in the example below.



Simple True/False returning missing letters.
**************************************************
.. code-block:: python

    """This example demonstrates a simple true and false test using the PangramChecker class 
    and prints what's missing if the result is false."""
    import string 
    from pangram_classes import PangramChecker


    # example pangram variable
    sentence = ("The five boxing wizards jump quickly")

    # create object from pangram_classes PangramChecker

    check = PangramChecker(sentence)

    # checks if sentence passes the sentence through the 'ispangram' test. Then prints True.
    if(check.is_pangram()): 
        print("True")

    # if sentence fails pangram test then send it through 'missing_letters' to see what letters are missing and print them.
    else: 
        print("False","You're missing: ", check.missing_letters())

