#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import os

queries = mysqlQueries.split(";")
#print queries

for q in queries:
    # execute queries
    db1 = os.system(mysqlServer['mysqlHome'] + "mysql -h " + mysqlServer['url'] + " -D " + mysqlServer['schema'] + " -u " + mysqlServer['username'] + " -p" + mysqlServer['password'] + " -A -e '" + q.replace("\n" ,"").replace("'", "\'") + "'")
    os.system("exit")  # close client
    print 'Successfully ran the query: ',  q
