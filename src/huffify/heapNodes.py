from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    char: str
    freq: int

    def __add__(self, other: Node) -> Node:
        char = self.char + other.char
        freq = self.freq + other.freq
        return Node(char, freq)

    def __gt__(self, other: Node) -> bool:
        return self.freq > other.freq


@dataclass
class LexicographicNode(Node):
    def __add__(self, other: LexicographicNode) -> LexicographicNode:
        freq = self.freq + other.freq
        if self.char < other.char:
            char = self.char + other.char
        else:
            char = other.char + self.char
        return LexicographicNode(char, freq)

    def __gt__(self, other: LexicographicNode) -> bool:
        if self.freq == other.freq:
            if self.char < other.char:
                return True
            else:
                return False
        else:
            return self.freq > other.freq
