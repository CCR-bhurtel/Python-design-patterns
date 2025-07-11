class Target:
    def request(self)->str:
        return "Target: the default target's behavour."
    

class Adaptee:
    def specific_request(self)->str:
        return ".eetpadA eht fo roivaheb laicepS"
    

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
        
    def request(self)->str:
        return f'Adapter: (TRANSLATED){self.adaptee.specific_request()[::-1]}'
    
def client_code(target: Target)->None:
    print(target.request(), end="")

if __name__ == "__main__":
    print("Client: I can work just find with the Target objects:")
    
    target = Target()
    client_code(target)
    print("\n")
    

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    
    adapter = Adapter(adaptee)
    client_code(adapter)