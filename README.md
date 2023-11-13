# python-challenge

# ---------------------------------------------------------------------------
# Author: Hamza Saleem
# Instructor: Piro Dhimitri 
# ---------------------------------------------------------------------------

The CSV filepath has been set relative to Python-Challenge as the working directory
Therefore in order for the code to run smoothly, kindly have the working directory set as PYTHON-CHALLENGE

There should be a main file with the script in each assignment folder, PyBank and PyPoll, a folder(directory) called Resources holding the raw csv files for each assignment and a folder(directory) called Analysis holding the analysis text file that was written by the script. Please keep in mind that the analysis folder is progammed such that, if the analysis folder was to be deleted, the main script will create a folder and the analysis text file. If the folder and file exist, then they will be overwritten

# References:
1. https://stackoverflow.com/questions/14555263/print-the-sum-of-a-list-of-integers-without-using-sum - This reference was used to sum the total of the values within a list. total_net += i is a shorthand for total_net = total_net + i and since i is not the index of the list but rather the value itself, total_net would add up to all iteration values of i. 

2. https://note.nkmk.me/en/python-os-mkdir-makedirs/#create-a-directory-osmkdir - This reference was used to create a new directory using the OS.mkdir() method which creates a directory given a relative filepath

3.  https://www.freecodecamp.org/news/file-handling-in-python/ - This reference was used to get the syntax in order to create a text file and write in it. Class notes show how to create a csv file and how to write in a csv file, but for our purposes, I needed to create a text file and write in it 

4. https://docs.python.org/3/tutorial/datastructures.html - This reference was used to be able to print a dictionary's key and value pair in an effective way. list.items() is a method for dictionaries that takes no parameters and returns the key and value pair in a tuple. Using a for loop, we can iterate between all the items within a dictionary and then either store it or print it. 

5. https://docs.python.org/3/tutorial/datastructures.html - this reference was used to get the method count(). count() is a method for lists that returns the number of times the parameter appears in that list. So, given a parameter as a value, the method will look for how many times that value appeared in the list. 


