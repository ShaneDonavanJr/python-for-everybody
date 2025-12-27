import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_2246531.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print(data)
print('Retrieved',len(data),'characters')

comments = json.loads(data).get("comments", {})
print(data)
print('Retrieved',len(data),'comments')


nums = list()
for comment in comments:
    print(f"Analyzing: {comment}")
    try : 
        count = comment.get("count", 0)
        print(f"Adding {comment.get('name', '`User')}'s comment count: {count}")
        nums.append(count)
    except Exception as e : 
        print(f"There has been an error: {e}")

print('Count:', len(nums))
print('Sum:', sum(nums))