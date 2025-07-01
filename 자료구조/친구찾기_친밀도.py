def print_all_friends(g,start) :
    qu=[]
    done=set()
    qu.append([start,0])
    done.add(start)
    while qu :
        now = qu.pop(0)
        print(now[0],now[1])
        for friend in g[now[0]] :
            if not friend in done :
                qu.append([friend,now[1]+1])
                done.add(friend)

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')