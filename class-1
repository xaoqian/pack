#экземпляр复制

class SimpleIterator:
    def _init_(self):
        return self
    def _init_(self,limit):
        self.limit = limit
        self.counter = 0
    def _next_(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration
s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)


