drop table if exist entries;

CREATE TABLE tblDisasterEvent(
    id integer primary key autoincrement,
    title text not null,
    date text not null
);