// -----------
// Mon, 13 Nov
// -----------

/*
In Java
    overriding
    abstract classes and methods
    dynamic binding
*/

class A {
    public abstract void f (int);}

class B extends A {
    ...}

class T {
    public static void main (...) {
        A x = new A(); // not ok
        A x = new B();

/*
consequences of an abstract method in A
    A becomes abstract
    B must either define f() or become abstract
    A is prohibited from defining f()
*/

final class A {
    public void f (int) {...}}

class B extends A {
    public void f (int) {...}}

class C extends A {
    public void f (int) {...}}

class T {
    public static void main (...) {
        A x;
        if (...)
            x = new B();
        else
            x = new C();
        x.f(2);

/*
where does Java behave statically?
    static method
    final method
    final class
    private methods
*/

class A {}

class B {
    private static B x;

    private B () {}

    public static B only () {
        if (x == null)
            x = new B();
        return x;}}

class T {
    public static void main (...) {
        A x = new A();
        A y = new A();
        s.o.p(x == y); // false

        B z = new B();               // not ok
        s.o.p(B.only() == B.only()); // true






















