This is a simple project that takes in a file input and verifies if it is a csv file.
Once a csv file is received,it processes it and writes data to database.
There can be 2 types of users-customers and representatives- it writes data to corresponding mongodb collection(table) based on type(ID)- CRxx for customer,RPxx for representative.
The cluster was hosted on cloud-mongodb atlas and all necessary connections have been made
web interface and route was built using Flask and python
