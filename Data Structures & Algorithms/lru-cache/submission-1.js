class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.map = new Map();
        this.capacity = capacity;
    }
    
    // this.map.keys()는 iterator를 반환하고, next로 첫 번째 [key,value]를 반환하기 때문에 O(1)로 처리 가능
    // map.keys()로 생성된 iterator 객체에서 next() 메서드는 배열의 shift()처럼 선입선출로 반환
    
    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if (!this.map.has(key)) return -1;
        const val = this.map.get(key);
        this.map.delete(key);
        this.map.set(key, val);
        return val;
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        this.map.delete(key);
        this.map.set(key, value);
        if (this.map.size > this.capacity) {
            const firstItem = this.map.keys().next().value;
            this.map.delete(firstItem);
        }
    }
}
