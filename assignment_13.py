import urllib.request
import xml.etree.ElementTree as ET

# url = input('Enter location: ')
url = 'http://py4e-data.dr-chuck.net/comments_2246530.xml'
# if len(url) < 1 : 
#     url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

print(tree)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)
    try : 
        print(int(result.text))
        nums.append(int(result.text))
    except Exception as e : 
        print(f"There has been an error: {e}")

print('Count:', len(nums))
print('Sum:', sum(nums))
