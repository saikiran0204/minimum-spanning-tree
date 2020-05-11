from turtle import *
from tkinter import *
from sys import exit


def exit_from_final(x, y):
    if 225 >= (500 - x) ** 2 + (-350 - y) ** 2:
        exit()


def minimum_spanning_tree():
    global graph, positions
    pencolor('Green')
    onscreenclick(exit_from_final)
    pensize("5")
    speed(1)
    spanning_tree = {}
    different_parts = []
    according_to_weights = [[0, 0, 99999]]
    for i in graph.keys():
        different_parts.append([i])
        spanning_tree[i] = {}
        for j in graph[i].keys():
            for k in range(len(according_to_weights)):
                if graph[i][j] < according_to_weights[k][2] and [j, i, graph[i][j]] not in according_to_weights:
                    according_to_weights.insert(k, [i, j, graph[i][j]])
                    break
    for i in range(len(according_to_weights)):
        for j in range(len(different_parts)):
            if according_to_weights[i][0] in different_parts[j]:
                node_1 = j
            if according_to_weights[i][1] in different_parts[j]:
                node_2 = j
        if node_1 == node_2:
            pass
        else:
            penup()
            setposition(positions[according_to_weights[i][0]])
            pendown()
            setposition(positions[according_to_weights[i][1]])
            spanning_tree[according_to_weights[i][0]][according_to_weights[i][1]] = graph[according_to_weights[i][0]][
                according_to_weights[i][1]]
            if node_1 > node_2:
                different_parts[node_2] += different_parts[node_1]
                different_parts.pop(node_1)
            else:
                different_parts[node_1] += different_parts[node_2]
                different_parts.pop(node_2)


def from_click_third(node, click_2, window):
    global graph, click_1
    weight = int(node.get())
    window.destroy()

    graph[click_1][click_2] = weight
    graph[click_2][click_1] = weight
    half_distance = (positions[click_1][0] + positions[click_2][0]) // 2, (
            positions[click_1][1] + positions[click_2][1]) // 2
    pendown()
    setposition(half_distance)
    write(weight)
    setposition(positions[click_2])
    penup()
    click_1 = None


def click_third(x, y):
    global positions, click_1, graph
    if 225 >= (500 - x) ** 2 + (-350 - y) ** 2:
        minimum_spanning_tree()
    k = True
    for i in positions.keys():
        if 225 >= (positions[i][0] - x) ** 2 + (positions[i][1] - y) ** 2:
            k = False

            if click_1 is None:
                click_1 = i
                setposition(positions[i])
            else:
                window_1 = Tk()
                if i in graph[click_1].keys():
                    Label(window_1, text='Edge already entered').grid(row=0, column=0)
                    z = Button(window_1, text="close", command=lambda: window_1.destroy())
                    z.grid(row=1, column=1)
                    click_1 = None
                else:
                    Label(window_1, text="Enter weight of the edge:").grid(row=0, column=0)
                    node = Entry(window_1)
                    node.grid(row=0, column=1)
                    z = Button(window_1, text="Enter",
                               command=lambda node=node, i=i, window=window_1: from_click_third(node, i, window))
                    z.grid(row=1, column=1)
                window_1.mainloop()
    if k:
        window = Tk()
        Label(window, text='Please click on node').grid(row=0, column=0)
        z = Button(window, text="close", command=lambda: window.destroy())
        z.grid(row=1, column=1)
        window.mainloop()


def third():
    window = Tk()
    if len(positions.keys()) < 2:
        Label(window, text='you have not entered minimum number of nodes').grid(row=0, column=0)
        z = Button(window, text="close", command=lambda: window.destroy())
        z.grid(row=1, column=1)
        window.mainloop()
    else:
        setposition(500, -365)
        pendown()
        fillcolor('Green')
        begin_fill()
        circle(15)
        end_fill()
        penup()
        setposition(493, -363)
        write('end')
        Label(window, text='Now enter for edges by clicking two nodes and hit green end').grid(row=0, column=0)
        z = Button(window, text="close", command=lambda: window.destroy())
        z.grid(row=1, column=0)
        onscreenclick(click_third)


def get(node, x, y, window2):
    global positions, graph
    node_name = str(node.get())
    window2.destroy()
    setposition(x, y)
    entry = 3
    for i in positions.keys():
        if i == node_name:
            entry = 1
            break
        else:
            entry = 3
    if entry == 1:
        frame_2 = Tk()
        Label(frame_2, text="Node already taken").grid(row=0, column=0)
        z = Button(frame_2, text="close", command=lambda: frame_2.destroy())
        z.grid(row=1, column=1)
    else:
        write(node_name)
        positions[node_name] = [x, y]
        graph[node_name] = {}


def click_second(x, y):
    global positions
    if 225 >= (500 - x) ** 2 + (-350 - y) ** 2:
        third()
    else:
        enter = True
        window_2 = Tk()
        for i in positions.keys():
            if 500 >= (positions[i][0] - x) ** 2 + (positions[i][1] - y) ** 2:
                enter = False
        if enter:
            Label(window_2, text="Enter node name:").grid(row=0, column=0)
            node = Entry(window_2)
            node.grid(row=0, column=1)
            z = Button(window_2, text="Enter",
                       command=lambda node=node, x=x, y=y, window_2=window_2: get(node, x, y, window_2))
            z.grid(row=1, column=1)
        else:
            Label(window_2, text="Entered position is near to the another node").grid(row=0, column=0)
            z = Button(window_2, text="Close", command=lambda: window_2.destroy())
            z.grid(row=1, column=1)


def second():
    Screen().setup(1200, 800)
    speed(0)
    penup()
    setposition(500, -365)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(15)
    end_fill()
    penup()
    setposition(493, -363)
    write('end')
    onscreenclick(click_second)
    mainloop()


def first():
    window = Tk()
    Label(window, text="Right click for nodes to be inserted and then press end in the window").grid(row=0, column=0)
    z = Button(window, text="close", command=lambda: window.destroy())
    z.grid(row=1, column=0)
    window.mainloop()
    second()


click_1 = None
graph = {}
positions = {}
first()
