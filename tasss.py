import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8000")
print("3 é par: %s" % str(s.is_even(3)))
print("100 é par: %s" % str(s.is_even(100)))
    
    
   