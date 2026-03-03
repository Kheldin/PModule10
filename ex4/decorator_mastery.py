from functools import wraps
from typing import Any, Callable
from time import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        print(f"Casting {func.__name__}")
        begin = time()
        res = func(*args, **kwargs)
        end = time()
        t = end - begin
        print(f"Spell completed in {t}")
        print("Result:", res)
        return res

    return wrapper


@spell_timer
def fireball() -> str:
    return "Fireball cast !"


def power_validator(min_power: int) -> Callable[..., Any]:
    def wrapper(func: Callable[..., Any]) -> str | Callable[..., Any]:
        @wraps(func)
        def wrapper_bis(*args: Any, **kwargs: Any) -> str | None:
            return (
                func(*args, **kwargs)
                if args[2] >= min_power
                else "Insufficient power for this spell"
            )

        return wrapper_bis

    return wrapper


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper_bis(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper_bis
    return wrapper


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

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
