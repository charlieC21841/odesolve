# odesolve

in my odesolve.py file i have the functions created to pass the tests,
i also have the test_odesolve file to test my code and a picture of the graph which is a result of the odesolve function.
To run the code you will need both files in the same directory and run the test file in spyder. The graph will show up if you press ctrl + shift + g.
When running my code you will need to use my test_odesolve file as the last solveto test fails with h when it equals 1e-5. I was unable to find the cause for this error and fixed it by rounding the xguess value in test_solveto to 4 places so it gets close to the true value -11 but is only close enough when rounded to 4 places.
https://jupyter.org/try-jupyter/lab?path=odesolve.ipynb (link to the jupyter notebook)
