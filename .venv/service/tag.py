
db = []
def create(data):
    db.append(data)

def get(data):
    print(True if data in db else False)