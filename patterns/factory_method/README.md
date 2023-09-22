# Factory method

> Information taken from [resources](https://refactoring.guru/design-patterns/abstract-factory)

## Intent

**Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

![](https://refactoring.guru/images/patterns/content/factory-method/factory-method-en.png?id=cfa26f33dc8473e803fadae0d262100a)

## Problem

Imagine that you’re creating a logistics management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the `Truck` class.

After a while, your app becomes pretty popular. Each day you receive dozens of requests from sea transportation companies to incorporate sea logistics into the app.

![](https://refactoring.guru/images/patterns/diagrams/factory-method/problem1-en.png?id=de638561be0bbb1025ada6bfcb815def)

Great news, right? But how about the code? At present, most of your code is coupled to the `Truck` class. Adding `Ships` into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

As a result, you will end up with pretty nasty code, riddled with conditionals that switch the app’s behavior depending on the class of transportation objects.

## Solution

The Factory Method pattern suggests that you replace direct object construction calls (using the `new` operator) with calls to a special __factory__ method. Don’t worry: the objects are still created via the `new` operator, but it’s being called from within the factory method. Objects returned by a factory method are often referred to as products.

![](https://refactoring.guru/images/patterns/diagrams/factory-method/solution1.png?id=fc756d2af296b5b4d482e548214d08ef)

At first glance, this change may look pointless: we just moved the constructor call from one part of the program to another. However, consider this: now you can override the factory method in a subclass and change the class of products being created by the method.

There’s a slight limitation though: subclasses may return different types of products only if these products have a common base class or interface. Also, the factory method in the base class should have its return type declared as this interface.

![](https://refactoring.guru/images/patterns/diagrams/factory-method/solution2-en.png?id=db5de848c1d490b835666ef54d131d46)

For example, both `Truck` and `Ship` classes should implement the `Transport` interface, which declares a method called `deliver`. Each class implements this method differently: trucks deliver cargo by land, ships deliver cargo by sea. The factory method in the `RoadLogistics` class returns truck objects, whereas the factory method in the `SeaLogistics` class returns ships.

![](https://refactoring.guru/images/patterns/diagrams/factory-method/solution3-en.png?id=b6f53911fc0d56f9ef99501fc4aec059)

The code that uses the factory method (often called the client code) doesn’t see a difference between the actual products returned by various subclasses. The client treats all the products as abstract `Transport`. The client knows that all transport objects are supposed to have the `deliver` method, but exactly how it works isn’t important to the client.

More informations on [resource](https://refactoring.guru/design-patterns/factory-method)