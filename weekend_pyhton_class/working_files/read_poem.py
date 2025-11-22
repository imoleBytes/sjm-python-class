

def readPoem(num=0):
    f = open("humpty_poem.txt", "r")
    content = ""
    try:
        if num == 0:       
            content = f.read()
        else:            
            content = f.readlines()[num]
        print(content.strip("\n"))  
        f.close()
    except:
        print(f"Lyrics not up to {num} lines: please provide valid line number")
  
   

readPoem()