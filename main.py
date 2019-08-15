from com.deluxe.datascience.metadatamanager.apiconsumer import Apiconsumer

a = Apiconsumer()

# Authentication
a.authenticate('admin', 'adminadmin112')

# Getting all Origins
origins = a.getOrigins()
print('ORIGIN: ', origins[1])

# Getting databases in an origin
databases = a.getDatabaes(origins[1]['idh'])
print('DB: ', databases[3])

# Getting schemas
schemas = a.getSchemas(databases[3]['idh'])
print('SCHEMA: ', schemas[0])

# Getting tables in a database
tables = a.getTables(schemas[0]['idh'])
print('TABLES: ')
for table in tables:
    print('  - ' + table['name'])

# Getting fields in a table
fields = a.getFields(tables[10]['idh'])
# displaying one of the field config
print(fields[5])
