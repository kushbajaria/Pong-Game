#!/usr/bin/env python3

'''main program for pong game'''
import sys
from videogame import game


def main():
    '''main function for pong game'''
    print("Welcome to Pong.")


if __name__ == "__main__":
    sys.exit(game.PongGame().run())
