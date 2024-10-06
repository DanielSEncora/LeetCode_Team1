function isMatch(s: string, p: string): boolean {
    let stringSize: number = s.length;
    let patternSize: number = p.length;
    let stringPointer: number = 0;
    let patternPointer: number = 0;

    if (!p.includes("*") && !p.includes(".")) {
        return s === p;
    }

    const match = (i: number, j: number): boolean => {
        if (i >= stringSize) return false;
        return s[i] === p[j] || p[j] === '.';
    };

    while (patternPointer < patternSize) {
        if (patternPointer + 1 < patternSize && p[patternPointer + 1] === '*') {
            if (isMatch(s.substring(stringPointer), p.substring(patternPointer + 2))) {
                return true;
            }

            while (stringPointer < stringSize && match(stringPointer, patternPointer)) {
                if (isMatch(s.substring(stringPointer + 1), p.substring(patternPointer + 2))) {
                    return true;
                }
                stringPointer++;
            }

            patternPointer += 2;
        } else {
            if (!match(stringPointer, patternPointer)) {
                return false;
            }
            stringPointer++;
            patternPointer++;
        }
    }

    return stringPointer === stringSize && patternPointer === patternSize;
}
