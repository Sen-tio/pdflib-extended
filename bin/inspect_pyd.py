import pdflib_extended.core.pdflib_py as pdflib_py
import inspect

print(dir(pdflib_py))

for name, obj in inspect.getmembers(pdflib_py):
    if inspect.isfunction(obj):
        print(f"Function: {name}")
        print(inspect.signature(obj))
    elif inspect.isclass(obj):
        print(f"Class: {name}")
        for method_name, method in inspect.getmembers(obj, inspect.isfunction):
            print(f"  Method: {method_name}")
            print(inspect.signature(method))
