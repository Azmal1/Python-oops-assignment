# 10) Write a Python program to get the class name of an instance in Python.

class MyClass:
    pass

if __name__ == "__main__":  
    # Create an instance of MyClass
    obj = MyClass()

    # Using type() function to get the class name
    class_name_with_type = type(obj).__name__
    print("Class name using type():", class_name_with_type)

    # Using __class__ attribute to get the class name
    class_name_with_attribute = obj.__class__.__name__
    print("Class name using __class__ attribute:", class_name_with_attribute)
