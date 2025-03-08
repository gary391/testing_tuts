| Term    | Definition                                                                          | Example                                     | 
|---------|-------------------------------------------------------------------------------------|---------------------------------------------| 
| Module  | A single Python file (.py) containing code (functions, classes, variables)          | math.py, random.py, or your custom utils.py | 
| Package | A directory (folder) containing multiple modules, identified by an __init__.py file | numpy, requests, or your own mypackage/     | 
| Library | A collection of modules and packages bundled together to provide functionality      | requests, pandas, scikit-learn              |
Module → A single Python file containing code.

# file: mymodule.py
    def greet():
        return "Hello!"
You can import it as:
    
    import mymodule
    print(mymodule.greet())  # Hello!
Package → A folder with an __init__.py file that contains multiple modules.
    
    mypackage/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
You can import it as:

    from mypackage import module1

Library → A collection of packages and modules that provide specific functionality.
    requests (for HTTP requests)
    pandas (for data analysis)
    matplotlib (for visualization)

💡 In short:

 - A module is a single file.
 - A package is a folder of modules.
 - A library is a collection of packages/modules that provide a set of features.

