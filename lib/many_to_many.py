class Author:

    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contract_list = []
        Author.all_authors.append(self)
        
    def contracts(self):
        return self.contract_list
    
    def books(self):
        return [contract.book for contract in self.contract_list]
        
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        sum_of_royalties = [contract.royalties for contract in self.contract_list]
        return sum(sum_of_royalties)


class Book:

    all_books = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        Book.all_books.append(self)
    

    def contracts(self):
        return self.contracts_list
    
    def authors(self):
        return [contract.author for contract in self.contracts_list]

class Contract:

    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author): 
            self._author = author
            self.author.contract_list.append(self)

        else:
            raise Exception()
        
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if (type(book) == Book): 
            self._book = book
            self.book.contracts_list.append(self)
        else:
            raise Exception()
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if (type(date) == str):
            self._date = date
        else:
            raise Exception()
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if (type(royalties) == int):
            self._royalties = royalties
        else: 
            raise Exception()
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contracts, key=lambda contract: contract.date)