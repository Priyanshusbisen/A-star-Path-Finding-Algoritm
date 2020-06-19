try:
    import pygame
    from math import sqrt
    import time
    import tkinter
    from tkinter import *
except:
    import install_requirements
    import pygame
    import time
    from math import sqrt
    import tkinter
    from tkinter import *


class Node():
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self,other):
        return self.position == other.position

    def Adjency_list(self):
        '''This Function return the list of all adjacent element
            of the current node.'''
        global Screen_height,Screen_width,wall_list
        adjency_list = []
        test_list = [(1,0),(-1,0),(0,1),(0,-1)]
        for i,j in test_list:
            if (self.position[0]+i, self.position[1]+j) not in wall_list:
                if 0<= self.position[0]+i <= Screen_width-1 and 0 <= self.position[1]+j <= Screen_height-1:
                    adjency_list.append((self.position[0]+i, self.position[1]+j))
                    
        

        return adjency_list

    def visualize(self,color):
        global block_size, window
        rect = pygame.Rect(self.position[0]*block_size,self.position[1]*block_size,block_size-1,block_size-1)
        pygame.draw.rect(window,color,rect)
        


def onsubmit():
    '''on clicking the submit button we need
        the tk window to get destroyed'''
    global start, end
    
    start = (int(Entry1.get().split(',')[0]),int(Entry1.get().split(',')[1]))
             
    end = (int(Entry2.get().split(',')[0]),int(Entry2.get().split(',')[1]))

    popup_window.quit()
    popup_window.destroy()



Screen_height = 600
Screen_width = 800
block_size = 20    

pygame.init()
window = pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption('Path Finder')

for j in range(Screen_height):
    for i in range(Screen_width):
        node = Node(None,(i,j))
        node.visualize((114,160,193))
    pygame.display.update()


popup_window = Tk()
popup_window.title('Input Position')
v = IntVar()
label1 = Label(popup_window,text='Start(x,y): ')
label1.grid(pady = 3)
Entry1 = Entry(popup_window)
Entry1.grid(row=0,column=1,pady=3)
label2 = Label(popup_window,text ='End(x,y): ')
label2.grid(row = 1,column = 0,pady = 3)
Entry2 = Entry(popup_window)
Entry2.grid(row = 1,column= 1,pady =3)
submit = Button(popup_window,text = 'Submit',command = onsubmit)
submit.grid(row=2,column=0,padx =2,pady=2)
show_steps = Checkbutton(popup_window,text = 'Show Procedure',variable = v)
show_steps.grid(row = 3)
show_steps.var = v
popup_window.update()
mainloop()

start_node = Node(None,start)
end_node = Node(None,end)


start_node.visualize((0,128,0))#green color
end_node.visualize((0,0,139))#red color
pygame.display.update()

wall_list = []

def Mouse_action(position):
    '''creates a wall on all the blocks
        where the mouse cursor goes when
        right click is pressed.'''

    global wall_list
    x = position[0]//block_size
    y = position[1]//block_size
    node = Node(None,(int(x),int(y)))
    if node.position != start and node.position != end:
        node.visualize((0,0,0))
        wall_list.append(node.position)



    
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            Mouse_action(pos)    
            pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                loop = False
                break

    
open_list = []
closed_list = []
open_list.append(start_node)
start_node.g= start_node.h=start_node.f = 0


def main():
    '''This function performs the main Astar algorithm'''  


    global start_node, end_node, window, start, end,wall_list, Screen_height, Screen_width, block_size,stop,v

    if len(open_list)>0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            open_list.pop(current_index)
            closed_list.append(current_node)
            
            if current_node.position == end_node.position:
                stop = True
                path = []
                current = current_node
                
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                    
                    
                for i in path:
                    if i != start and i!= end:
                        rect = pygame.Rect(i[0]*block_size,i[1]*block_size,block_size-1,block_size-1)
                        pygame.draw.rect(window,(255,0,0),rect)
                        pygame.display.update()
                return None
                
    
                    
            ignore = False
            for i in range(len(current_node.Adjency_list())):
                new_node = Node(current_node,current_node.Adjency_list()[i])
                if  new_node not in closed_list:

                    tempg = current_node.g + 10
                    
                    new_node.h = int(sqrt((end_node.position[1]-new_node.position[1])*(end_node.position[1]-new_node.position[1]) + (end_node.position[0]-new_node.position[0])*(end_node.position[0]-new_node.position[0]))*10)
                    
                    new_node.f = new_node.g + new_node.h
                    if new_node in open_list:
                        if new_node.g > tempg:
                            new_node.g = tempg
                    else:
                            open_list.append(new_node)
                if v.get() ==1:
                    if new_node.position != start and new_node.position != end:
                        new_node.visualize((255,255,0))
        

stop = False

while not stop:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    if  not stop:
        if v.get() == 1:
            time.sleep(0.1)
        else:
            pass
        main()











        
        
