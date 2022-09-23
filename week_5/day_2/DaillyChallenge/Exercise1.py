# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.current
# Page should be set to 1).
import tarfile


class Pagination:
    def __init__(self,items,pageSize):
        self.items=[]
        self.items=items
        self.pageSize=int(pageSize)
        self.pageSize=6
        # print(self.items)
    #method
    def getVisibleItems(self,n,m):
        newList=[]
        chaine=" ".join(self.items)
        taille=len(chaine)
        # print(chaine)
        for i in range(0,taille):
            self.items.append(chaine[i])
        # print("First page :",end=" ")
        print("p.getVisibleItems()")
        print(self.items[n:m])
        self.pageSize=len(self.items[n:m])
        # print(self.pageSize)
        # print(self.items)
        # for i in range(5):
        #     newList.append(self.items[i])
        # print(newList)
    #method
    def first_page(self):
        print("")
        print("p.first_page() :")
        print("")
        print(self.pageSize)
        self.getVisibleItems(1,self.pageSize+1)
    def nextPage(self):
        # print(self.items[5:9])
        print("")
        print("p.nextPage() :")
        print(self.pageSize)
        print("")
        
        self.getVisibleItems(self.pageSize+1,self.pageSize+self.pageSize+1)
        self.pageSize+=self.pageSize+1
    #method
    def last_page(self):
        print("")
        print("p.Last_page() :")
        print(self.pageSize-1)
        print("")
        self.getVisibleItems(self.pageSize,self.pageSize+4)
        self.pageSize+=self.pageSize+2
    #method
    def prevpage(self):
        print("")
        print("p.prevpage(): ")
        print(self.pageSize)
        print("")
        self.getVisibleItems(self.pageSize-3,self.pageSize)
    #method
    def goToPage(self):
        self.nextPage()
    
   
#instance
alphabetList = "abcdefghijklmnopqrstuvwxyz".split(' ')
p=Pagination(alphabetList,4)
p.getVisibleItems(1,p.pageSize)
p.first_page()
p.nextPage()
p.last_page()
p.prevpage()
p.goToPage(p.nextPage())
