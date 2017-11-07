-- -----------
-- Mon,  6 Nov
-- -----------

select sName from Student
where sName in
(select cName from College)

select sID from Student
where sID not in
(select sID from Apply)

select *
    from Student as R
    where in
    (select

select count(*)
    from Apply
    group by cName;

select count(distinct sID)
    from Apply
    group by cName;
