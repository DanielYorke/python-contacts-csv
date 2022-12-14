class Contact:
    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
    
    def __eq__(self , other) -> bool:
        if isinstance(other,Contact):
            return self.name == other.name
        return False

    def __str__(self) -> str:
        return self.name + "\t" + self.phone + "\t" + self.email + "\n"