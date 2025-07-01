def print_all_friends(g,start) :
    qu=[]
    done=set()
    qu.append(start)
    done.add(start)
    while qu :
        now = qu.pop(0)
        print(now)
        for friend in g[now] :
            if friend not in done :
                qu.append(friend)
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