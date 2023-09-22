# Adapter

> Information taken from [resources](https://refactoring.guru/design-patterns/adapter)

## Intent

**Adapter** is a structural design pattern that allows objects with incompatible interfaces to collaborate.

![](https://refactoring.guru/images/patterns/content/adapter/adapter-en.png?id=11ef6ae6177291834323e3f918c47cd2)

## Problem

Imagine that you’re creating a stock market monitoring app. The app downloads the stock data from multiple sources in XML format and then displays nice-looking charts and diagrams for the user.

At some point, you decide to improve the app by integrating a smart 3rd-party analytics library. But there’s a catch: the analytics library only works with data in JSON format.

![](https://refactoring.guru/images/patterns/diagrams/adapter/problem-en.png?id=60d01f6c72ba85030cd52d5955caa3d8)

You could change the library to work with XML. However, this might break some existing code that relies on the library. And worse, you might not have access to the library’s source code in the first place, making this approach impossible.

## Solution

You can create an __adapter__. This is a special object that converts the interface of one object so that another object can understand it.

An adapter wraps one of the objects to hide the complexity of conversion happening behind the scenes. The wrapped object isn’t even aware of the adapter. For example, you can wrap an object that operates in meters and kilometers with an adapter that converts all of the data to imperial units such as feet and miles.

Adapters can not only convert data into various formats but can also help objects with different interfaces collaborate. Here’s how it works:

1. The adapter gets an interface, compatible with one of the existing objects.
2. Using this interface, the existing object can safely call the adapter’s methods.
3. Upon receiving a call, the adapter passes the request to the second object, but in a format and order that the second object expects.

Sometimes it’s even possible to create a two-way adapter that can convert the calls in both directions.

![](https://refactoring.guru/images/patterns/diagrams/adapter/solution-en.png?id=5f4f1b4575236a3853f274b690bd6656)

Let’s get back to our stock market app. To solve the dilemma of incompatible formats, you can create XML-to-JSON adapters for every class of the analytics library that your code works with directly. Then you adjust your code to communicate with the library only via these adapters. When an adapter receives a call, it translates the incoming XML data into a JSON structure and passes the call to the appropriate methods of a wrapped analytics object.

## Real-World Analogy

![](https://refactoring.guru/images/patterns/content/adapter/adapter-comic-1-en.png?id=c3842e3fff878a5b93e3186606998fc6)

When you travel from the US to Europe for the first time, you may get a surprise when trying to charge your laptop. The power plug and sockets standards are different in different countries. That’s why your US plug won’t fit a German socket. The problem can be solved by using a power plug adapter that has the American-style socket and the European-style plug.

More informations on [resource](https://refactoring.guru/design-patterns/adapter)