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
    #run function to solve the problem
    maxFitness = (nq*(nq-1))/2                                      #Best Fitness (GOAL)
    population = [generateChromosome(nq) for _ in range(100)]       #Initialize Population 'two dimensional array of range 100 and length 4'

    generation = 1                                                  #Generation Number

    while not maxFitness in [fitness(chrom, maxFitness) for chrom in population]:       #while maxFitness not found in population
        population = DEQueen(population, fitness, maxFitness)                    #call Differential Evolution function
        generation += 1
    for chrom in population:
        if fitness(chrom, maxFitness) == maxFitness:
            return chrom



#===================Differential Evolution Algorithm=====================================================

def generateChromosome(nq):
    #randomly generates a sequence of Chromosomes.
    return [ random.randint(1, nq) for _ in range(nq) ]

def mutation(chromosome):
    #change the value of a random index in chromosome.
    n = len(chromosome)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    chromosome[c] = m
    return chromosome

def crossover(chromx, chromy):
    #reproduce new chromosome from two Chromosomes.
    n = len(chromx)
    c = random.randint(0, n - 1)
    return chromx[0:c] + chromy[c:n]



def fitness(chromosome, maxFitness):
    #calculate fitness for chromosome.
    virtical_collisions = 0
    diagonal_collisions = 0
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2      #collisions[3,1,4,2] = 0/2 = 0


    n = len(chromosome)
    left_diagonal = [0] * 2*n                       #[0,0,0,....,2*n]
    right_diagonal = [0] * 2*n                      #[0,0,0,....,2*n]
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1                           #[0,1,1,0,1,1,0,0]
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1        #[0,1,1,0,1,1,0,0]


    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))      #maxFitness = Best Fitness

def probability(chromosome, fitness, maxFitness):
    #calculate chromosome fitness probability
    return fitness(chromosome, maxFitness) / maxFitness

def randomChromosome(population, probabilities):
    #pick random chrosome, based on probability
    total = sum(w for w in probabilities)                                       #sum of all probabilities
    r = random.uniform(0, total)                                                #random probability
    upto = 0
    for c, w in zip(population, probabilities):                                 #[[po1,pr1],[po2,pr2],......[pon,prn]]
        if upto + w >= r:
            return c                                                            #population with hiegher probability
        upto += w                                                               #sum of all previous probabilities
    assert False, "No Chromosome Selected"                                      #throw exception


def DEQueen(population, fitness, maxFitness):
    #Differential Evolution Algorithm
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(chrom, fitness, maxFitness) for chrom in population]       #probability of each chromosome
    for i in range(len(population)):
        x = randomChromosome(population, probabilities)                  #Best Chromosome1
        y = randomChromosome(population, probabilities)                  #Best Chromosome2
        child = mutation(x)                                         #mutation
        child = crossover(child, y)                     #           #crossover creating new chromosome from the best two chromosomes
        if fitness(child, maxFitness) < fitness(x, maxFitness):     #selection
            child = x
        new_population.append(child)
        if fitness(child, maxFitness) == maxFitness: break
    return new_population                                           #new generation


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


