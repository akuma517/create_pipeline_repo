# Task Definition

Create a pipeline that which takes all .c and .h files from https://github.com/Infineon/psoc6hal/tree/master/ and run uncrustify as shown below. 

´´´
uncrustify -c mystyle.cfg -f somefile.c -o somefile.c
´´´

Configuration file can be basic as defined in the example page.

Task shall be coded in python.

# Solution

The repo implements the task and the details are described as below.

A workflow is implemented which builds the 'uncrustify' repo.

The repo at https://github.com/Infineon/psoc6hal/tree/master/ is added as a submodule to the working repo and all the .c and .h files in the repository are beautified using the given command. 

The beautified code is stored in a separate DESTINATION folder as due to access issues the main repo can not be modified. Please find the modified files in `\beautified_code\`. 



 

