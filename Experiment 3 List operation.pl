mylist([1,2,3,4,5]).
list_hpt([Head,P|Tail],Head,P,Tail).
list_h([Head|_],Head).

search(N):-
    mylist(X),
    member(N,X).

length_list(X,N):-
    length(X,N).

append([],L,L). 
append([Head|Tail],L,[Head|Result]):-
    append(Tail,L,Result).

reverse([],[]).
reverse([Head],[Tail],Result):-
    reverse(Tail,Result1),
    append(Result1,[Head],Result).