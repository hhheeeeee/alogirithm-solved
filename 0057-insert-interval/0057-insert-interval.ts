function insert(intervals: number[][], newInterval: number[]): number[][] {
    let [newStart, newEnd] = newInterval, left = [], right = [];
    for( let int of intervals ){
        let [start, end] = int;
        if( end < newStart )left.push(int);
        else if( start > newEnd )right.push(int);
        else {
            newStart = Math.min(start, newStart);
            newEnd = Math.max(end, newEnd);
        }
    }
    return [...left, [newStart, newEnd], ...right]
};