from models.contact import Contact


x = Contact("Bob", "111-1111", "Bob@email.com")
y = Contact("Bobby", "112-1111", "Bobby@email.com")
print(x.name)
print(x == y)