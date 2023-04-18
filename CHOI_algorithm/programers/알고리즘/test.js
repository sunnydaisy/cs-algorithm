function getObj(i) {

    return ({
        "id": i+1,
        "title": "Product " + i,
        "price": Math.floor(Math.random() * 31) * 1000,
        "content": "This is Product " + i,
        "size" : ["S", "M", "L", "XL"],
        "color" : ["white", "grey", "black", "blue"],
        "category": "top",
        "recommend" : Math.floor(Math.random() * 31),
        "src": "/product{i+1}.jpg"
    })
}
let result = [];
for (let i = 0; i<30; i++) {
    result.push(JSON.stringify(getObj(i)));
}

console.log(result);