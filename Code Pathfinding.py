#!/usr/bin/env python
# coding: utf-8

# In[9]:


peta = {'S':set(['A','B']),
         'A':set(['C']),
         'B':set(['C','D']),
         'C':set(['D','E']),
         'D':set(['E'])}

def bfs(graph,start,end):
    queue=[[start]]                                  #queue untuk mengambil start yang diinput
    visited=set()                                    #membuat variable visited untuk set()
    
    while queue:                                     #untuk while sebanyak queue
        rute=queue.pop(0)                            #var rute dibuat untuk mengambil queue yang telah di pop
        print("rute :",rute)
        state=rute[-1]                               #var state dibuat untuk mengambil isi var rute
        #print("-1 :",state)
        if state==end:                               #jika start = end maka akan return
            return rute

        elif state not in visited:                   #jika state belum pernah visited atau state != visited
            for cabang in graph.get(state,[]):       #for sebanyak statenya
                newrute=list(rute)                   #var newrute dibuat untuk mengisi list rute
                
                newrute.append(cabang)               #isi newrute digabunggkan dengan isi cabang
                
                queue.append(newrute)                #isi queue digabunggkan dengan isi newrute
                
            visited.add(state)                       #gunanya menyimpan kota yang telah dikunjungi
    
        isi=len(queue)               #berguna mencegah jika diinput start = 0 atau tidak ada maka akan muncul tidak ditemukan
        if isi==0:
            print("tidak di temukan")

def dfs(graph, start, end):
    stack=[[start]]
    visited=set()

    while stack:
       
        panjang_stack=len(stack)-1                   #var panjang_stack dibuat dan memiliki isi dari len(stack)-1
        jalur=stack.pop(panjang_stack)               #var jalur dibuat dan memiliki isi stack.pop(panjang_stack)
        print("Jalur :",jalur)
        state=jalur[-1]                              #var state dubuat untuk mengambil isi var jalur
        
        if state==end:
            return jalur
        elif state not in visited:
            for cabang in graph.get(state, []):
                jalur_baru = list(jalur)
                jalur_baru.append(cabang)
                stack.append(jalur_baru)
           
            visited.add(state)
       
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
            
print("BFS :",bfs(peta,'S','E'))
print("DFS :",dfs(peta,'S','E'))


# In[ ]:





# In[ ]:





# In[ ]:




