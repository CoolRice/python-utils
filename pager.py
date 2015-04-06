# -*- coding: utf-8 -*-  
class Pager(object):
    
    list = None
    total = 0                           # 总数
    limit = 4                           # 每页条目
    pages = 1                           # 总页数
    pageNumber = 1                      # 当前页
    
    navigatePages = 5
    navigatePageNumbers = []
    
    isFirstPage = False;                # 是否为第一页
    isLastPage = False;                 # 是否为最后一页
    hasPreviousPage = False;            # 是否有前一页
    hasNextPage = False;                # 是否有下一页
    
    def __init__(self, pageNumber, total, limit):
        self.navigatePageNumbers = []
        
        self.total = total
        self.limit = limit
        
        self.pages = (self.total - 1) / self.limit + 1;
        
        self.pageNumber = pageNumber
        self.calcNavigatePageNumbers()
        self.judgePageBoudary()
    
    def calcNavigatePageNumbers(self):
        # 当总页数小于或等于导航页码数时
        if self.pages <= self.navigatePages:
            for i in range(0, self.pages):
                self.navigatePageNumbers.append(i + 1)
        # 当总页数大于导航页码数时
        else :
            startNum = self.pageNumber - self.navigatePages / 2
            endNum = self.pageNumber + self.navigatePages / 2
#             print 'startNum:' + str(startNum)
#             print 'endNum:' + str(endNum)
            if startNum < 1:
                startNum = 1
                # (最前navigatePages页
                for i in range(0, self.navigatePages):
                    self.navigatePageNumbers.append(startNum)
                    startNum += 1
            elif endNum > self.pages:
                endNum = self.pages
                # 最后navigatePages页
                for i in  range(0,self.navigatePages):
                    self.navigatePageNumbers.append((endNum-i));
                self.navigatePageNumbers.reverse()
            else:
                # 所有中间页
                for i in range(0, self.navigatePages):
                    self.navigatePageNumbers.append(startNum)
                    startNum += 1

    def judgePageBoudary(self):
        self.isFirstPage = self.pageNumber == 1;
        self.isLastPage = self.pageNumber == self.pages & self.pageNumber != 1;
        self.hasPreviousPage = self.pageNumber > 1;
        self.hasNextPage = self.pageNumber < self.pages;

# test    
# p = Pager(pageNumber=1, total=19, limit=4)
# print p.navigatePageNumbers