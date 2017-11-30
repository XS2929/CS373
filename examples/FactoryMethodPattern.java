// -------------------------
// FactoryMethodPattern.java
// -------------------------

// https://en.wikipedia.org/wiki/Factory_method_pattern

import java.util.ArrayList;
import java.util.List;

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

class Room {}
class EnchantedRoom extends Room {}

class Door {
    private Room _r;
    private Room _s;

    public Door (Room r, Room s) {
        _r = r;
        _s = s;}}

class EnchantedDoor extends Door {
    public EnchantedDoor (Room r, Room s) {
        super(r, s);}}

final class Maze {
    private List<Room> _rooms = new ArrayList<Room>();
    private List<Door> _doors = new ArrayList<Door>();

    public void addRoom (Room r) {
        _rooms.add(r);}

    public void addDoor (Door d) {
        _doors.add(d);}

    public Room room (int i) {
        return _rooms.get(i);}

    public Door door (int i) {
        return _doors.get(i);}}

class Game {
    public final Maze createMaze () {
        Maze m = new Maze();
        m.addRoom(makeRoom());
        m.addRoom(makeRoom());
        m.addRoom(makeRoom());
        m.addDoor(makeDoor(m.room(0), m.room(1)));
        m.addDoor(makeDoor(m.room(1), m.room(2)));
        return m;}

    public Room makeRoom () {
        return new Room();}

    public Door makeDoor (Room r, Room s) {
        return new Door(r, s);}}

class EnchantedGame extends Game {
    public EnchantedRoom makeRoom () {
        return new EnchantedRoom();}

    public EnchantedDoor makeDoor (Room r, Room s) {
        return new EnchantedDoor(r, s);}}

public final class FactoryMethodPattern extends TestCase {
    public void test_1 () {
        Game g = new Game();
        Maze m = g.createMaze();
        assertEquals(Game.class,         g.getClass());
        assertEquals(Maze.class,         m.getClass());
        assertEquals(Room.class, m.room(0).getClass());
        assertEquals(Door.class, m.door(0).getClass());}

    public void test_2 () {
        Game g = new EnchantedGame();
        Maze m = g.createMaze();
        assertEquals(EnchantedGame.class, g.getClass());
        assertEquals(Maze.class,          m.getClass());
        assertEquals(EnchantedRoom.class, m.room(0).getClass());
        assertEquals(EnchantedDoor.class, m.door(0).getClass());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(FactoryMethodPattern.class));}}
