function faultyKeeb(inputStr) {
    /* Imagine you have a faulty keyboard. Whenever you type a vowel on it 
    (a,e,i,o,u,y), it reverses the string that you have written, instead of
    typing the character. Typing other characters works as expected.
    This function returns what whould be typed on such a keyboard.
    */
    if (typeof(inputStr) != 'string'){
        throw new TypeError(`input must be a string. Type was: ${typeof(inputStr)}`);
    }
    transformedString = ""
    normalisedInput = inputStr.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    vowels = "aeiouy"
    normalisedInput.split("").forEach((normChar, index) => {
        if (vowels.includes(normChar)){
            transformedString = transformedString.split("")
                .reverse()
                .join("")
        } else {
            transformedString += inputStr.charAt(index)
        }
    })
    return transformedString
}

// unit tests
testTupples = [
    // [input, expected output]
    ["string", "rtsng"],
    ["hello world!", "w hllrld!"],
    ["texte accentué", "cctxt nt"]
]

testTupples.forEach(testData => {
    output = faultyKeeb(testData[0])
    console.assert(output == testData[1],
        `Unit Test failed - input, actual output, \
expected output = '${testData[0]}', '${output}', '${testData[1]}'`)
})
