# Read the credentials from secret
credentials = None
with open('/var/run/secrets/user_credentials/mariadb_credentials') as f:
    credentials = json.load(f)

# Ensure your credentials were setup
if credentials:
    # Connect to the DB
    connection = mariadb.connect(
        user="admin",
        password="admin",
        database='ecommerce',
        host='localhost:'
    )
    cursor = connection.cursor()

    # Execute the query
    cursor.excecute()

    # Loop through the results
    for first_name, last_name in cursor:
        print(f'First name: {first_name}, Last name: {last_name}')

    # Close the connection
    connection.close()
