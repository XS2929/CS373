-- ---------------
-- Aggregation.sql
-- ---------------

use test;

-- -----------------------------------------------------------------------
drop table if exists Student;
drop table if exists Apply;
drop table if exists College;

-- -----------------------------------------------------------------------
create table Student (
    sID    int,
    sName  text,
    GPA    float,
    sizeHS int);

create table Apply (
    sID      int,
    cName    text,
    major    text,
    decision boolean);

create table College (
    cName      text,
    state      char(2),
    enrollment int);

-- -----------------------------------------------------------------------
insert into Student values (123, 'Amy',    3.9,  1000);
insert into Student values (234, 'Bob',    3.6,  1500);
insert into Student values (320, 'Lori',   4.0,  2500);
insert into Student values (345, 'Craig',  3.5,   500);
insert into Student values (432, 'Kevin',  4.0,  1500);
insert into Student values (456, 'Doris',  3.9,  1000);
insert into Student values (543, 'Craig',  3.4,  2000);
insert into Student values (567, 'Edward', 2.9,  2000);
insert into Student values (654, 'Amy',    3.9,  1000);
insert into Student values (678, 'Fay',    3.8,   200);
insert into Student values (765, 'Jay',    2.9,  1500);
insert into Student values (789, 'Gary',   3.4,   800);
insert into Student values (876, 'Irene',  3.9,   400);
insert into Student values (987, 'Helen',  3.7,   800);

insert into Apply values (123, 'Berkeley', 'CS',             true);
insert into Apply values (123, 'Cornell',  'EE',             true);
insert into Apply values (123, 'Stanford', 'CS',             true);
insert into Apply values (123, 'Stanford', 'EE',             false);
insert into Apply values (234, 'Berkeley', 'biology',        false);
insert into Apply values (321, 'MIT',      'history',        false);
insert into Apply values (321, 'MIT',      'psychology',     true);
insert into Apply values (345, 'Cornell',  'bioengineering', false);
insert into Apply values (345, 'Cornell',  'CS',             true);
insert into Apply values (345, 'Cornell',  'EE',             false);
insert into Apply values (345, 'MIT',      'bioengineering', true);
insert into Apply values (543, 'MIT',       'CS',            false);
insert into Apply values (678, 'Stanford', 'history',        true);
insert into Apply values (765, 'Cornell',  'history',        false);
insert into Apply values (765, 'Cornell',  'psychology',     true);
insert into Apply values (765, 'Stanford', 'history',        true);
insert into Apply values (876, 'MIT',      'biology',        true);
insert into Apply values (876, 'MIT',      'marine biology', false);
insert into Apply values (876, 'Stanford', 'CS',             false);
insert into Apply values (987, 'Berkeley', 'CS',             true);
insert into Apply values (987, 'Stanford', 'CS',             true);

insert into College values ('Berkeley', 'CA', 36000);
insert into College values ('Cornell',  'NY', 21000);
insert into College values ('Irene',    'TX', 25000);
insert into College values ('MIT',      'MA', 10000);
insert into College values ('Stanford', 'CA', 15000);

-- -----------------------------------------------------------------------
select * from Student;
select * from Apply;
select * from College;

-- -----------------------------------------------------------------------
select "*** students, such that ***";
select "*** the number of other students with the same GPA equals ***";
select "*** the number of other students with the same high school size ***";

select "*** #1 ***";
select *
    from Student as R
    where
        (select count(*)
            from Student as S
            where (R.sID != S.sID) and (R.GPA = S.GPA))
        =
        (select count(*)
            from Student as S
            where (R.sID != S.sID) and (R.sizeHS = S.sizeHS))
    order by sID;

-- -----------------------------------------------------------------------
select "*** stats on GPA of students ***";

select "*** #2a ***";
select count(*) from Student;
select       *  from Student;

select "*** #2b ***";
select avg(GPA), max(GPA), min(GPA), sum(GPA)
    from Student;

-- -----------------------------------------------------------------------
select "*** stats on GPA of students applying to CS ***";

select "*** #3a ***";
select count(*)
    from Student
    where sID in (select sID from Apply where major = 'CS');
select *
    from Student
    where sID in (select sID from Apply where major = 'CS')
    order by GPA desc;

select "*** #3b ***";
select avg(GPA), max(GPA), min(GPA), sum(GPA)
    from Student
    where sID in (select sID from Apply where major = 'CS')
    order by GPA desc;

-- -----------------------------------------------------------------------
select "*** amount by which the average GPA of students applying to CS ***";
select "*** exceeds the average GPA of students not applying to CS ***";

