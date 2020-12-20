class Requests{
    url=""
    constructor({url}){}
    get(callback){
        fetch(url)
        .then(res=>{res.json()})
        .then(data=>{
            callback(data)
        })
    }
    post(postData,callback){
        fetch(url,
            {"method":"POST",
            "data":postData}
        ).then(res=>{res.json()})
        .then(data=>{callback(data)})
    }
}