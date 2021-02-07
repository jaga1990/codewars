class PaginationHelper():
    collection = None
    items_per_page = None
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if self.items_per_page>=self.item_count():
            return 1            
        elif self.item_count() % self.items_per_page == 0:
            return self.item_count()//self.items_per_page
            #print(self.item_count()/self.items_per_page)
        else:
            return (self.item_count()-1)//self.items_per_page + 1
            #print((self.item_count()-1)/self.items_per_page + 1)
    
    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1            
        elif self.item_count() % self.items_per_page == 0 or page_index < self.page_count()-1:
            return self.items_per_page
        else:
            return self.item_count()-(self.items_per_page*(self.page_count()-1))


    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1
        else:
            return item_index // self.items_per_page        

page = PaginationHelper([1,2,3,4], 2)
page2 = PaginationHelper([3,4,5], 2)
print(page.page_index(3), page2.page_index(0))
