CREATE TABLE rev_users(
    userid numeric NOT NULL,
    userrole character varying NOT NULL,
    firstname character varying NOT NULL,
    lastname character varying NOT NULL,
  	username character varying NOT NULL,	
  	user_password character varying NOT NULL,
    PRIMARY KEY(userid)
);

CREATE TABLE rev_journals(
    userid numeric NOT NULL,
    entry character varying NOT NULL,
    timesent time NOT NULL,
    datesent date NOT NULL,
    FOREIGN KEY(userid) REFERENCES rev_users(userid)
);