#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Jupyter Notebooks.
# 
# # Tutorial 1 — Introducing Jupyter Notebooks
# 
# Benjamin J. Morgan, University of Bath.

# # Contents
# 
# - [Data Analysis with Jupyter Notebooks](#intro)
#     - [Why analyse data with computer code?](#why)
# - [Getting Started with Jupyter Notebooks](#getting_started)
# - [Running Code](#running_code)
# - [Saving Notebooks](#saving_notebooks)
# - [Comments and Markdown cells](#comments)
# - [Using assert Statements for Interactive Feedback](#assert_statements)

# # Data Analysis with Jupyter Notebooks<a id="intro"></a>
# 
# This is a Jupyter notebook. In some ways each document is like a physical notebook. It can be used for describing an experiment, recording data, and commenting on it. Unlike a physical notebook, a Jupyter notebook also allows you to run and easily share computer code. This combination makes Jupyter notebooks a very useful tool for analysing data collected from experiments. Unlike spreadsheets or combinations of separate data analysis codes, a Jupyter notebook allows you to collect desciptions and notes for individual experiments, links to the raw data collected, the computer code that performs any necessary data analysis, and the final figures generated with these data, ready for use in a report or published paper.
# 
# ## Why analyse data using code?<a id="id"></a>
# Using computer code allows you to analyse experimental data *programmatically*. All the steps for working with your data are carried out according to a *program*; a predefined series of instructions; like a recipe for a particular meal. 
# 
# Once a particular program has been written, it will always produce the same results with the same starting data. This makes it possible to &ldquo;show your working&rdquo;. Scientists presenting new results can share their original data, alongside the code that they used for all their analysis. This has a number of benefits. Other scientists can review the code, run it against the original data set, and check that any analysis has been done correctly. 
# 
# Finished code can also be used as a starting point for looking at a similar set of data. The original scientist might repeat their experiment to confirm their results, or another group might collect data under slightly different conditions, and want to compare the two cases. Often the steps described by the code are the same for small data sets and for large data sets. Once an analysis program exists, processing enormous data sets simply becomes a question of access to sufficiently powerful computers. 

# # Getting Started with Jupyter Notebooks<a id='getting_started'></a>
# 
# A Jupyter notebook consists of a series of **cells** that contain text. These cells are arranged vertically, top-to-bottom in the document. Any cell can be edited by clicking on it. A cell in **edit mode** is indicated by a green border. 
# <img style="width:700px" src='figures/target_cell.png' />
# A cell with a blue border is in **command mode**. 
# <img style="width:700px" src='figures/command_mode_cell.png' />
# In command mode you are not able to type into a cell, but you can still edit the notebook (reordering cells, executing code, etc.) Commands for editing notebooks can be accessed from the manu at the top of the screen, and commonly used commands have keyboard shortcuts, which will be highlighted in the examples below. The full list of keyboard shortcuts can be found through **Help > Keyboard Shortcuts** in the menu, or by pressing **H**.
# 
# To edit a cell in command mode, press enter or double click on the cell.

# ## Running Code<a id="running_code"></a> 
# 
# The Jupyter notebook is primarily useful for writing and running code. A large number of different computer languages can be used in Jupyter notebooks. In these examples, we will be using Python (specifically Python 3). Python is increasingly used across a large number of scientific disciplines for data management and analysis. The large scientific community means that very good resources already exist for data processing, such as the Jupyter project, and specific prewritten tools for manipulating and plotting data.
# 
# This course will not go into detail about how to write your own Python code. Instead, as much as possible we are going to focus on learning how to use readily available packages for data analysis. There are plenty of resources for learning Python for more traditional programming tasks, such as the DataCamp [Learn Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science) tutorial.
# 
# The default cell type in a Jupyter notebook is a **code** cell. If you open a new notebook it will have one, empty, code cell. And you can always create more cells by clicking in the menu on **Insert > Insert Cell Above** (or press **A**) or **Insert > Insert Cell Below** (or press **B**).  
# <img style="width:550px" src='http://blogs.bath.ac.uk/python/wp-content/uploads/sites/140/2017/11/insert_cell.png'/>
# Any code typed into a code cell can be run (or &ldquo;**executed**&rdquo;) by pressing `Shift-Enter` or pressing the <img style='display:inline; height:1.5em; vertical-align: bottom;' src='figures/run_code_button.png'/> button in the notebook toolbar.
# 
# This practical consists of an interactive tutorial (this notebook), followed by a a series of exercises. Some code cells in the tutorial will already have code in them, which you can **run** by selecting and pressing `Shift-Enter` or clicking the toolbar button:

# In[ ]:


2+3 # run this cell…


# You should now have <span style="color:#D64423; font-family:monospace">Out[ ]:</span> with the result of running this code printed next to it:
# <img style="width:590px" src='http://blogs.bath.ac.uk/python/wp-content/uploads/sites/140/2017/11/output.png'/>
# and the focus has automatically moved to the next cell. You can always re-select a cell to run it again.
# 
# Most of the code examples will be presented like this:
# 
# >```python
# print("hello")
# ```
# 
# with an empty code cell underneath. These examples are for you to type into the empty code cell and then run. Do not copy and paste these. You will learn the concepts faster and become comfortable with writing your own code if you type each piece of code out.
# 
# Start with this example:
# 
# >```python
# print("hello")
# ```

# In[ ]:


print( "hello" )


# Your output should be
# 
# ```
# hello
# ```

