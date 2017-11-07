-- -----------
-- Fri, 27 Oct
-- -----------

select "*** ID, name, and GPA of students who applied in CS ***";

select "*** #1 ***";
select "this is not right, why?";

select sID, sName, GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS';

select "*** #2 ***";
select "this is right";

select distinct sID, sName, GPA
    from Student
    inner join Apply using (sID)
    where major = 'CS';

select "*** #3 ***";
select "this is also right, using subquery, with in";

select sID, sName, GPA
    from Student
    where sID in
        (select sID
            from Apply
            where major = 'CS');

select "*** #4 ***";
select "and so is this";

select sID, sName, GPA
    from Student
    where sID in
        (select distinct sID
            from Apply
            where major = 'CS');
