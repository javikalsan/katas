from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Player:
    name: str
    position: int


@dataclass(frozen=True)
class GameStatus:
    last_player: Optional[str]
    winner: Optional[str]
    draw: bool
