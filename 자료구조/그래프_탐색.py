def bfs(g, start) :
    qu=[]
    done=set()
    qu.append(start)
    done.add(start)
    while qu :
        now = qu.pop()
        print(now)
        for i in g[now]:
            if not i in done :
                qu.append(i)
                done.add(i)

g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(g, 1)