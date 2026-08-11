class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        let parents = new Array(n).fill(1).map((_, i) => i);

        let find = (v) => {
            if (v === parents[v]) return v;
            return (parents[v] = find(parents[v]));
        };

        let union = (p, q) => {
            let parentP = find(p);
            let parentQ = find(q);

             if (parentP === parentQ) return;

            if (parentP > parentQ) {
                parents[parentP] = parentQ;
            } else {
                parents[parentQ] = parentP;
            }
        };

        for (let [s, e] of edges) {
            union(s, e);
        }

        const roots = parents.map((_, node) => find(node));

        return new Set(roots).size;
    }
}
 
