# Import the ElementTree module of the xml library and the regular expression engine. 
#The ElementTree module will be used to do the parsing. The regular expression engine will be used to search for specific data
import xml.etree.ElementTree as ET
import re

# use the parse function from ET (ElementTree) to parse the myfile.xml file and assign it to a variable
# get the root element with the getroot function and assign it to a variable
xml = ET.parse("myfile.xml")
root = xml.getroot()

# Create a regular expression to get the contents of the XML root content in the <rpc> tag 
# and then add additional regular expressions to drill down into the content in order to find the value of the <edit-config>,
# <default-operation>, and <test-option> elements
ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

# Add print statements to print the value of the <default-operation> and <test-option> elements
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
