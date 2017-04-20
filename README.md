# Preface #

This document describes the functionality provided by the xlr-mysql-query-plugin
See the **XL Release Reference Manual** for background information on XL Release and release concepts.


# Overview #

The xlr-mysql-query-plugin is an XL Release plugin that adds capability for running mysql queries at different points during a release.  Simply paste your queries in the text box with the correct syntax, separated by semi-colons and they will run when the task is started during your pipeline release.

* **XL Release requirements**
	* **XL Release**: version 6.0+
	* **MySQL Server Configuration Item**: The MySQL server connections must be stored as configuration items in XL Release including the local path to the msyql client.  (i.e. /usr/local/mysql/bin/)
	* **MySQL Client**: MySQL Client must be installed on the XL Release server for remotely connecting to the database.
	
## Types ##

+ xlr.MysqlQueries: runs each query.  Separate the queries in the text box by semi-colon. Queries can contain XL Release variables.  Syntax of queries must be correct including backticks around table names and double quotes around values.
# xlr-mysql-query-plugin
