
select rand() knt
go 5

create table sales1
(c1 varchar(20) not null,
c2 varchar(20) not null,
c3 varchar(20) not null,
date datetime not null
unique clustered (c2, c3))

exec sp_configure --system procedure
exec sp_columns Employees1 --column information 
exec xp_dirtree"C:\Users\Manish\Google Drive\ND\Career\me",0,1 --extended procedure
exec sp_helptext 'sp_configure' -- returns source code of the sp
exec sp_helptext xp_dirtree --points to a DLL
exec sp_help --lots of system information
exec sp_help Employees1 --info about a table
exec sp_helptrigger Employees1

--Create SP
select * from Production.Product
--CREATE PROC Sales
select schema_name(schema_id) as schemaname,
	name as procname
from sys.procedures

exec sp_help sp_MScleanupmergepublisher
go;
