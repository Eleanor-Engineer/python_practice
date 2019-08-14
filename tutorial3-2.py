def same(a,b):
    if a.lower() == b.lower() :
        return 'They are the same.'
    else:
        return ':('

print(same('Marc LOVES hanging off the side of buildings','marc loves hanging off the side of buildings'))
print(same('James is writing his FIRST react app', 'james is writing a react app'))