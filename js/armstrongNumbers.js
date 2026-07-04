function is_armstrong(num){
    let total = 0;
    let digits = String(num);
    let digitCount = digits.length

    for (const char of digits){
        total += Number(char) ** digitCount;
    }
    return total === num;
}


exports.findArmstrongNumbers = function findArmstrongNumbers(numbers){
    const result = [];

    for (const number of numbers)
        if (is_armstrong(number)){
            result.push(number)
        }
    return result
}   

