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

def retry_spell(max_attempts: int) -> Callable[..., Any]:
    # @wraps()
    nb_tries = 1
    def wrapper(func: Callable[..., Any]):
        def wrapper_bis(*args: Any, **kwargs: Any) -> None:
            nonlocal nb_tries
            save_tries = nb_tries
            while nb_tries <= max_attempts:
                try:
                    func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                        f"(attempt {nb_tries}/{max_attempts})")
                    nb_tries += 1
                if nb_tries > max_attempts:
                    print("Spell casting failed after max_attempts attempts")
                if nb_tries == save_tries:
                    break
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

    print("\n=============Testing retry spell=============")

    print("\nTesting with error")
    @retry_spell(max_attempts=5)
    def raise_error() -> None:
        raise ValueError
    raise_error()

    print("\nTesting with no error")
    @retry_spell(max_attempts=3)
    def no_error() -> None:
        print("No problemo")

    no_error()