from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any, Callable
import time


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    if operation == "min":
        return reduce(min, spells)
    if operation == "mul":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    raise ValueError("Unsuported Operation")


def partial_enchanter(
    base_enchantment: Callable[..., Any],
) -> dict[str, Callable[..., Any]]:
    fire_elem = partial(base_enchantment, element="fire", power=50)
    water_elem = partial(base_enchantment, element="water", power=50)
    air_elem = partial(base_enchantment, element="air", power=50)
    earth_elem = partial(base_enchantment, element="earth", power=50)

    return {
        "fire_partial": fire_elem,
        "water_partial": water_elem,
        "air_partial": air_elem,
        "earth_partial": earth_elem,
    }


def without_memoization(n: int) -> int:
    if n < 2:
        return n
    return without_memoization(n - 1) + without_memoization(n - 2)


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., Any]:
    @singledispatch
    def dispatcher(damage: int) -> int:
        return damage
    
    @dispatcher.register(str)
    def _1(enchantment: str) -> str:
        return f"Enchantement: {enchantment}"
    
    @dispatcher.register(list)
    def _2(multi_cast: list[Any]) -> list[Any]:
        return [val for val in multi_cast]

    return dispatcher

if __name__ == "__main__":

    def base_enchantment(element: str, power: int, target: str) -> str:
        return f"{element} hits {target} with {power} power"

    print("=============Testing spell reducer=============")
    try:
        print(spell_reducer([8, 4], "add"))
    except Exception as e:
        print(e)
    print("\n=============Testing partial enchanter=============")
    partial_test = partial_enchanter(base_enchantment)
    print(partial_test["fire_partial"](target="dragon"))
    print(partial_test["water_partial"](target="dragon"))
    print(partial_test["air_partial"](target="dragon"))
    print(partial_test["earth_partial"](target="dragon"))

    print("\n=============Testing memoized_fibonacci=============")
    begin = time.time()
    without_memoization(18)
    end = time.time()
    print(f"Took {end-begin} without LRU Cache")

    memoized_fibonacci(28)
    begin = time.time()
    memoized_fibonacci(18)
    end = time.time()
    print(f"Took {end-begin} with LRU Cache")

    print("\n=============Testing spell dispatcher=============")
    dispatcher = spell_dispatcher()
    print(dispatcher([1, 5]))
    print(dispatcher("bonjour"))
    print(dispatcher(9))