select "*** #4a ***";
select *
    from
        (select avg(GPA) as gpa
            from Student
            where sID in
                (select sID
                    from Apply
                        where major = 'CS')) as R,
        (select avg(GPA) as gpa
            from Student
            where sID not in
                (select sID
                    from Apply
                        where major = 'CS')) as S;

select "*** #4b ***";
select R.gpa - S.gpa
    from
        (select avg(GPA) as gpa
            from Student
            where sID in
                (select sID
                    from Apply
                        where major = 'CS')) as R,
        (select avg(GPA) as gpa
            from Student
            where sID not in
                (select sID
                    from Apply
                        where major = 'CS')) as S;

-- -----------------------------------------------------------------------
select "*** college name and number of APPLICATIONS to that college ***";

select "*** #5a ***";
select count(*) from Apply;
select       *  from Apply order by cName;

select "*** #5b ***";
select *, count(*)
    from Apply
    group by cName;

select "*** #5c ***";
select cName, count(*)
    from Apply
    group by cName;

-- -----------------------------------------------------------------------
select "*** college name and number of APPLICANTS to that college ***";

select "*** #6a ***";
select count(*) from Apply;
select       *  from Apply order by cName;

select "*** #6b ***";
select cName, count(sID), count(distinct sID)
    from Apply
    group by cName;

-- -----------------------------------------------------------------------
select "*** stats on college enrollment by state ***";

select "*** #7a ***";
select count(*) from College;
select       *  from College order by state;

select "*** #7b ***";
select state, avg(enrollment), max(enrollment), min(enrollment), sum(enrollment)
    from College
    group by state;

-- -----------------------------------------------------------------------
select "*** stats on GPA of applicants to each college and major ***";

select "*** #8a ***";
select count(*) from Student inner join Apply using (sID);
select       *  from Student inner join Apply using (sID) order by cName, major;

select "*** #8b ***";
select cName, major, avg(GPA), max(GPA), min(GPA), max(GPA) - min(GPA)
    from Student
    inner join Apply using (sID)
    group by cName, major;

-- -----------------------------------------------------------------------
select "*** max spread between min and max GPA of applicants ***";
select "*** to each college and major ***";

select "*** #9a ***";
select max(x)
    from
        (select max(GPA) - min(GPA) as x
            from Student
            inner join Apply using (sID)
            group by cName, major) as T;

select "*** #9b ***";
select cName, major, avg(GPA), max(GPA), min(GPA), max(GPA) - min(GPA)
    from Student
    inner join Apply using (sID)
    group by cName, major
    having
        max(GPA) - min(GPA)
        =
		(select max(x)
			from
				(select max(GPA) - min(GPA) as x
					from Student
					inner join Apply using (sID)
					group by cName, major) as T);

-- -----------------------------------------------------------------------
select "*** number of colleges applied to by each student ***";

select "*** #10a ***";
select count(*) from Student inner join Apply using (sID);
select       *  from Student inner join Apply using (sID);

select "*** #10b ***";
select "does not include student who did not apply anywhere";

select sID, sName, count(distinct cName) as count_cName
    from Student
    inner join Apply using (sID)
    group by sID
    order by count(cName) desc;

select "*** #10c ***";
select "does include student who did not apply anywhere";

select sID, sName, count(distinct cName) as count_cName
    from Student
    inner join Apply using (sID)
    group by sID
union
select sID, sName, 0 as count_cName
    from Student
    where sID not in
        (select sID from Apply)
order by count_cName desc;

-- -----------------------------------------------------------------------
select "*** colleges with fewer than 5 APPLICATIONS ***";

select "*** #11a ***";
select cName, count(*)
    from Apply
    group by cName;

select "*** #11b ***";
select cName, count(*)
    from Apply
    group by cName
    having count(*) < 5;

-- -----------------------------------------------------------------------
select "*** colleges with fewer than 5 APPLICANTS ***";

select "*** #12a ***";
select cName, count(distinct sID)
    from Apply
    group by cName;

select "*** #12b ***";
select cName, count(distinct sID)
    from Apply
    group by cName
    having count(distinct sID) < 5;

-- -----------------------------------------------------------------------
select "*** majors whose applicant's max GPA is less than the average ***";

select "*** #13a ***";
select avg(GPA)
    from Student;

select "*** #13b ***";
select major, max(GPA)
    from Student
    inner join Apply using (sID)
    group by major;

select "*** #13c ***";
select major
    from Student
    inner join Apply using (sID)
    group by major
    having
        max(GPA)
        <
        (select avg(GPA) from Student);

-- -----------------------------------------------------------------------
drop table if exists Student;
drop table if exists Apply;
drop table if exists College;

exit
