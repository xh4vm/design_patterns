# Abstract Factory

> Information taken from [resources](https://refactoring.guru/design-patterns/abstract-factory)

## Intent

**Abstract** Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-en.png?id=d0210ee255712a245fead94a3fafabe0)

## Problem

Imagine that you’re creating a furniture shop simulator. Your code consists of classes that represent:

1. A family of related products, say: `Chair` + `Sofa` + `CoffeeTable`.
2. Several variants of this family. For example, products `Chair` + `Sofa` + `CoffeeTable` are available in these variants: `Modern`, `Victorian`, `ArtDeco`.

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/problem-en.png?id=e38c307511e684828be898de02d6c268)

You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite mad when they receive non-matching furniture.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-comic-1-en.png?id=f4012920c5034122eedbb0c9fec0cdb3)

Also, you don’t want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs very often, and you wouldn’t want to change the core code each time it happens.

## Solution

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., chair, sofa or coffee table). Then you can make all variants of products follow those interfaces. For example, all chair variants can implement the `Chair` interface; all coffee table variants can implement the `CoffeeTable` interface, and so on.

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution1.png?id=71f2018d8bb443b9cce90d57110675e3)

The next move is to declare the __Abstract Factory__—an interface with a list of creation methods for all products that are part of the product family (for example, `createChair`, `createSofa` and `createCoffeeTable`). These methods must return **abstract** product types represented by the interfaces we extracted previously: `Chair`, `Sofa`, `CoffeeTable` and so on.

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2.png?id=53975d6e4714c6f942633a879f7ac571)

Now, how about the product variants? For each variant of a product family, we create a separate factory class based on the `AbstractFactory` interface. A factory is a class that returns products of a particular kind. For example, the `ModernFurnitureFactory` can only create `ModernChair`, `ModernSofa` and `ModernCoffeeTable` objects.

The client code has to work with both factories and products via their respective abstract interfaces. This lets you change the type of a factory that you pass to the client code, as well as the product variant that the client code receives, without breaking the actual client code.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-comic-2-en.png?id=fbce1a263acfefc76074fd20fae7b8c3)

Say the client wants a factory to produce a chair. The client doesn’t have to be aware of the factory’s class, nor does it matter what kind of chair it gets. Whether it’s a Modern model or a Victorian-style chair, the client must treat all chairs in the same manner, using the abstract `Chair` interface. With this approach, the only thing that the client knows about the chair is that it implements the `sitOn` method in some way. Also, whichever variant of the chair is returned, it’ll always match the type of sofa or coffee table produced by the same factory object.

There’s one more thing left to clarify: if the client is only exposed to the abstract interfaces, what creates the actual factory objects? Usually, the application creates a concrete factory object at the initialization stage. Just before that, the app must select the factory type depending on the configuration or the environment settings.

More information on [resource](https://refactoring.guru/design-patterns/abstract-factory)