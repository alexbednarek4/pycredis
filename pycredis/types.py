from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class SimpleString:
    data: str


@dataclass
class Error:
    data: str


@dataclass
class Integer:
    data: int


@dataclass
class BulkString:
    data: bytes


@dataclass
class Array(Sequence):
    data: list

