class Publisher:
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        return f"{subscriber} has successfully subscribed!"

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
        return f"{subscriber} has successfully unsubscribed"

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

class Subscriber:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")

def demo():
    publisher = Publisher()
    sub_one = Subscriber("Grant")
    sub_two = Subscriber("Ralph")
    sub_three = Subscriber("Sonya")
    publisher.subscribe(sub_one)
    publisher.subscribe(sub_two)
    publisher.subscribe(sub_three)
    publisher.notify("A new video has been uploaded!")
    publisher.unsubscribe(sub_three)
    publisher.notify("Yet another video has been uploaded!")

if __name__ == "__main__":
    demo()
    
