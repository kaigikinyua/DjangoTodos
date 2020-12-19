import {Messages} from './Messages.js';
class DynamicUI{
    parent="";
    constructor({parentID}){
        this.parent=parentID;
    }
    appendElement(child){
        var parent_elm=document.getElementById(this.parent)
        if(parent_elm!=null && parent_elm!=undefined){
            parent_elm.appendChild(child)
            return true
        }else{return false}
    }
    hideElement(){
        if(elem_exists(this.parent)){
            var elem=document.getElementById(this.parent)
            elem.style.display="none"
        }
        
    }
}

function elem_exists(elem){
    var elem=document.getElementById(elem)
    if(elem!=undefined && elem!=null){
        return true
    }else{
        Messages.showError("Element by id "+elem+" does not exist");
        return false
    }
}

export {DynamicUI}
