# coding=utf-8
from tkinter import font
from tkinter import *
from tkinter import ttk
import sys
import os
import random

root=Tk()

root.title("n queen")
style=ttk.Style()
style.theme_use('classic')
f1=ttk.Frame(root)
f1.pack()
f1.config(width=300,height=100,relief=RIDGE)
f2=ttk.Frame(root)
f2.pack()
f2.config(width=100,height=100,relief=RIDGE)

style=ttk.Style()
style.theme_use('classic')

def run(nq):
    chrom = [0]*nq
    board = [ [0] * nq for _ in range(nq)]
    BTQueen(board, 0, chrom)
    return chrom

#===================Backtracking Algorithm=====================================================

def BTQueen(board, col, chrom):

    if col >= len(chrom):
        return True

    for i in range(len(chrom)):

        if valid(board, i, col, chrom):
            board[i][col] = 1
            chrom[col] = i+1
            if BTQueen(board, col + 1, chrom):
                return True

            board[i][col] = 0
            chrom[col] = 0
    return False


def valid(board, row, col, chrom):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i-=1
        j-=1

    i = row
    j = col
    while j >= 0 and i < len(chrom):
        if board[i][j] == 1:
            return False
        i+=1
        j-=1

    return True


#--------------------Board Design==============================================================================
def build_board(chrome):
    counter = 0
    for i in chrome:
        for n in range(len(chrome)):
            if counter%2 == 0:
                if n%2 == 0:
                    if n == i-1:
                        ttk.Label (f1, background='#999', text='♛',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label (f1, background='#999', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                else:
                    if n == i-1:
                        ttk.Label (f1, background='#fff', text='♛',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label (f1, background='#fff', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
            else:
                if n%2 == 0:
                    if n == i-1:
                        ttk.Label (f1, background='#fff', text='♛',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label (f1, background='#fff', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                else:
                    if n == i-1:
                        ttk.Label (f1, background='#999', text='♛',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label (f1, background='#999', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
        counter+=1

#=============1===================================================================================
but1 = ttk.Button(f2, text='easy', width=20)
but1.grid(row=0, column=0, sticky='nsew')
but1.config(command=lambda:[restart_program(), Click()])


def Click():
 Click.a = 1

 if Click.a == 1:
    chrome = run(4)
    build_board(chrome)
    
#=============2===================================================================================
but2=ttk.Button(f2,text='medium',width=20)
but2.grid(row=0,column=1,sticky='nsew')
but2.config(command=lambda :[restart_program(),Click2()])


def Click2():
 Click2.s =2
 if Click2.s ==2:
    chrome = run(6)
    build_board(chrome)

#=============3===================================================================================

but3=ttk.Button(f2,text='hard',width=20)
but3.grid(row=0,column=2,sticky='nsew')
but3.config(command=lambda :[restart_program(),Click3()])


def Click3():
    Click3.t = 3

    if Click3.t == 3:
        chrome = run(8)
        build_board(chrome)

                             
#=============restart program===================================================================================
def restart_program():
    for label in f1.grid_slaves():
        label.grid_forget()



root.mainloop()


