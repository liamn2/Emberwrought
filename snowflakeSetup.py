from snowflake.snowpark import Session
from snowflake.core import Root

session = Session.builder.config("connection_name", "default").create()
root = Root(session)

snowflake.core()		# Pull resource from Snowflake
snowflake.core.database() 	# Access databases
snowflake.core.schema()		# Access Schemum
snowflake.core.table()		# Access tables
snowflake.core.task()		# Access tasks
snowflake.core.task.dagv1()	# Access higher level task for better DAG
snowflake.core.compute_pool()	# Manage compute pools in Snowpark Container
				  Services (SCS)
snowflake.core.image_repository	# Manage image repositories in SCS
snowflakek.core.service() 	# Manage services in SCS
