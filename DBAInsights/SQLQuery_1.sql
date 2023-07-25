create database BotecoDBADB
GO

use BotecoDBADB
GO


CREATE table pedido
(

npedido int,
comida VARCHAR(50),
bebida VARCHAR(50)

)

select *
from pedido


select @@SERVERNAME
select @@SERVICENAME


SELECT DISTINCT dovs.logical_volume_name AS LogicalName,
dovs.volume_mount_point AS Drive,
CONVERT(INT,dovs.available_bytes/1048576.0) AS FreeSpaceInMB
FROM sys.master_files mf
CROSS APPLY sys.dm_os_volume_stats(mf.database_id, mf.FILE_ID) dovs
ORDER BY FreeSpaceInMB ASC
GO

SELECT session_id,wait_duration_ms,wait_type FROM sys.dm_os_waiting_tasks order by wait_duration_ms desc