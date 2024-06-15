#Imports
import json;
import random;
import tkinter as tk;
from tkinter import messagebox;

#Game Build
class TicTacToe:
    def __init__(self, root, p1, p2):
        self.root = root
        self.root.title("TicTacToe")
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.p1 = p1
        self.p2 = p2
        self.create_grid()

    def create_grid(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text = '', font = 'normal 20 bold', width = 5, height = 2,
                                   command = lambda row = row, col = col: self.on_button_click(row, col))
                button.grid(row = row, column = col)
                self.board[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col]["text"] == '' and not self.winner():
            self.board[row][col]['text'] = self.current_player

            if self.winner():
                winner_name = self.p1 if self.current_player == 'X' else self.p2
                messagebox.showinfo("TicTacToe", f"Player {winner_name} wins!")
            elif self.tie():
                messagebox.showinfo("TicTacToe", "It's a tie!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'


    def winner(self):
        for row in range(3):
            if self.board[row][0]['text'] == self.board[row][1]['text'] == self.board[row][2]['text'] != '':
                return True
        for col in range(3):
            if self.board[0][col]['text'] == self.board[1][col]['text'] == self.board[2][col]['text'] != '':
                return True
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            return True
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            return True
        return False

    def tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col]['text'] == '':
                    return False
        return True

#Grabbing Player names
p1 = input("Name for player 1: ")
p2 = input("Name for player 2: ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root, p1, p2)
    root.mainloop()
