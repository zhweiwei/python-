str = "this is string example....wow!!! this is really string"

print(str.replace("is", "was"))
print(str.replace("is", "was", 3))
print(str)

import  re
str = "this is string example....wow!!! this is really string"
print(re.sub("is","was",str))
