from expression.core import Result, Success, Failure
from typing import List, TypeVar, Callable

T = TypeVar("T")
E = TypeVar("E")

def traverse_results(results: List[Result[T, E]]) -> Result[List[T], E]:
    values: List[T] = []
    
    for result in results:
        if result.is_ok:
            values.append(result.ok)
        else:
            return result
    return Success(values)