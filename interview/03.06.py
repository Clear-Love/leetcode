'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 20:32:14
LastEditors: lmio 2091319361@qq.com
Description: 面试题 03.06. 动物收容所
'''
from collections import deque
from typing import List

class AnimalShelf:

    def __init__(self):
        self.animals = deque()
        self.cats = deque()
        self.dogs = deque()

    def enqueue(self, animal: List[int]) -> None:
        self.animals.append(animal[0])
        if animal[1]:
            self.dogs.append(animal[0])
        else:
            self.cats.append(animal[0])

    def dequeueAny(self) -> List[int]:
        if not self.animals:
            return [-1, -1]
        id = self.animals.popleft()
        if self.dogs and self.dogs[0] == id:
            self.dogs.popleft()
            return [id, 1]
        else:
            self.cats.popleft()
            return [id, 0]

    def dequeueDog(self) -> List[int]:
        if self.dogs:
            id = self.dogs.popleft()
            self.animals.remove(id)
            return [id, 1]
        return [-1, -1]

    def dequeueCat(self) -> List[int]:
        if self.cats:
            id = self.cats.popleft()
            self.animals.remove(id)
            return [id, 0]
        return [-1, -1]