An Ambari 1.7+ Stack service package for the HBase REST gateway.

To deploy, copy the entire directory into your Ambari stacks folder and restart Ambari:

```
git clone https://github.com/laurentedel/hbaserest
sudo mv hbaserest /var/lib/ambari-server/resources/stacks/HDP/2.2/services/
sudo service ambari-server restart
```

Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard. 

If you want to delete the HBase REST gateway service from the Ambari services list:
```
curl -u $user:$pass -i -H 'X-Requested-By: ambari' -X DELETE http://$host:8080/api/v1/clusters/$cluster/services/HBASEREST
```

You'll maybe have to modify the script path in the service configuration as it's configured to /usr/hdp/current/hbase-client/bin/hbase-daemon.sh, meaning for HDP2.2+


Some parameters has to be added and configured accordingly in Ambari/HBASE (custom hbase-site) :

```
hbase.rest.authentication.kerberos.keytab=/etc/security/keytabs/spnego.service.keytab
hbase.rest.authentication.kerberos.principal=HTTP/_HOST@MYREALM
hbase.rest.authentication.type=kerberos
hbase.rest.info.port=8085
hbase.rest.kerberos.principal=hbase/_HOST@BDFG2PP2
hbase.rest.keytab.file=/etc/security/keytabs/hbase.service.keytab
hbase.rest.port=9091
hbase.rest.support.proxyuser=true
```
Good luck !
