interface CacheNode {
    key: number;
    value: number;
    prev: CacheNode | null;
    next: CacheNode | null;
}

class LRUCache {
    private capacity: number;
    private map: Map<number, CacheNode>;
    private head: CacheNode | null;
    private tail: CacheNode | null;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.map = new Map();
        this.head = null;
        this.tail = null;
    }

    private remove(node: CacheNode): void {
        const prevNode = node.prev;
        const nextNode = node.next;

        if (prevNode) prevNode.next = nextNode;
        if (nextNode) nextNode.prev = prevNode;

        if (this.head === node) this.head = nextNode;
        if (this.tail === node) this.tail = prevNode;
    }

    private insertAtHead(node: CacheNode): void {
        node.next = this.head;
        node.prev = null;

        if (this.head) {
            this.head.prev = node;
        }

        this.head = node;

        if (!this.tail) {
            this.tail = node;
        }
    }

    get(key: number): number {
        if (!this.map.has(key)) {
            return -1;
        }

        const node = this.map.get(key)!;
        this.remove(node);
        this.insertAtHead(node);

        return node.value;
    }

    put(key: number, value: number): void {
        if (this.map.has(key)) {
            const existingNode = this.map.get(key)!;
            this.remove(existingNode);
        }

        const newNode: CacheNode = { key, value, prev: null, next: null };
        this.insertAtHead(newNode);
        this.map.set(key, newNode);

        if (this.map.size > this.capacity) {
            const lru = this.tail!;
            this.remove(lru);
            this.map.delete(lru.key);
        }
    }
}
