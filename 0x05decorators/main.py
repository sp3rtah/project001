

def onMessageType(type):
    handler = {'type': None}

    def decorator(f):
        handler[type] = f
        f('One')
        f('Two')
        return f
    return decorator


@onMessageType('text')
def checkmate(text):
    print(text)

if __name__ == '__main__':
    checkmate('Hello')
