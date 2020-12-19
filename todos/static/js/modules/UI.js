class DynamicUI{
    parent="";child=""
    constructor({parentID,contents}){
        this.parent=parentID;this.contents=contents
    }
    appendElement(){
        var parent_elm=document.getElementById(this.parent)
        if(parent_elm!=null && parent_elm!=undefined){
            parent_elm.appendChild(this.child)
            return true
        }else{return false}
    }
}