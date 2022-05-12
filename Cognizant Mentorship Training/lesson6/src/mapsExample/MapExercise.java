package mapsExample;

import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

public class MapExercise {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Person p1 = new Person("John", "john@google.com");
        Person p2 = new Person("Mary", "mary@google.com");
        Person p3 = new Person("John", "john@udacity.com");
        Person p4 = new Person("Mary", "mary@udacity.com");

        Map<String, Person> map = new HashMap<String, Person>();
        map.put(p1.getName(), p1);
        map.put(p2.getName(), p2);
        map.put(p3.getName(), p3);
        map.put(p4.getName(), p4);

        System.out.println(map.get(p1.getName()));
        System.out.println(map.get(p2.getName()));
        System.out.println(map.get(p3.getName()));
        System.out.println(map.get(p4.getName()));

        System.out.println(map.get(p1.getName()).getEmail());
        System.out.println(map.get(p2.getName()).getEmail());
        System.out.println(map.get(p3.getName()).getEmail());
        System.out.println(map.get(p4.getName()).getEmail());

        System.out.println(map.get(p1.getName()).getName());
        System.out.println(map.get(p2.getName()).getName());
        System.out.println(map.get(p3.getName()).getName());
        System.out.println(map.get(p4.getName()).getName());

        System.out.println(map.get(p1.getName()).toString());
        System.out.println(map.get(p2.getName()).toString());
        System.out.println(map.get(p3.getName()).toString());
        System.out.println(map.get(p4.getName()).toString());

        Map<String, Person> mapOfPeople = new HashMap<String, Person>();
        Person mike = new Person("Mike", "mike@email.com");
        Person shaun = new Person("Shaun", "shaun@email.com");
        Person sally = new Person("Sally", "sally@email.com");
        Person cesar = new Person("Cesar", "cesar@email.com");

        ArrayList<Person> people = new ArrayList<Person>();
        people.add(mike);
        people.add(shaun);
        people.add(sally);
        people.add(cesar);

        for (Person person : people) {
            mapOfPeople.put(person.getName(), person);
        }

        for (String email : mapOfPeople.keySet()) {
            System.out.println(email);
        }

        for (Person person : mapOfPeople.values()) {
            System.out.println(person);
        }

        System.out.println("Get Mike: " + mapOfPeople.get("mike@email.com"));
        System.out.println("Get Jeff: " + mapOfPeople.get("jeff@email.com"));
        System.out.println("Contains Mike: " + mapOfPeople.containsKey("mike@email.com"));
        System.out.println("Contains Jeff: " + mapOfPeople.containsKey("jeff@email.com"));

    }

    private static void addToMap(Map<String, Person> map, Person person) {
        map.put(person.getEmail(), person);
    }

}
