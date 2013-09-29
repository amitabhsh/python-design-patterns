Design Patterns in Python
-------------------------

I lost touch with my python skills so i have decided to write up all the design patterns in Python and Java at the same time.
Since i have been using Java since some time, it made sense to write a program first in Java and then try to write the same in Python,
this exposes me changes in the language syntax and other built-in objects required for the same functionality.

I'll use this Markdown to document these changes along with What(tl;dr for the pattern), When (to use it), How the Pattern is Implemented in the example

*   *Factory Pattern*
    <p>
     1. What : Works as a Factory, providing different type of objects. Think of it as a *Central* Object creation class for the entire application.
     2. When : When we have multiple classes with different behavior, it makes sense to centralize them into a one or more classes. Imagine all DAO objects created from a single Factory.We'll only need to modify a single class instead of modifying all in case something changes.
     3. How :
        <p> *Scenario* : Write a simple logger that can write to File, Console but should be flexible to open to writing to a database , Stream or a Messaging Queue in Future.
             ConsoleLogger() : Implements a Log method which prints a string to console
             FileLogger(): Implements a Log method which writes a string to File
             DateClass() : Exposes a static method using which any class can get current datetime.
             LogFactory(): Reads the config file to check if the logger required is console or File. and then returns the object
        </p>
        *Java to Python*
        <p>
        - To read the properties file i typicall used java.util packages to read the properties file. There are ways around to doing the same but python has a built in
        module called ConfigParser. This can be used to read the config files with .ini extension.
        A config file is structured as following
        [section]
        parametername=value
        [section2]
        parametername=value
        </p>
</p>

