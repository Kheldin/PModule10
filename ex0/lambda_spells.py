from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: (f"* {x} *"), spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "max_power": max(mages, key=lambda x: x["power"]),
        "min_power": min(mages, key=lambda x: x["power"]),
        "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages),
    }


if __name__ == "__main__":

    print("=============Testing artifact sorter=============")
    artifacts: list[dict[str, Any]] = [
        {"name": "Crystal Orb", "power": 85, "type": "divination"},
        {"name": "Fire Staff", "power": 92, "type": "offensive"},
        {"name": "Shadow Cloak", "power": 60, "type": "stealth"},
        {"name": "Thunder Hammer", "power": 78, "type": "offensive"},
        {"name": "Healing Chalice", "power": 45, "type": "support"},
    ]
    print(artifact_sorter(artifacts))

    print()

    print("=============Testing power filter=============")
    mages: list[dict[str, Any]] = [
        {"name": "Alex", "power": 30, "element": "fire"},
        {"name": "Jordan", "power": 75, "element": "ice"},
        {"name": "Riley", "power": 50, "element": "lightning"},
        {"name": "Morgan", "power": 20, "element": "earth"},
        {"name": "Sage", "power": 90, "element": "arcane"},
    ]
    print(power_filter(mages, 50))

    print()

    print("=============Testing spell transformer=============")
    spells = ["fireball", "heal", "shield", "lightning bolt", "frost nova"]
    print(spell_transformer(spells))

    print()

    print("=============Testing mages stats=============")
    print(mage_stats(mages))
