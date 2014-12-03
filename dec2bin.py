class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
       return  self.items==[]
    def pop(self):
        return self.items.pop()
    
def dec2bin(sayi):
    s=Stack()
    while sayi>0:
        a=sayi %2
        s.push(a)
        sayi=int(sayi/2)
    b=""
    while not s.isEmpty():
        b = b+ repr(s.pop())
    return b
    print(b)

