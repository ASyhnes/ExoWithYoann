objects = [("A", "foo"), ("B", "bar"), ("C", "baz")]
search_param = "bar"

for obj in objects:
    if obj[1] == search_param:
        print("The object has been found:", obj)
        break
else:
    print("Error: the object was not found")