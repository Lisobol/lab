Ivan ={
    "name": "ivan",
    "age": 51,
    "children":
        [{ "name": "vasja", "age": 13, },
         { "name": "petja", "age": 22, }],
}
darja = {
    "name": "darja",
    "age": 44,
    "children": [{ "name": "kirill", "age": 18, },
                 { "name": "pavel", "age": 11,}]
}
emps = [Ivan, darja]
for i in emps:
    for j in range(len(i["children"])):
        if i["children"][j]["age"] > 18:
            print(i["name"])