# Get all the accounts of Zimbra and print Firstname, Lastname.
for i in `zmprov -l gaa`; zmprov -l ga $i givenName sn; done; 
# Display all the distribution lists along with verbose information.
zmprov -l gadl -v
