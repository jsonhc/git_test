select a.tablespace_name,a.bytes/1024/ 1024 "Sum MB",(a.bytes-b.bytes)/1024 /1024 "used MB"
,b.bytes/ 1024/1024 "free MB",round(((a.bytes-b.bytes)/a.bytes)*100 ,2
) "percent_used"
from 
(select tablespace_name, sum(bytes) bytes from dba_data_files group by tablespace_name) a,
(select tablespace_name, sum(bytes) bytes,max (bytes) largest from dba_free_space
 group by tablespace_name) b
where a.tablespace_name=b.tablespace_name


# 以下是拆分上面的sql
SQL> select TABLESPACE_NAME,sum(bytes) as total_bytes from dba_data_files  group by TABLESPACE_NAME;
TABLESPACE_NAME                TOTAL_BYTES
------------------------------ -----------
UNDOTBS1                         304087040
SYSAUX                           723517440
USERS                              5242880
SYSTEM                           723517440
TESTTBS                           31457280
SQL> select tablespace_name,sum(bytes) free_bytes from dba_free_space group by tablespace_name ;
TABLESPACE_NAME                FREE_BYTES
------------------------------ ----------
SYSAUX                          118751232
UNDOTBS1                        290586624
USERS                             2621440
SYSTEM                            2883584
TESTTBS                          29360128
