from PackageA import dbhelper

print("Inside moduleB")
dbhelper.banana("Calling moduleB from moduleA")

# Command to run this file as module
# python -m PackageB.test2