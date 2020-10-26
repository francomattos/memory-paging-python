# The list of program words requested by program
wordBank = [10,11,104,170,73,309,185,245,246,434,458]

# Make a class for the paging system because why not
class PagingCounter:
    # Initializes variables for the program
    def __init__(self, _memSize, _pageSize):
        self.memSize = _memSize
        self.pageSize = _pageSize
        self.pageBank = []
    # This function checks if word is in memory, if not uses queue method to load page to memory
    def toMemory(self, wordVal):
        # This gives page number as per instructions
        self.pageLocation = int(wordVal /self.pageSize)
        # Return true if already loaded in memory, false if not
        if self.pageLocation in self.pageBank:
            return True
        else:
            if len(self.pageBank) < (self.memSize/self.pageSize):
                self.pageBank.append(self.pageLocation)
                return False
            else:
                self.pageBank.pop(0)
                self.pageBank.append(self.pageLocation)
                return False
    # This function initializes the paging process for a given scenario and return counter
    def initPaging(self):
        successCounter = 0
        for i in wordBank:
           # print("Word: " + str(i))
            if self.toMemory(i):
                successCounter += 1
           #     print("success")
           # else:
           #     print("Fail")
        return successCounter


print("a.)  Find the success frequency for the request list using a FIFO replacement Algorithm and a page size of 100 words (there are two page frames).")
page1 = PagingCounter(200,100)
answer = page1.initPaging()
print("The success frequency is: " + str(answer) + ".\n")

print("b.)  Find the success frequency for the request list using a FIFO replacement Algorithm and a page size of 20 words (10 pages, 0 through 9).")
page2 = PagingCounter(200,20)
answer = page2.initPaging()
print("The success frequency is: " + str(answer) + ".\n")

print("c.)  Find the success frequency for the request list using a FIFO replacement Algorithm and a page size of 200 words.")
page3 = PagingCounter(200,200)
answer = page3.initPaging()
print("The success frequency is: " + str(answer) + ".\n")

print("d.)  What do your results indicator ''Can you make any general statements about what happens when page sizes are halved or doubled?")
print("There could be a general statement which indicates that when the page size is halved the success rate decreases, and when it is doubled it increases.\n")

print("e.)  Are there any overriding advantages in using smaller pages?  What are the offsetting factors? Remember that transferring 200 words of information \n" +
      "takes less than twice as long as transferring 100 words because of the way secondary storage devices operate (the transfer rate is higher than the access, \n" +
      "or search/find, rate).")
print("Using smaller pages means that a program takes less space in memory, so memory usage is more efficient. The offsetting factor of using smaller pages is that the \n" +
      "success frequency decreases, so the program needs to itself into memory more often making the overall procedure slower. \n")

print("f.)  Repeat (a) through (c) above, using a main memory of 400 words. The size of each page frame will again correspond to the size of the page.")
page4 = PagingCounter(400,100)
answer = page4.initPaging()
print("The success frequency for memory size 400 and page size 100 is: " + str(answer))
page5 = PagingCounter(400,20)
answer = page5.initPaging()
print("The success frequency for memory size 400 and page size 20 is: " + str(answer))
page6 = PagingCounter(400,200)
answer = page6.initPaging()
print("The success frequency for memory size 400 and page size 200 is: " + str(answer) + ".\n")

print("g.)  What happened when more memory was given to the program? Can you make some general statements about this occurrence?" +
      "What changes might you expect to see if the request list was much longer, as it would be in real life?")
print("More memory given to the system means that larger page sizes can be utilized and the success rate would increase for larger programs.\n")

print("h.)  Could this request list happen during the execution of a real program? Explain.")
print("It would be extremely unlikely for this execution to happen in a real program, real programs tend to run in sequential order, " +
      "which this program is not doing, specially the segment '170,73,309,185,245'. But while unlikely, it is possible for this execution order " +
      "to happen in a program due to the flexible nature of computer programming. \n")

print("i.)  Would you expect the success rate of an actual program under similar conditions to be higher or lower than the one in this problem?")
print("The success rate of a real program would be higher in the same memory and page size scenarios given. This is due to programs being " +
      "sequention in nature as explained above \n \n")

input("Press any key to close...")


