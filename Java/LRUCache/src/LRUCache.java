import java.util.HashMap;
import java.util.LinkedList;

public class LRUCache {
    private int capacity;
    LinkedList<Integer> nodos;
    HashMap<Integer,Integer> keysValues;

        LRUCache(int capacity){
            this.capacity = capacity;
            nodos = new LinkedList<>();
            keysValues = new HashMap<>();
        }

        public int get(int key) {
            if (keysValues.containsKey(key)) {
                nodos.remove((Object) key);
                nodos.push(key);
                return keysValues.get(key);
            }else{
                return-1;
            }
        }

        public void put(int key, int value) {

            if (keysValues.containsKey(key)){
                keysValues.replace(key,value);
                nodos.remove((Object) key);
                nodos.push(key);
                return;
            }

            if (this.capacity == keysValues.size()){
                keysValues.remove(nodos.getLast());
                keysValues.put(key,value);
                nodos.removeLast();
                nodos.push(key);
            }else{
                keysValues.put(key,value);
                nodos.push(key);
            }
        }
    }