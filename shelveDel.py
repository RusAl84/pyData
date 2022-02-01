import shelve
 
FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
 
with shelve.open(FILENAME) as states:
 
    state = states.pop("London", "NotFound")
    del states["Madrid"]  
    # states.clear()
    for key in states:
        print(key, " - ", states[key])