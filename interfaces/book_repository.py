from abc import ABC, abstractmethod

class BookRepository(ABC):
    @abstractmethod
    def add(self, book): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, book_id): pass

    @abstractmethod
    def update(self, book): pass

    @abstractmethod
    def delete(self, book_id): pass
