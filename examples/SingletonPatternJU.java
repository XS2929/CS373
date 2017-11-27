// -----------------------
// SingletonPatternJU.java
// -----------------------

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

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

public final class SingletonPatternJU extends TestCase {
    public void test_1 () {
    	assertEquals(Eager.only(), Eager.only());}

    public void test_2 () {
    	assertEquals( "Eager.f()", Eager.only().f());}

    public void test_3 () {
    	assertEquals(Lazy1.only(), Lazy1.only());}

    public void test_4 () {
    	assertEquals("Lazy1.f()", Lazy1.only().f());}

    public void test_5 () {
    	assertEquals(Lazy2.only(), Lazy2.only());}

    public void test_6 () {
    	assertEquals("Lazy2.f()", Lazy2.only().f());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(SingletonPatternJU.class));}}
