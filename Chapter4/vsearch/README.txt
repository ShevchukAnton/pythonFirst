Playing with self modules
How to create your own python package:

    create setup.py file with appropriate package description
    create README.txt file (can be empty)
    place all python modules, that u want to be included into the package, to same directory

    execute `py -3 setup.py sdist` to build package
    execute `pip install {package_name}` to install package into local repo