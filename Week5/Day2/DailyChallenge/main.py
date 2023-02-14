class Pagination:
    def __init__(self,items = [],pageSize = 10):
        self.items=items
        self.pageSize=pageSize
        self.start_pointer = 0
        self.end_pointer = self.pageSize

    def getVisibleItems(self):
        self.visible_item = self.items[self.start_pointer:self.end_pointer]
        print(self.visible_item)

    def prevPage(self):
        self.start_pointer -= self.pageSize
        self.end_pointer -= self.pageSize 


    def nextPage(self):
        self.start_pointer += self.pageSize
        self.end_pointer += self.pageSize 
    

    def firstPage(self):
        self.visible_item = self.items[0:self.pageSize]

    def lastPage(self):

        if len(self.items) % self.pageSize != 0:
            self.start_pointer = len(self.items) // self.pageSize * self.pageSize
            self.end_pointer = self.start_pointer + self.pageSize
        else:
            self.start_pointer = int((len(self.items) / self.pageSize - 1) * self.pageSize)
            self.end_pointer = self.start_pointer + self.pageSize

    def goToPage(self,page):
        self.end_pointer = self.pageSize * page
        self.start_pointer = self.end_pointer - self.pageSize


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
p.getVisibleItems()

p.nextPage()
p.getVisibleItems()
        
p.lastPage()
p.getVisibleItems()
