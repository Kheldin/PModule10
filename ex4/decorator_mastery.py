from functools import wraps
from typing import Any, Callable
from time import time

def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}")
        begin = time()
        res = func()
        end = time()
        t = end-begin
        print(f"Spell completed in {t}")
        print("Result:", res)
        return func()
    return wrapper


@spell_timer
def fireball() -> str:
    return ("Fireball cast !")

def power_validator(min_power: int) -> Callable[..., Any]:
    def wrapper(func: Callable[..., Any]) -> str | Callable[..., Any]:
        def wrapper_bis(*args: Any, **kwargs: Any) -> str | None:
            return (func(*args,**kwargs) if args[2] > min_power else 
                    "Insufficient power for this spell")
        return wrapper_bis
    return wrapper

class MageGuild():

    # @staticmethod
    # def validate_mage_name(name: str) -> bool:
    #     if len(name) < 3:
    #         # raise ValueError("Name should be at least 3 chars")
    #         return False
    #     return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"
        

if __name__ == "__main__":
    mage = MageGuild()
    fireball()
    print(mage.cast_spell("fireball", 12))