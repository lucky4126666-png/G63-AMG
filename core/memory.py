memory = {}

def add_memory(user_id, text):
    memory.setdefault(user_id, []).append(text)

def get_memory(user_id):
    return memory.get(user_id, [])[-5:]
