edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(d,h).
edge(d,j).
edge(e,i).
dfs(Start,Goal,Spath):-
    dfs(Start,Goal,Spath).
dfs_search(Goal,Goal,[Goal]).

dfs_search(Node,Goal,[Node|Path]):-
    edge(Node,Next),
    dfs_search(Next,Goal,Path).
    