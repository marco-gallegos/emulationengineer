
x = int(input("dame un numero x: "))
y = int(input("dame un numero y: "))

CMD = {
    "ID": 55,
    "Data": "hola",
    "More": [ 
        {
            "a": 1
        },
        {
            "b":2
        }
    ]
}

CMD["More"][0]["a"] += x 
CMD["More"][1]["b"] += y 

print(CMD)