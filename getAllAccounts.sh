# Get all the accounts of Zimbra and print Firstname, Lastname.
for i in `zmprov -l gaa`; zmprov -l ga $i givenName sn; done; 
# adding another two lines on master.
