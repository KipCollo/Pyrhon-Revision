from abc import ABC,abstractmethod

class Stream(ABC):

    @abstractmethod
    def open():
        pass

    @abstractmethod
    def read():
        pass

class File(Stream):
      
    def open():
        print("open from file")

   
    def read():
        print("Read from file")

file =File()
file.open()