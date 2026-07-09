class WordDictionary {
    constructor() {
        this.arr = [];
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
        this.arr.push(word);
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        if (word.includes(".")) {
            const reg = new RegExp("^" + word + "$");
            for (let w of this.arr) {
                if (w.search(reg) >= 0) {
                    return true;
                }
            }
            return false;
        } else {
            if (this.arr.find((v) => v == word)) {
                return true;
            }
            return false;
        }
    }
}
