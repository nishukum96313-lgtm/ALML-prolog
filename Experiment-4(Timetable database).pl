timetable(monday,    '9:00',  aiml,    aradhana,   room101).
timetable(monady,    '10:00', python,  ishita,    room102).
timetable(tuesday,   '9:00',  aiml,    ishita,    room101).
timetable(tuesday,   '10:00', dsa,     suryamani, room102).
timetable(wednesday, '9:00',  prolog,  aradhana,   lab1).
timetable(wednesday, '10:00', python,  aradhana,   room103).

%faculty schedule

faculty_schedule(Faculty,Day,Time,Subject,RoomNo):-
    timetable(Day,Time,Subject,Faculty,RoomNo).

%teaching subject
 subject_name(Subject,Faculty):-
    timetable(_,_,Subject,Faculty,_).

%class roomNo
room_no(RoomNo,Faculty):-
    timetable(_,_,_,Faculty,RoomNo).


