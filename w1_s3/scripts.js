// Given two numbers, return the sum of those two numbers.
function sumTwoNums(num1, num2) {
    return num1 + num2
}


// ########################## //


// Iterate from 0 to 255 adding odd numbers to an array and logging a message for even numbers. Return the array.
function returnOddArray() {
    let oddArray = []

    for(let i = 0; i <= 255; i++) {
        if(i % 2 == 1) {
            oddArray.push(i)
        } else {
            console.log('Even number ' + i + ' was ignored')
        }
    }

    return oddArray
}


// ########################## //


// Given an array, return a reversed version of the array.
function reverseArray(arr) {
    let reversedArray = []

    for(let i = arr.length - 1; i >= 0; i--) {
        reversedArray.push(arr[i])
    }

    return reversedArray
}


// ########################## //


// Given an object, console log each key/value pair (bonus objective: log each pair in the same line).
function logKeyValue(obj) {
    for(let key in obj) {
        console.log(key)
        console.log(obj[key])
    }
}


// ########################## //


// Given a string, loop through the string and log any vowels
function logVowels(str) {
    let vowels = ['a', 'e', 'i', 'o', 'u']

    for(let i = 0 ; i < str.length; i++) {
        for(let x = 0; x < vowels.length; x++) {
            if(str[i] === vowels[x]) {
                console.log(str[i])
                break
            }
        }
    }
}

logVowels('hello world')


// ########################## //


// Given a string and two index values, return a new string comprised of only the letters in the range of the two indices.
// E.g. newSubString('hello', 1, 3) -> 'ell'
function newSubString(str, idx1, idx2) {
    let newString = ''
    for(let i = idx1; i <= idx2; i++) {
        newString += str[i]
    }
    return newString
}


// ########################## //