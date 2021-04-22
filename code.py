peta = {'A':set(['B','C','D','F']),
         'B':set(['E','C']),
         'C':set(['A']),
         'D':set(['A','B']),
         'E':set(['C']),
         'F':set(['A'])}

def bfs(graph,start,end):
    queue=[[start]]
    visited=set()  
    while queue:
        rute=queue.pop(0) 
        
        state=rute[-1]
        print("state",state)
        
        
        if state==end: 
            print("rute BFS: ") 
            return rute


        elif state not in visited: 
            for cabang in graph.get(state,[]):
               
                newrute=list(rute)

                newrute.append(cabang)
                
                queue.append(newrute)
                

            visited.add(state) 
            
            

        isi=len(queue) 
        if isi==0:
            print("tidak di temukan")

def dfs(graph, start, end):
    stack=[[start]]
    visited=set()

    while stack:
       
        panjang_stack=len(stack)-1
        
        jalur=stack.pop(panjang_stack)
        
        state=jalur[-1]
        if state==end:
            print("rute DFS : ")
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
            
print(bfs(peta,'A','C'))
print(dfs(peta,'A','C'))