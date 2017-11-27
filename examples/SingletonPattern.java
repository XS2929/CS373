// ---------------------
// SingletonPattern.java
// ---------------------

class Eager {
    private static final Eager _only = new Eager();

    private Eager ()
        {}

    public static Eager only () {
        return _only;}

    public String f () {
        return "Eager.f()";}}

class Lazy1 {
    private static Lazy1 _only;

    private Lazy1 ()
        {}

    public static Lazy1 only () {
        if (Lazy1._only == null)
            Lazy1._only = new Lazy1();
        return Lazy1._only;}

    public String f () {
        return "Lazy1.f()";}}

class Lazy2 {
    private Lazy2 ()
        {}

    private static class Holder {
        private static final Lazy2 _only = new Lazy2();}

    public static Lazy2 only () {
        return Holder._only;}

    public String f () {
        return "Lazy2.f()";}}

public final class SingletonPattern {
    public static void test () {
    	assert(Eager.only()     == Eager.only());
    	assert(Eager.only().f() == "Eager.f()");

    	assert(Lazy1.only()     == Lazy1.only());
    	assert(Lazy1.only().f() == "Lazy1.f()");

    	assert(Lazy2.only()     == Lazy2.only());
    	assert(Lazy2.only().f() == "Lazy2.f()");}

    public static void main (String[] args) {
        System.out.println("SingletonPattern.java");
        test();
        System.out.println("Done.");}}
