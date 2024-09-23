/*

You're designing a smart laundry sorting system. 
You have a list of clothing items, each with a color and a fabric type. 
Sort these items into the minimum number of loads n and return n, where items 
of the same color can be washed together, and some different fabric types 
cannot be mixed together. "Normal" fabric types can be mixed with "heavy", 
but "delicate" cannot be mixed with anything. 

*/

function minLaundryLoads(load) {
    // Rules are: 
    // * clothes must be bundled by colors (red with red, blue with blue, ...)
    // * fabric type "delicate" must not be mixed with other types

    // What this function does: for each item of the load,
    // use the 2 rules above to assign each item to a bundle
    // Then, count the number of bundles.
    // "How many items are there in a bundle?" -> unknown, but not needed

    const DELICATE = "delicate"
    const uniqueValues = new Set()

    for (let i = 0; i < load.length; i++) {
        const color = load[i][0];
        const fabricType = load[i][1];
        // below is the trickery so set "delicate" items appart.
        const bundleableObject = color + (fabricType == DELICATE ? "D" : "")
        
        uniqueValues.add(bundleableObject)
    }
    return uniqueValues.size
}

function tests(){
    let load1 = [
        ["red", "normal"], // X
        ["blue", "normal"], // Y
        ["red", "delicate"], // Z
        ["blue", "heavy"] // Y
    ]
    
    let load2 = [
        ["white", "normal"], // Y
        ["white", "delicate"], // X
        ["white", "normal"], // Y
        ["white", "heavy"] // Y
    ]

    console.log("test OK ?", minLaundryLoads(load1) == 3)
    console.log("test OK ?", minLaundryLoads(load2) == 2)
}

tests()