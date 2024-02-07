from typing import TypeVar, Generic, Optional
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

T = TypeVar("T", bound=BaseModel)

class ServiceResponse(GenericModel, Generic[T]):
              statusCode: Optional[int] = Field(type=int, default=200, title="statusCode", description="API invocation HTTP Status Code")
               statusMessage: Optional[istr] = Field(type=str, default="OK", title="statusMessage", description="API invocation HTTP Status Message")
               data: Optional[T] = Field(default=None, title="data", description="API invocation result")

               def __init__(self, data:T=None, statusCode:int = 200, statusMessage: str=" ") -> None:
                        super().__init__()
                       self.data = data
                      self.statusCode = statusCode
                      self.statusMessage = statusMessage

            def setData(self, data):
                   self.data = data
