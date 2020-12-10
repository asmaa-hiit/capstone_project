#Write some markdown to explain that this notebook will be mainly used for the capstone project.
 
#@title This project is a notebook capstone
#@markdown Let's get started

no_type_checking = ''  #@param
string_type = 'example'  #@param {type: "string"}
slider_value = 142  #@param {type: "slider", min: 100, max: 200}
number = 102  #@param {type: "number"}
date = '2010-11-05'  #@param {type: "date"}
pick_me = "monday"  #@param ['monday', 'tuesday', 'wednesday', 'thursday']
select_or_input = "apples" #@param ["apples", "bananas", "oranges"] {allow-input: true}
#@markdown ---
#Import the pandas library as pd.
import pandas as pd
#Import the Numpy library as np.
import numpy as np
#Print the following the statement: Hello Capstone Project Course!
print('Hello Capstone Project Course!!!')
