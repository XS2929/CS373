// -----------
// Fri, 17 Nov
// -----------

abstract class A {
    void          f (long) {...} // runtime logic error
    final void    g (long) {...}
    abstract void h (long);}

class B extends A {
    void f (int) {...}
    void h (int) {...}} // not ok

class T {
    public static void main (...) {
        A x = new B();
        x.f(2);                     // A.f

/*
override a method for dynamic binding
you to have to respect the signature of the method

return type
name
number of args
types of args
*/

class Class {
    /*
    only Jave makes instances of class Class
    those instances are singletons
    */

    static Class forName (String s) {
        ...}

    Object newInstance () {
        ...}}

class A {
    /*
    causes Jave to instantiate an instance of class Class
    that describes class A
    */
    }

class T {
    public static void main (...) {
        Class c = A.class;            // class is a static data member

        A x = new A();
        Class d = x.getClass();       // getClass() is an instance method
        s.o.p(c == d);                // True

        Class e = Class.forName("A");
        s.o.p(c == e);                // True

        A y = (A) e.newInstance();    // newInstance() is an instance method
        A z = (A) e.newInstance();
        s.o.p(y == z);                // False

abstract class A {...}

interface A {...}

class A {
    private A () {}}

class A {
    A (int) {...}}
