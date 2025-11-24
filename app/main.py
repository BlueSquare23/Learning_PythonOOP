#!/usr/bin/env python3

from item import Item
from phone import Phone

def main():
    item = Item("myItem", 750)

    item.name = "newItemName"

    print(item.name)

if __name__ == "__main__":
    main()
