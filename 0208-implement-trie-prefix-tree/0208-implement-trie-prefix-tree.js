var Node = function (key, data = null) {
    this.key
    this.data = data
    this.children = {}
}


var Trie = function () {
     this.head = new Node(null);
}

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
    let cur = this.head

    for (let c of word) {
        if (!Object.keys(cur.children).includes(c)) {
            cur.children[c] = new Node(c)
        }
        cur = cur.children[c]
    }
    cur.data = word
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
    let cur = this.head

    for (let c of word) {
        if (Object.keys(cur.children).includes(c)) {
            cur = cur.children[c]
        } else {
            return false
        }
    }

    if (cur.data !== null)  {
        return true
    } return false
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
    let cur = this.head

    for (let c of prefix) {
        if (Object.keys(cur.children).includes(c)) {
            cur = cur.children[c]
        } else {
            return false
        }
    }

   return true
};


/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */