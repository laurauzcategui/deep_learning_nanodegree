## Jupyter Notebooks

Jupyter notebooks is a tool widely used on data analysis, data science and more. 

It's presented as a web application that allows you to combine explanatory text, math equations, code, visualizations, all in one document. 

Some notebooks examples: 
-  [Analysis of gravitational waves from two colliding blackholes detected by the LIGO experiment](https://www.gw-openscience.org/s/events/GW150914/GW150914_tutorial.html)

- [Web Scraping Indeed for Key Data Science Job Skills](https://nbviewer.jupyter.org/github/jmsteinw/Notebooks/blob/master/IndeedJobs.ipynb), really cool notebook showing by city in the states top skills need it for data science

- [Nice explanation about Neural networks](http://nbviewer.jupyter.org/github/masinoa/machine_learning/blob/master/04_Neural_Networks.ipynb), neural networks deep dive along with code

### Magic keywords

 Those are special commands that let you perform system calls such as changing directories. 

Highlights: 
* `%matplotlib`, work interactively with matplotlib 
* `%`, used for line magics
    
* `%%` --> used for cell magics

* `%timeit`, check how quick your code is. 

    You could use it in functions like this: 

    `%timeit fib(20)`

    or a whole portion on the cell

    ```
    import random 

    %%timeit 
    prize = 0 
    for i in range(100):
        roll = randon.randint(1,6)
        prize += roll
    ```

* `%pdb`, used for plugin in the interactive debugger

Reference to [Magic Commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

### Converting notebooks

>Nbconvert, will convert the Jupyter notebook file notebook.ipynb into the output format given by the FORMAT string.

- To convert a notebook to HTML:

`jupyter nbconvert --to html notebook.ipynb`

Reference of [nbconvert cli](https://nbconvert.readthedocs.io/en/latest/usage.html)

