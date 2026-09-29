marks(rahul,89).
marks(sita,56).
marks(suman,34).
marks(rohan,90).

%fail student

fail_student(student,Marks):-
    marks(student,Marks),
    Marks >= 45.

