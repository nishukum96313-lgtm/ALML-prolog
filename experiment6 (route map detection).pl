%direct connection
road(delhi,agra).
road(agra,gwalior).
road(gwalior,bhopal).
road(delhi,jaipur).
road(jaipur,ajmer).

%route recommendation
%direct route
travel(X,Y):-
    road(X,Y).
%query(travel(delhi,Y)


%indirect route
travel(X,Y):-
    road(X,Z),
    travel(Z,Y).
%query(travel(delhi,Y)