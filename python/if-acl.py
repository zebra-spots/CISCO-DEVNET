aclNUM = int(input("What is the IPv4 ACL number? "))
if aclNUM >= 1 and aclNUM <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNUM >=100 and aclNUM <= 199:
    print("This is an extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
