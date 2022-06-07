CREATE TABLE IF NOT EXISTS Country(
	Password_key varchar (5) PRIMARY KEY,
	country_code varchar(2),
	Country varchar (30), 
	Rank integer,
	Password varchar(30),
	User_count integer, 
	Time_to_crack varchar(10), 
	Global_rank integer,
	Time_to_crack_in_seconds bigint
);