# There will also be small exercises that ask you to write your own piece of code from scratch, or modify an example that is not finished yet; it might contain an error – often called a **bug**, or just not do exactly what we would like. These will be indicated with green boxes.

# <div class="alert alert-success"> 
# <b>Edit</b> the <span style="font-family:monospace;">print</span> statement below, so that when you run the cell it prints your name.
# </div>

# Missing code is indicated by a series of grey squares, which you will need to replace.

# In[ ]:


# Edit this code cell and run it.
print("My name is ◽◽◽")


# <div class="alert alert-success">
# Type new code into the cell below to print today's date.
# </div>

# In[ ]:


# Edit this code cell and run it.
print( ◽◽◽ )


# ## Saving Notebooks<a id="saving_notebooks"></a>
# 
# To save your notebook, you can select **File > Save and Checkpoint** from the Jupyter menu, or use the keyboard shortcut **⌘+S** (on macOS) or **ctrl+S** (on Windows & Linux). Jupyter notebooks are saved as **.ipynb** files.
# 
# <img style='width:550px' src='http://blogs.bath.ac.uk/python/wp-content/uploads/sites/140/2017/11/save_and_checkpoint.png'/>
# 
# You can make a copy of a notebook (for example, to save an old version while you work on a new idea, or to duplicate a notebook to a different directory) you can either select **File > Make a Copy**, which duplicates the current notebook in the same directory; or you can select **File&nbsp;>&nbsp;Download&nbsp;as&nbsp;>&nbsp;Notebook&nbsp;(.ipynb)**, to download a copy into your **Downloads**.

# ## Explain Your Code: Comments and Markdown Cells<a id="comments"></a>
# One of the advantages of using *code* for numerical calculations and data analysis is that you end up with a record of exactly what you have done. You, or anyone else, can read the code, to understand how you reached your answer. You can think of this as &ldquo;showing your working&rdquo;, and it can be very helpful if you want to solve a *similar* problem in the future.
# 
# Often, reading only the code can get quite cryptic (it is called &ldquo;code&rdquo;, after all), which makes it difficult to understand what is happening. To explain what a particular piece of code does, or to explain *why* a piece of code is being used, you can include **comments**.
# 
#  
# ```python
# # this is a comment
# ```
# 
# Any text that appears after a <span style="font-family:monospace; color:#438080">#</span> symbol is part of the comment, and is ignored when the code is run. 
# 
# Jupyter notebooks offer a second way to describe what you are doing: **Markdown cells**. A code cell can be converted to a Markdown cell by selecting Cell > Cell Type > Markdown from the menu.  
# <img src='http://blogs.bath.ac.uk/python/wp-content/uploads/sites/140/2017/11/markdown.png', width=350/>  
# A Markdown cell can be used to type plain text, which is displayed when the cell is run. Markdown cells are useful for documenting a notebook, particularly when you want to write something more detailed than a short comment. Markdown cells can also contain basic text formatting, links, images, and equations (more information is [here](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html)).

# <div class="alert alert-success">
# Type a comment into the cell below and run it.
# </div>

# In[ ]:


◽◽◽


# <div class="alert alert-success">
# The cell below should be a Markdown cell, but it is currently a code cell.  
# First run the cell to see what happens.
# Then change it into a **Markdown** cell, before re-running it. 
# </div>

# In[ ]:


Markdown cells allow you to type longer text to explain what your code is doing.  
Setting this cell to Markdown, and running it will format the text for clearer reading.  
Markdown also provides shorthand for including other features such as [links][cheatsheet].

[cheatsheet]:https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet


# To edit a Markdown cell after it has been run, double-click on it to see the raw Markdown code.

# <div class="alert alert-success">
# Double click on the Markdown output above that starts &ldquo;*Markdown cells allow you to type longer text&hellip;*&rdquo; and add the following Markdown code to it:<br/><br/><span style='font-family:monospace'># My favourite meals are<br/>
# - Breakfast<br/>
# - Lunch<br/>
# - Brunch
# </span><br/><br/>
# </div>
# 
# Then re-run the cell to view the formatted output.

# ## Using **<span style="color:#377d22; font-family:monospace">assert</span>** Statements for Interactive Feedback<a id="assert_statements"></a>
# 
# The exercise notebooks contain code cells with **<span style="color:#377d22; font-family:monospace">assert</span>** statements. These have been included so that you can test your code as you write it.  
# 
# An **<span style="color:#377d22; font-family:monospace">assert</span>** statement checks whether a particular condition is **true**, or **false**. If the specified condition is **false**, running the code will produce an <span style="color:#D64423; font-family:monospace">AssertionError</span> error. If this happens, go back to your code, and figure out the source of the error before moving on. If an **<span style="color:#377d22; font-family:monospace">assert</span>** statement runs without an error, your code works correctly and you can move on to the next part of the exercise.
# 
# e.g. if this is given as a mini-exercise
# 
# <div class="alert alert-success"> 
# Calculate two plus two.
# </div>
# 
# and you mistype the solution in the code cell below:

# In[ ]:


# enter your code in this cell
2+3


# In[ ]:


# this cell tests your code. You do not need to edit it.
assert _ == 4 
# the _ character refers to the output from the previous cell.


# Because the calcualtion code gives the wrong result, the **<span style="color:#377d22; font-family:monospace">assert</span>** statement in the following cell fails, producing an <span style="color:#D64423; font-family:monospace">AssertionError</span>.
# 
# <div class="alert alert-success"> 
# Correct the code above, and check that the test passes.
# </div>
