'''The “L” in SOLID is for Liskov Substitution Principle, which states that subclases(Derived) should be 
 substitutable for the classes from which they were derived. For example, if MySubclass is a subclass of 
 MyClass, you should be able to replace MyClass with MySubclass without bunging up the program.'''

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass

class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')

class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception('The notification is not supported')

if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')
    notification_manager = NotificationManager(SMS(), contact)
    notification_manager.send('Hello John')

# correct and redesigned version of the problem which does not violate the LSP
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)

if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    notification_manager.notification = email_notification
    notification_manager.send('Hi John')


# C++ example just to get more idea how we should think and find the inheritance does violate LSP or not
struct Rectangle {
    Rectangle(const uint32_t width, const uint32_t height) : m_width{width}, m_height{height} {}

    uint32_t get_width() const { return m_width; }
    uint32_t get_height() const { return m_height; }

    virtual void set_width(const uint32_t width) { this->m_width = width; }
    virtual void set_height(const uint32_t height) { this->m_height = height; }

    uint32_t area() const { return m_width * m_height; }

protected:
    uint32_t m_width, m_height;
};

struct Square : Rectangle {
    Square(uint32_t size) : Rectangle(size, size) {}
    void set_width(const uint32_t width) override { this->m_width = m_height = width; }
    void set_height(const uint32_t height) override { this->m_height = m_width = height; }
};

void process(Rectangle &r) {
    uint32_t w = r.get_width();
    r.set_height(10);

    assert((w * 10) == r.area()); // Fails for Square <--------------------
}

int main() {
    Rectangle r{5, 5};
    process(r);
    Square s{5};
    process(s);
    return EXIT_SUCCESS;
}

# correct way of thinking for the problem which does adheres the LSP
struct Shape {
    virtual uint32_t area() const = 0;
};

struct Rectangle : Shape {
    Rectangle(const uint32_t width, const uint32_t height) : m_width{width}, m_height{height} {}

    uint32_t get_width() const { return m_width; }
    uint32_t get_height() const { return m_height; }

    virtual void set_width(const uint32_t width) { this->m_width = width; }
    virtual void set_height(const uint32_t height) { this->m_height = height; }

    uint32_t area() const override { return m_width * m_height; }

private:
    uint32_t m_width, m_height;
};

struct Square : Shape {
    Square(uint32_t size) : m_size(size) {}
    void set_size(const uint32_t size) { this->m_size = size; }
    uint32_t area() const override { return m_size * m_size; }

private:
    uint32_t m_size;
};

void process(Shape &s) {
    // Use polymorphic behaviour only i.e. area()
}

