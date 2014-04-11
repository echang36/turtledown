turtledown
==========

My final data science project is in the folder titled congressional-record-master. 

--------------

Folders:

-output
Contain the raw text and XML files of the Congressional hearings. These
were pulled using the congressional-record script 
(https://github.com/unitedstates/congressional-record).

-congress_data / congress_data_even / congress_data_random
Contain files written by my scripts, parsed text files that are arranged by name of 
conservative and liberal representatives.

-ipython notebooks
Contain the ipython notebooks I used to test all these scripts. They wont' work as they
are, because I moved them into a folder within congressional-record master after using 
them. In order to use them, you will need to change the path names.

--------------

Scripts: 

congressional_record.py
Processes the downloaded data.

scikit_commands.py
Runs various scikit analysis on the resulting processed data.

--------------

The rest of the files and folders were used by the congressional-record script. Note that
there are two setup.py files, because I had to change the setup file to work on my 
computer. I used setup2.py; the original is setup.py