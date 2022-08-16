# from abc import ABC
#
# class HilbertSpace(ABC):
#
#     @abstractmethod
#     def __iter__(self):
#         while False:
#             yield None
#
#     def get_iterator(self):
#         return self.__iter__()
#
#     @classmethod
#     def __subclasshook__(cls, C):
#         if cls is MyIterable:
#             if any("__iter__" in B.__dict__ for B in C.__mro__):
#                 return True
#         return NotImplemented